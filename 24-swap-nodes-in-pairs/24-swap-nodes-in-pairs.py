class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans = head
        mod = 1
        while head != None and head.next:
            if mod%2 != 0:
                temp = head.val 
                head.val = head.next.val
                head.next.val = temp
            mod += 1
            head = head.next
        return ans