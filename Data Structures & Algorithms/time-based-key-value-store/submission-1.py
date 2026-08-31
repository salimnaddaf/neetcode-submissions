class TimeMap:

    def __init__(self):
        self.timemap = {}


    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timemap:
            self.timemap[key]=[]
        self.timemap[key].append([timestamp,value])

    def get(self, key: str, timestamp: int) -> str:
        if key in self.timemap:
            arr = self.timemap[key]
            left = 0
            right = len(arr) -1
            while left <= right:
                mid = (left + right) //2
                if arr[mid][0] == timestamp:
                    return arr[mid][1]
                if arr[mid][0] > timestamp:
                    right = mid -1
                else :
                    left = mid + 1
            if left > 0:
                return arr[left-1][1]
        return ""