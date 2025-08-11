import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Max heap
        stones = [-s for s in stones]

        heapq.heapify(stones)

        while len(stones) >= 2:
            Y = heapq.heappop(stones)
            X = heapq.heappop(stones)

            if X != Y:
                heapq.heappush(stones, Y - X)
        if stones:    
            return -stones[0]
        
        return 0
