class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_with_index = []
        for i, num in enumerate(nums):
            nums_with_index.append((num, i))

        nums_with_index.sort()
        s,e= 0, len(nums_with_index)-1
        while s<e:
            if nums_with_index[s][0] + nums_with_index[e][0] == target:
                return [nums_with_index[s][1],nums_with_index[e][1]]
            if nums_with_index[s][0] + nums_with_index[e][0] > target:
                e-=1
            else:
                s+=1
            
        return []