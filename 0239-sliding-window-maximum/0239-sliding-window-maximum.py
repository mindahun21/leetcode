class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        deq = deque()  
        for i in range(len(nums)):
            if deq and deq[0] < i - k + 1:
                deq.popleft()
            
            while deq and nums[deq[-1]] < nums[i]:
                deq.pop()
            
            deq.append(i)
            
            if i >= k - 1:
                res.append(nums[deq[0]]) 
        
        return res