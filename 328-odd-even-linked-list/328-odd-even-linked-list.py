class Solution:
    def oddEvenList(self, root: Optional[ListNode]) -> Optional[ListNode]:
            head = dummy = ListNode(0)
            head2 = dummy2 = ListNode(0)
            i = 0
            while root:
                if i % 2 != 0:
                    head.next = ListNode(root.val)
                    head =head.next
                if i % 2 == 0:
                    head2.next = ListNode(root.val)
                    head2 = head2.next 
                root = root.next
                i+=1
            head2.next = dummy.next
            return dummy2.next