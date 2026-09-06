class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for point in points:
            heapq.heappush(heap,(-((point[0] * point[0]) + (point[1] * point[1])) ,point))
            if len(heap) > k:
                heapq.heappop(heap)
        res = []
        for point in heap:
            res.append(point[1])
        return res