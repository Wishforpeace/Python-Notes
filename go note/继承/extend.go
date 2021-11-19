type Engine interface {
	Run()
	Stop()
}
type Bus struct{
	Engine
}
func (c *Bus) Working()  {
	c.Run()
	c.Stop()
}