class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result = [-1, -1]
        l=0
        r=len(nums) -1
        while l<=r and -1 in result:
            if nums[l] == target:
                result[0] = l
            else:
                l+=1
            if nums[r] == target:
                result[1] = r
            else:
                r-=1

        return result