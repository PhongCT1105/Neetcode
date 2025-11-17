class Solution:
    def cal_distance(self, point):
        x, y = point[0], point[1]
        import math
        distance = math.sqrt(x**2 + y**2)
        return (distance, point)
    
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        import heapq
        heap = []
        for point in points:
            heapq.heappush(heap, self.cal_distance(point))
        ans = []

        for _ in range(k):
            point = heapq.heappop(heap)
            ans.append(point[1])

        return ans
