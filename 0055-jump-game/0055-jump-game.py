class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        index = 0
        for i in range(n):
            if i + nums[i] > index:
                index = i +nums[i]
            
            if index < i+1 and i<n-1:
                return False
            elif index >= n-1:
                return True
        
        if index >= 

