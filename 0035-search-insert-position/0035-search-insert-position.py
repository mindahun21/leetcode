class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)

        if nums[0]>target:
            return 0

        l=0
        r=len(nums) -1
        while l<r:
            if  nums[l]>target:
                return l
            else:
                l+=1
            
            if nums[r]<target:
                return r+1
            else:
                r-=1

        if  nums[l]>target:
            return l
        if nums[r]<target:
            return r+1