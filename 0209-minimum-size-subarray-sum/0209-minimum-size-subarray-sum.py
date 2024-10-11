class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float('inf')
        l= 0
        s = 0
        for r in range(len(nums)):
            s+=nums[r]
            while s>=target:
                res = min(res, r-l+1)
                s= s-nums[l]
                l+=1
            
        return res if res != float('inf') else 0