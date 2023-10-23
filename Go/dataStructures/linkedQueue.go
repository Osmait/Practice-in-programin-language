package datastructures

type node struct {
	Data any
	Next *node
}

type Queue struct {
	head   *node
	tail   *node
	length int
}

func (ll *Queue) enqueue(n any) {
	var newNode node
	newNode.Data = n

	if ll.tail != nil {
		ll.tail.Next = &newNode
	}
	ll.tail = &newNode
	if ll.head == nil {
		ll.head = &newNode
	}
	ll.length++
}

func (ll *Queue) dequeue() any {
	if ll.isEmpty() {
		return -1
	}
	data := ll.head.Next
	ll.head = ll.head.Next
	if ll.head == nil {
		ll.tail = nil
	}
	ll.length--
	return data
}

// isEmpty it will check our list is empty or not
func (ll *Queue) isEmpty() bool {
	return ll.length == 0
}

// len is return the length of queue
func (ll *Queue) len() int {
	return ll.length
}

// frontQueue it will return the front data
func (ll *Queue) frontQueue() any {
	return ll.head.Data
}

// backQueue it will return the back data
func (ll *Queue) backQueue() any {
	return ll.tail.Data
}
