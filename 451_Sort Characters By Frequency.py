class Solution:
    def frequencySort(self, s: str) -> str:

        freq = {}

        for c in s:
            freq[c] = freq.get(c, 0) + 1
        
        import heapq
        heap = []

        for i in freq:
            heapq.heappush(heap, (-freq[i], i))

        ans = []
        for _ in range(len(heap)):
            item = heapq.heappop(heap)
            times, letter = -item[0], item[1]
            ans.append(times*letter)

        return "".join(ans)
