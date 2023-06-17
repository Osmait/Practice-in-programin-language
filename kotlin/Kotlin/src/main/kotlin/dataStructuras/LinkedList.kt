package dataStructuras


class ListNode(var valor:Int){
    var next: ListNode? = null
}
class LinkedList {
    private var head: ListNode? = null

    fun  addNode(valor:Int){
        val newNode = ListNode(valor)
        if (head == null){
            head = newNode

        }else{
            var current = head
            while (current?.next != null){
                current = current.next
            }
            current?.next = newNode
        }
    }

    fun  printList(){
        var current = head
        while(current != null){
            print("${current.valor} ${if(current.next != null) "->" else ""} ")
            current = current.next
        }
        println()
    }

}

fun main(){
    val  linkedList = LinkedList()
    linkedList.addNode(1)

    linkedList.addNode(2)
    linkedList.addNode(3)
    linkedList.addNode(4)

    linkedList.printList()
}