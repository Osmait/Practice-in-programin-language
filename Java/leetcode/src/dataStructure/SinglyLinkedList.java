package dataStructure;

import java.util.StringJoiner;

public class SinglyLinkedList  extends Node{
    private Node head;

    private int size;

    public SinglyLinkedList(){
        head = null;
        size = 0;
    }
    public SinglyLinkedList(Node head,int size){
        this.head = head;
        this.size = size;
    }
    public boolean detectLoop(){
        Node slow = head;
        Node fast = head;
        while(fast!=null && fast.next!=null && fast.next.next!=null){
            fast = fast.next.next;
            slow = slow.next;
            if(slow == fast){
                return true;
            }
        }
        return false;

    }
    public Node middle() {
        if (head == null) {
            return null;
        }
        Node firstCounter = head;
        Node secondCounter = firstCounter.next;
        while (secondCounter != null && secondCounter.next != null) {
            firstCounter = firstCounter.next;
            secondCounter = secondCounter.next.next;
        }
        return firstCounter;
    }

    public void swapNodes(int valueFirst, int valueSecond) {
        if (valueFirst == valueSecond) {
            return;
        }
        Node previousA = null, currentA = head;
        while (currentA != null && currentA.value != valueFirst) {
            previousA = currentA;
            currentA = currentA.next;
        }

        Node previousB = null, currentB = head;
        while (currentB != null && currentB.value != valueSecond) {
            previousB = currentB;
            currentB = currentB.next;
        }
        /** If either of 'a' or 'b' is not present, then return */
        if (currentA == null || currentB == null) {
            return;
        }

        // If 'a' is not head node of list
        if (previousA != null) {
            previousA.next = currentB;
        } else {
            // make 'b' as the new head
            head = currentB;
        }

        // If 'b' is not head node of list
        if (previousB != null) {
            previousB.next = currentA;
        } else {
            // Make 'a' as new head
            head = currentA;
        }
        // Swap next pointer

        Node temp = currentA.next;
        currentA.next = currentB.next;
        currentB.next = temp;
    }

    public Node reverseList(Node node){
        Node prevNode = head;
        while (prevNode.next != null) {
            prevNode = prevNode.next;
        }
        Node prev = null,curr = node ,next;
        while (curr != null) {
            next = curr.next;
            curr.next = prev;
            prev = curr;
            curr = next;
        }
        prevNode.next = prev;
        return head;
    }
    public void clear(){
        Node cur = head;
        while(cur!=null){
            Node prev = cur;
            cur = cur.next;
            prev = null;
        }
        head = null;
        size = 0;
    }
    public boolean isEmpty(){
        return size == 0;
    }
    public int size(){
        return size;
    }
    public void setHead(Node head){
        this.head = head;
    }
    public int count(){
        int count = 0;
        Node cur = head;
        while(cur!=null){
            cur = cur.next;
            count++;
        }
        return count;
    }
    public boolean search(int value){
        Node cur = head;
        while(cur!=null){
            if(cur.value == value){
                return true;
            }
            cur = cur.next;
        }
        return false;
    }
    @Override
    public String toString(){
        StringJoiner joiner = new StringJoiner("->");
        Node cur = head;
        while (cur!=null){
            joiner.add(cur.value+"->");
            cur = cur.next;
        }
        return joiner.toString();
    }

    public  void deleteDuplicates(){
        Node pred = head;
        Node newHead = head;
        while(pred!=null){
            if (newHead.next !=null && newHead.value == newHead.next.value){
                while (newHead.next !=null && newHead.value == newHead.next.value){
                    newHead = newHead.next;
                }
                pred.next = newHead.next;
                newHead = null;
            }
            pred = pred.next;
            newHead = pred;

        }

    }
    public void print(){
        Node temp = head;
        while (temp!=null && temp.next!=null){
            System.out.println("->");
            temp = temp.next;
        }
        if (temp!=null){
            System.out.println(temp.value);
            System.out.println();
        }
    }
    public void insetHead(int x){
        insertNth(x,0);

    }

    public void insert(int data) {
        insertNth(data, size);
    }

    public void insertNth(int data, int position) {
        checkBounds(position, 0, size);
        Node newNode = new Node(data);
        if (head == null) {
            /* the list is empty */
            head = newNode;
            size++;
            return;
        }
        if (position == 0) {
            /* insert at the head of the list */
            newNode.next = head;
            head = newNode;
            size++;
            return;
        }

        Node cur = head;
        for (int i = 0; i < position - 1; ++i) {
            cur = cur.next;
        }
        newNode.next = cur.next;
        cur.next = newNode;
        size++;
    }

    public void deleteHead() {
        deleteNth(0);
    }

    /**
     * Deletes an element at the tail
     */
    public void delete() {
        deleteNth(size - 1);
    }

    public void deleteNth(int position) {
        checkBounds(position, 0, size - 1);
        if (position == 0) {
            Node destroy = head;
            head = head.next;
            destroy = null;
            /* clear to let GC do its work */
            size--;
            return;
        }
        Node cur = head;
        for (int i = 0; i < position - 1; ++i) {
            cur = cur.next;
        }

        Node destroy = cur.next;
        cur.next = cur.next.next;
        destroy = null; // clear to let GC do its work

        size--;
    }
    public int getNth(int index) {
        checkBounds(index, 0, size - 1);
        Node cur = head;
        for (int i = 0; i < index; ++i) {
            cur = cur.next;
        }
        return cur.value;
    }

    public void checkBounds(int position, int low, int high) {
        if (position > high || position < low) {
            throw new IndexOutOfBoundsException(position + "");
        }
    }




}
