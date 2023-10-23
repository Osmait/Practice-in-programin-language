package datastructures

import "testing"

func TestQueue(t *testing.T) {
	queue := Queue{}

	queue.enqueue("prueba")
	queue.enqueue("prueba2")
	if queue.len() != 2 {
		t.Errorf("Fail test  want %d and recive %d", 2, queue.len())
	}

	queue.dequeue()
	if queue.len() != 1 {
		t.Errorf("Fail test  want %d and recive %d", 1, queue.len())
	}
}
