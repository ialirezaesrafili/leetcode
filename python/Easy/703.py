import heapq


class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.min_heap = []

        # Initialize the heap with the first k elements from nums
        for num in nums:
            self.add(num)  # Utilize the add function to maintain the heap property

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        heapq.heappush(self.min_heap, val)

        # If heap size exceeds k, remove the smallest element
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)

        # The root of the heap is the kth largest element
        return self.min_heap[0]
