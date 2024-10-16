class NumArray:

    def __init__(self, nums: List[int]):
        self.NumArray = []
        self.NumArray.append(nums[0])
        for i in range(1,len(nums)):
            self.NumArray.append(self.NumArray[i-1]+nums[i])



    def sumRange(self, left: int, right: int) -> int:
        if left == 0 :
            return self.NumArray[right]
        return self.NumArray[right] - self.NumArray[left-1] 

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)