class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None:
            return False
        
        visited = set()
        cur_node = head
        
        while cur_node not in visited:
            visited.add(cur_node)
            
            if cur_node.next is None:
                return False
            
            cur_node = cur_node.next
        return True