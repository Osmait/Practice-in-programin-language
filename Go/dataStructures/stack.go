package datastructures

import (
	"sync"
)

type Stack[T any] struct {
	lock sync.Mutex
	data []T
}

func (s *Stack[T]) Push(item T) {
	s.lock.Lock()
	defer s.lock.Unlock()

	s.data = append(s.data, item)
}

func (s *Stack[T]) Pop() (T, error) {
	s.lock.Lock()
	defer s.lock.Unlock()

	// if len(s.data) == 0 {
	// 	return  ,fmt.Errorf("stack is empty")
	// }

	item := s.data[len(s.data)-1]
	s.data = s.data[:len(s.data)-1]
	return item, nil
}

func (s *Stack[T]) Peek() (T, error) {
	s.lock.Lock()
	defer s.lock.Unlock()

	// if len(s.data) == 0 {
	// 	return nil, fmt.Errorf("stack is empty")
	// }

	return s.data[len(s.data)-1], nil
}
