class KthLargest:
    heap = []
    k = 0
    def __init__(self, k: int, nums: List[int]):
        self.k=k
        for num in nums:
            heapq.heappush(self.heap,num)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap,val)
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return heapq.heappop(self.heap)

