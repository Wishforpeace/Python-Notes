package person
type Student struct{
	name string
	score float32
}
//获取name
func(s *Student) GetName() string {
	return s.name
}
//设置 name
func (s *Student) SetName(newName string){
	s.name = nemName
}