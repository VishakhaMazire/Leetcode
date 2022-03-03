class Solution:
    def frequencySort(self, s: str) -> str:
        heap, cnt = [], Counter(s)
        ret = ''
        for key in cnt:
            heappush(heap, (-cnt[key], key))
        while len(heap) > 0:
            cur = heappop(heap)
            ret += cur[1] * (-cur[0])
        return ret