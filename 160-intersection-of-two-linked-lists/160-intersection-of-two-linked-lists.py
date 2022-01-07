class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        def list_len(node: ListNode) -> int:
            l = 0
            while node:
                l += 1
                node = node.next
            return l
                
        len_A = list_len(headA)
        len_B = list_len(headB)
        if len_A > len_B:
            headA, headB = headB, headA
            len_A, len_B = len_B, len_A
            
        for i in range(len_B - len_A):
            headB = headB.next
            
        while headA:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
            
        return None