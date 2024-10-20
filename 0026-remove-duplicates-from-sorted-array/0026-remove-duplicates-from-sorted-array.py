class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        k=  1
        unique_index = 0
        for  i in range(1, len(nums)):
            if nums[i] != nums[unique_index]:
                unique_index = i
                k+=1
            else:
                nums[i] = float('inf')
        
        nums.sort()
        for i in range(k, len(nums)):
            if nums[i] == float('inf'):
                nums[i] = "_"
        
        return k

