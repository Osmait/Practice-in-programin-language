package datastructures

type Node[T any] struct {
	Val  T
	Prev *Node[T]
	Next *Node[T]
}

// Create new node.
func NewNode[T any](val T) *Node[T] {
	return &Node[T]{val, nil, nil}
}
