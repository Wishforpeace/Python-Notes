package main
import "fmt"
//正方形结构体
type Square struct {
	sidenLen float32
}
//三角形结构体
type Triangle struct {
	Bottom float32
	Height float32
}
func (t *Triangle) Area() float32 {
	return (t.Bottom * t.Height)/2
}
//接口 Shape
type Shape interface {
	Area() float32
}
//计算正方形的面积
func (sq *Square) Area() float32{
	return sq.sidenLen * sq.sidenLen
}

func main()  {
	t := &Triangle{6,8}
	s := &Square{8}
	shapes := []Shape{t,s}//创建Shape类型的数组
	for n,_ := range shapes{
		fmt.Println("图形数据：",shapes[n])
		fmt.Println("它的面积是：",shapes[n].Area)
	}	
}