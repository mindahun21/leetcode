class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        nums.sort()

        for i in range(len(nums)-3):
            if i>0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1, len(nums)-2):
                if j>i+1 and nums[j]== nums[j-1]:
                    continue
                k = j+1
                l=len(nums)-1

                while k<l:
                    t = nums[i]+nums[j]+nums[k]+nums[l]

                    if t>target:
                        l-=1
                    elif t<target:
                        k+=1
                    else:
                        result.append([nums[i],nums[j],nums[k],nums[l]])
                        k+=1

                        while nums[k] == nums[k-1] and k<l:
                            k+=1
    
        return result
                    