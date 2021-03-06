class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            
            if i in {"{", "(", "["}:
                stack.append(i)
            else:
                if not stack: return False
                char = stack.pop()
                if i == "}":
                    if char != "{": return False
                
                if i == ")":
                    if char != "(": return False
                
                if i == "]":
                    if char != "[": return False
        return len(stack) == 0