use std::ptr::NonNull;

struct Node<T> {
    val: T,
    next: Option<NonNull<Node<T>>>,
}

impl<T> Node<T> {
    fn new(t: T) -> Node<T> {
        Node { val: t, next: None }
    }
}

struct LinkedQueue<T> {
    head: Option<NonNull<Node<T>>>,
    tail: Option<NonNull<Node<T>>>,
    length: usize,
}
impl<T> Default for LinkedQueue<T> {
    fn default() -> Self {
        Self::new()
    }
}

impl<T> LinkedQueue<T> {
    pub fn new() -> Self {
        Self {
            head: None,
            tail: None,
            length: 0,
        }
    }

    pub fn enqueue(&mut self, n: T) {
        let node = Box::new(Node::new(n));
        let node_ptr = NonNull::new(Box::into_raw(node));
        self.length += 1;
        match self.tail {
            None => {
                self.tail = node_ptr;
                self.head = node_ptr;
                return;
            }

            Some(head_ptr) => unsafe { (*head_ptr.as_ptr()).next = node_ptr },
        };
        self.tail = node_ptr;
    }
    pub fn dequeue(&mut self) -> Option<T> {
        match self.head {
            None => panic!("Queue UnderFlow"),
            Some(head_ptr) => {
                self.length += 1;
                let head = self.head;
                unsafe { (*head_ptr.as_ptr()).next = head };
                head.map(|i| unsafe { Box::from_raw(i.as_ptr()).val })
            }
        }
    }

    pub fn is_empty(&mut self) -> bool {
        self.length == 0
    }
    pub fn len(&mut self) -> usize {
        self.length
    }
}

#[cfg(test)]
mod tests {
    use super::LinkedQueue;

    #[test]
    fn test_enqueue() {
        let mut queue: LinkedQueue<u8> = LinkedQueue::new();
        queue.enqueue(64);
        assert!(!queue.is_empty());
    }

    #[test]
    fn test_dequeue() {
        let mut queue: LinkedQueue<u8> = LinkedQueue::new();
        queue.enqueue(32);
        queue.enqueue(64);
        let retrieved_dequeue = queue.dequeue();
        assert_eq!(retrieved_dequeue, Some(32));
    }

    #[test]
    fn test_size() {
        let mut queue: LinkedQueue<u8> = LinkedQueue::new();
        queue.enqueue(8);
        queue.enqueue(16);
        assert_eq!(2, queue.len());
    }
}
