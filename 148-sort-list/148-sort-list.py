# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def merge(head1, head2):
            dummy_head = cur_ptr = ListNode()
            while head1 and head2:
                if head1.val <= head2.val:
                    cur_ptr.next = ListNode(head1.val)
                    head1 = head1.next
                else:
                    cur_ptr.next = ListNode(head2.val)
                    head2 = head2.next 
                cur_ptr = cur_ptr.next
                if head1: cur_ptr.next = head1
                if head2: cur_ptr.next = head2
            return dummy_head.next
        
        def mergeSort(head):
            if not head:
                return
            if not head.next:
                return head
            prev = slow = fast = head
            while fast and fast.next:
                prev = slow
                slow = slow.next
                fast = fast.next.next
            prev.next = None
            
            head1, head2 = head, slow
            head1 = mergeSort(head1)
            head2 = mergeSort(head2)
            return merge(head1, head2)
        
        return mergeSort(head)