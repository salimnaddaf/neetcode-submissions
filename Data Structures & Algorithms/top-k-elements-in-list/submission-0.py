import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap={}
        for num in nums:
            freqMap[num]=freqMap.get(num,0)+1
        heap=[]
        for num , freq in freqMap.items():
            heapq.heappush(heap,(freq,num))
            if len(heap)>k:
                heapq.heappop(heap)
        res=[]
        for freq,num in heap:
            res.append(num)
        return res

