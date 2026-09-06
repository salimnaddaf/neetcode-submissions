class KthLargest:
    heap = []
    def __init__(self, k: int, nums: List[int]):
        for num in nums:
            heapq.heappush(self.heap,num)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap,num)
        while len(self.heap) >= k:
            heapq.heappop(self.heap)
