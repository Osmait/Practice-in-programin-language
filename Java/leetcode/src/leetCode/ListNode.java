package leetCode;

public class ListNode {

    public int val;
    public ListNode next;
    public ListNode(int val) {
        this.val = val;
    }

    public static ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        ListNode dummy = new ListNode(0);
        ListNode tail = dummy;
        while (l1 != null && l2 != null) {
            if (l1.val < l2.val) {
                tail.next = l1;
                l1 = l1.next;
            } else {
                tail.next = l2;
                l2 = l2.next;
            }
            tail = tail.next;
        }
        if (l1 != null) {
            tail.next = l1;
        }else  if (l2 != null) {
            tail.next = l2;
        }
        return dummy.next;

    }
}



