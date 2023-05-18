package datastructures

import (
	"errors"
	"fmt"
)

type Singly[T any] struct {
	length int
	head   *Node[T]
}

func NewSingly[T any]() *Singly[T] {
	return &Singly[T]{}
}

func (s *Singly[T]) AddAtBeg(val T) {
	n := NewNode(val)
	n.Next = s.head
	s.head = n
	s.length++
}

func (s *Singly[T]) AddAtEnd(val T) {
	n := NewNode(val)
	if s.head == nil {
		s.head = n
		s.length++
		return
	}
	cur := s.head
	for ; cur.Next != nil; cur = cur.Next {
	}
	cur.Next = n
	s.length++
}

func (s *Singly[T]) DelAtBeg() (T, bool) {
	if s.head == nil {
		var r T
		return r, false
	}
	cur := s.head
	s.head = cur.Next
	s.length--
	return cur.Val, true
}

func (s *Singly[T]) DelAtEnd() (T, bool) {
	if s.head == nil {
		var r T
		return r, false
	}
	if s.head.Next == nil {
		return s.DelAtBeg()
	}
	cur := s.head

	for ; cur.Next.Next != nil; cur = cur.Next {
	}
	retval := cur.Next.Val
	cur.Next = nil
	s.length--
	return retval, true
}

func (s *Singly[T]) DelByPos(pos int) (T, bool) {
	switch {
	case s.head == nil:
		var r T
		return r, false
	case pos-1 > s.length:
		var r T
		return r, false
	case pos-1 == 0:
		return s.DelAtBeg()
	case pos-1 == s.Count():
		return s.DelAtEnd()
	}
	var prev *Node[T]
	var val T
	cur := s.head
	count := 0

	for count < pos-1 {
		prev = cur
		cur = cur.Next
		count++
	}
	val = cur.Val
	prev.Next = cur.Next
	s.length--
	return val, true

}

func (s *Singly[T]) Count() int {
	return s.length
}

func (s *Singly[T]) Reverse() {
	var prev, Next *Node[T]
	cur := s.head

	for cur != nil {
		Next = cur.Next
		cur.Next = prev
		prev = cur
		cur = Next
	}
	s.head = prev
}

func (s *Singly[T]) ReversePartition(left, right int) error {
	err := s.checkPartition(left, right)
	if err != nil {
		return err
	}
	tmpNode := &Node[T]{}
	tmpNode.Next = s.head
	pre := tmpNode
	for i := 0; i < left-1; i++ {
		pre = pre.Next
	}
	cur := pre.Next

	for i := 0; i < right-left; i++ {
		next := cur.Next
		cur.Next = next.Next
		next.Next = pre.Next
		pre.Next = next
	}
	s.head = tmpNode.Next
	return nil
}

func (s *Singly[T]) checkPartition(left, right int) error {
	if left > right {
		return errors.New("left boundary must smaller than right")
	} else if left < 1 {
		return errors.New("left boundary starts from the first node")
	} else if right > s.length {
		return errors.New("right boundary cannot be greater than the length of the linked list")
	}
	return nil
}

func (s *Singly[T]) Display() {
	for cur := s.head; cur != nil; cur = cur.Next {
		fmt.Print(cur.Val, "<-")
	}

	fmt.Print("\n")
}
