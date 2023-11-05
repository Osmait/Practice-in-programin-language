package strategy

import "fmt"

type Lru struct{}

func (s *Lru) evict(c *Cache) {
	fmt.Println("Evicting by lru strtegy")
}
