package dataStructure;

public class Node {

    int value;


    Node next;

    Node() {}


    Node(int value) {
        this(value, null);
    }

    Node(int value, Node next) {
        this.value = value;
        this.next = next;
    }

}
