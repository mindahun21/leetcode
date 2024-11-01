class Solution:
    def minOperations(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)-2):
            if nums[i] ==0:
                res +=1
                for j in range(3):
                    nums[i+j] = (nums[i+j] + 1) % 2
        
        return -1 if 0 in nums else res
