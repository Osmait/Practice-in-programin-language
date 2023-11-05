
import { assertEquals } from "https://deno.land/std@0.192.0/testing/asserts.ts";

type NodeQueue<T> = {
  value: T,
  next?: NodeQueue<T>
}


export class LinkedQueue<T>{
  public size: number;
  public head?: NodeQueue<T>;
  private tail?: NodeQueue<T>;

  constructor() {
    this.head = this.tail = undefined;
    this.size = 0;
  }
  enqueue(item: T): void {
    const node = { value: item } as NodeQueue<T>;
    this.size++

    if (!this.tail) {
      this.tail = this.head = node;
      return
    }
    this.tail.next = node
    this.tail = node
  }
  dequeue(): T | undefined {
    if (!this.head) throw new Error("Queue UnderFlow")
    this.size--
    const head = this.head;
    this.head = this.head.next
    return head.value
  }


  /**
  * Returns the item at the front of the queue.
  *
  * @returns The item at the front of the queue or null if the queue is empty.
  */
  peek(): T | undefined | null {

    if (this.isEmpty()) {
      return null;
    }
    return this.head?.value;
  }

  /**
   * Checks if the queue is empty.
   *
   * @returns {boolean} Whether the queue is empty or not.
   */
  isEmpty(): boolean {
    return this.size === 0
  }

  /**
   * Returns the number of items in the queue.
   *
   * @returns {number} The number of items in the queue.
   */
  length(): number {
    return this.size;
  }
}


Deno.test(() => {
  const queue = new LinkedQueue()
  queue.enqueue("hola")
  assertEquals(queue.length() === 1)

})
