class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        return [n for n, i in sorted(sorted((n, i) for i, n in
                                            enumerate(nums))[-k:],
                                     key=lambda t: t[1])]