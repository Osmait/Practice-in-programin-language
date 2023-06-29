use std::{fmt::Display, ptr::NonNull};

#[derive(Debug)]
struct Node<T> {
    val: T,
    next: Option<NonNull<Node<T>>>,
}

impl<T> Node<T> {
    fn new(t: T) -> Node<T> {
        Node { val: t, next: None }
    }
}
#[derive(Debug)]
pub struct Queue<T> {
    length: i32,
    head: Option<NonNull<Node<T>>>,
}
impl<T> Queue<T> {
    pub fn new() -> Queue<T> {
        Queue {
            length: 0,
            head: None,
        }
    }

    pub fn enqueu(&mut self, value: T) {
        let new_node = Box::into_raw(Box::new(Node::new(value)));
        let new_node = NonNull::new(new_node).expect("Erro Allocate Node in Memory");
        if let Some(mut temp) = self.head {
            while let Some(next) = unsafe { temp.as_ref().next } {
                temp = next;
            }
            unsafe {
                temp.as_mut().next = Some(new_node);
            }
        } else {
            self.head = Some(new_node);
        }
        self.length += 1;
    }
    pub fn dequeue(&mut self) -> Option<T> {
        if let Some(old_head) = self.head {
            let old_val = unsafe { Box::from_raw(old_head.as_ptr()) }.val;
            self.head = unsafe { old_head.as_ref().next };
            self.length -= 1;
            Some(old_val)
        } else {
            None
        }
    }
}

impl<T> Display for Node<T>
where
    T: Display,
{
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        match self.next {
            Some(node) => write!(f, "{},{}", self.val, unsafe { node.as_ref() }.val),
            None => write!(f, "{}", self.val),
        }
    }
}

impl<T> Display for Queue<T>
where
    T: Display,
{
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        match self.head {
            Some(node) => write!(f, "{}", unsafe { node.as_ref() }.val),
            None => Ok(()),
        }
    }
}
