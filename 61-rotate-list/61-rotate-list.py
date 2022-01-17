class Solution(object):
    def rotateRight(self, head, k):
        if not head:
            return None
        length = 0
        temp = head
        tail = head
        while temp:
            length +=1
            tail = temp
            temp=temp.next
        tail.next = head
        k = k%length
        foward = length - k -1
        temp = head
        for _ in range(foward):
            temp = temp.next
        ans = temp.next
        temp.next = None
        return ans