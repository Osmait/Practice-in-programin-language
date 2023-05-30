package strategy

import "fmt"

type Fifo struct {
}

func (l *Fifo) evict(c *Cache) {
	fmt.Println("Evincting by fifo strtegy")
}
