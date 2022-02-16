class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        else:
            while len(stones) > 1:
                s = sorted(stones)
                x = s.pop(-1)
                y = s.pop(-1)
                if x != y:
                    s.append(x - y)
                if s == []:
                    return 0
                stones = s
            return stones[0]