class MedianFinder:

    def __init__(self):
        self.small = [] # max heap
        self.large = [] # min heap

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -num)
        # numbers in self.small always <= numbers in self.large
        if self.small and self.large:
            if (-self.small[0] > self.large[0]):
                val = -heapq.heappop(self.small)
                heapq.heappush(self.large, val)

        # balance the two heap
        if abs(len(self.small) - len(self.large)) > 1:
            if len(self.small) > len(self.large):
                val = -heapq.heappop(self.small)
                heapq.heappush(self.large, val)
            else:
                val = -heapq.heappop(self.large)
                heapq.heappush(self.small, val)

    def findMedian(self) -> float:
        if len(self.small) == len(self.large):
            return (-self.small[0] + self.large[0]) / 2
        elif len(self.small) > len(self.large):
            return -self.small[0]
        else:
            return self.large[0]
