import heapq
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        maxHeap = []

        for point in points:
            X, Y = point[0], point[1]
            dist = math.sqrt(X**2 + Y**2)

            heapq.heappush(maxHeap, [-dist, X, Y])
            
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)

        res = [[point[1], point[2]] for point in maxHeap]

        return res
