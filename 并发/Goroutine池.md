# Goroutine池

1.前言

+ goroutine虽然很小，但是当无休止的Goroutine会出现高频率的调度Goroutine，会浪费很多资源的同时占用很多内存。设计goroutine池，限制协程上限，重用协程，不要每次都去创建一个新的协程。

2.作用

+ 大量的goroutine会占用很大的内存，goroutine池可以减轻内存负担
+ 性能消耗：重复的创建与销毁goroutine，大量的goroutine调度等会占用资源，goroutine池可以减轻资源消耗
+ 减少goroutine创建时间，提高效率
+ 管理协程，控制并发量，定期回收等

3.实现思路

+ 启动服务等时候 初始化一个Goroutine Pool，这个协程池维护了任务的管道和worker。
+ 外部请求投递到Goroutine Pool，Goroutine Pool的操作是：判断当前运行的worker是否已经超过了Pool的容量，如果超过就将请求放到任务管道中知道运行的worker将管道中的任务执行，如果没有超过就重新开一个worker处理。

4.代码实现

     ```go
     package main
     
     import (
     	"fmt"
     	"time"
     )
     
     type Task struct {
     	F func()
     }
     
     // 创建任务
     func NewTask(f func()) *Task {
     	task := Task{F: f}
     	return &task
     }
     
     // 任务调用
     func (t *Task) RunTask() {
     	t.F()
     }
     
     // 协程池
     type GoroutinePool struct {
     	CapNum int
     	// 进任务的管道
     	InChannel chan *Task
     	// 任务调度的管道
     	WorkChannel chan *Task
     }
     
     func NewPool(capnum int) *GoroutinePool {
     	pool := GoroutinePool{
     		CapNum:      capnum,
     		InChannel:   make(chan *Task),
     		WorkChannel: make(chan *Task),
     	}
     	return &pool
     }
     
     // 从InChannel管道拿到任务，放入WorkChannel
     func (p *GoroutinePool) TaskInChannelOut() {
     	for task := range p.InChannel {
     		p.WorkChannel <- task
     	}
     }
     
     // 任务执行者从WorkChannel获取任务并执行
     func (p *GoroutinePool) Worker() {
     	for task := range p.WorkChannel {
     		task.RunTask()
     	}
     }
     
     func (p *GoroutinePool) PoolRun() {
     	// 任务执行
     	for i := 0; i < p.CapNum; i++ {
     		go p.Worker() //开启指定数量的协程执行任务
     	}
     	// 从InChannel管道拿到任务，本质是往WorkChannel里面添加任务
     	p.TaskInChannelOut()
     
     	close(p.WorkChannel)
     	close(p.InChannel)
     }
     
     // 1.从InChannel获取任务并写入WorkChannel
     // 2.从WordChannel里面获取任务并执行
     // 少了往InChannel写入任务
     func main() {
     	cap_num := 5
     
     	pool := NewPool(cap_num)
     	go func() {
     		for {
     			task := NewTask(func() {
     				fmt.Println(time.Now())
     			})
     			pool.InChannel <- task
     		}
     	}()
     
     	// 任务调度
     	pool.PoolRun()
     }
     
     ```

