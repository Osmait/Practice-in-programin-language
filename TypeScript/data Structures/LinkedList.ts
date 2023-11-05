/**
 * Represents a node in a linked list.
 *
 * @template T The type of the data stored in the node.
 * @property data The data stored in the node.
 * @property next A reference to the next node in the list. Can reference to null, if there is no next element.
 */

class ListNode<T> {
  constructor(public data: T, public next?: ListNode<T>) {}
}

export class SinglyLinkedList<T> {
  private head?: ListNode<T>;
  private tail?: ListNode<T>;
  private length: number;

  constructor() {
    this.head = undefined;
    this.tail = undefined;
    this.length = 0;
  }

  public isEmpty(): boolean {
    return !this.head;
  }

  public get(index: number): T | null {
    if (index < 0 || index >= this.length) return null;
    if (this.isEmpty()) return null;
    let current: ListNode<T> = this.head!;

    for (let i = 0; i < index; i++) {
      if (!current.next) return null;
      current = current.next;
    }
    return current.data;
  }

  push(data: T): void {
    const node: ListNode<T> = new ListNode<T>(data);
    if (this.isEmpty()) {
      this.head = node;
      this.tail = node;
    } else {
      node.next = this.head;
      this.head = node;
    }
    this.length++;
  }
  pop(): T {
    if (this.isEmpty()) throw new Error("index out of bounds");
    const node: ListNode<T> = this.head!;
    this.head = this.head!.next;
    this.length--;
    return node.data;
  }
  append(data: T): void {
    const node: ListNode<T> = new ListNode<T>(data);
    if (this.isEmpty()) {
      this.head = node;
    } else {
      this.tail!.next = node;
    }
    this.tail = node;
    this.length++;
  }

  removeTail(): T {
    if (!this.head) {
      throw new Error("index out of bounds");
    }
    const currentTail = this.tail;
    if (this.head === this.tail) {
      this.head = undefined;
      this.tail = undefined;
      this.length--;

      return currentTail!.data;
    }
    let currentNode: ListNode<T> = this.head;
    while (currentNode.next !== currentTail) {
      currentNode = currentNode.next!;
    }
    this.tail = currentNode;
    this.length--;
    return currentTail!.data;
  }

  insertAt(index: number, data: T): void {
    if (index < 0 || index > this.length)
      throw new Error("index out of bounds");
    if (index === 0) {
      this.push(data);
      return;
    }
    if (index === this.length) {
      this.append(data);
      return;
    }
    const newNode: ListNode<T> = new ListNode<T>(data);
    let currentNode: ListNode<T> | undefined = this.head;
    for (let i = 0; i < index - 1; i++) {
      currentNode = currentNode?.next;
    }
    const nextNode = currentNode?.next;
    currentNode!.next = nextNode;
    newNode.next = nextNode;

    this.length++;
  }

  removeAt(index: number): T {
    if (index < 0 || index >= this.length)
      throw new Error("index out of bounds");
    if (index === 0) return this.pop();
    if (index === this.length - 1) return this.removeTail();
    let previousNode: ListNode<T> | undefined;
    let currentNode: ListNode<T> | undefined = this.head;
    for (let i = 0; i < index - 1; i++) {
      if (i === index - 1) previousNode = currentNode;
      currentNode = currentNode?.next;
    }
    previousNode!.next = currentNode!.next;
    this.length--;

    return currentNode!.data;
  }

  clear(): void {
    this.head = undefined;
    this.tail = undefined;
    this.length = 0;
  }

  toArray(): T[] {
    const array: T[] = [];
    let currentNode: ListNode<T> | undefined = this.head;
    while (currentNode) {
      array.push(currentNode.data);
      currentNode = currentNode.next;
    }
    return array;
  }
  getLength(): number {
    return this.length;
  }
}

const list = new SinglyLinkedList<number>();

list.append(1);
list.append(2);
list.push(3);

// list.clear();
console.log(list.isEmpty());
