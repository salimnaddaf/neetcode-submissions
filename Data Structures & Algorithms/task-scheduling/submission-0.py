class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap = []
        tasksMap = {}
        for task in tasks:
            tasksMap[task] = tasksMap.get(task,0)+1
        for task,count in tasksMap.items():
            heapq.heappush(heap,(-count,task))
        counter = 0
        tempHeap = []
        while heap or tempHeap:
            cycle = 0
            while heap and cycle < n + 1: 
                count,task = heapq.heappop(heap)
                count = -count
                counter += 1
                cycle += 1
                count -= 1
                if count > 0:
                    heapq.heappush(tempHeap, (-count,task))
            while tempHeap:
                heapq.heappush(heap,heapq.heappop(tempHeap))
            if cycle < (n + 1) and heap:
                counter += n - cycle +1
        return counter

