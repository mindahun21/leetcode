class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = None
        dif = float('inf')
        for i in range(len(nums)-2):
            j = i+1
            k=len(nums)-1

            while j<k:
                t = nums[i]+nums[j]+nums[k]
                if abs(t- target) < dif:
                    dif = abs(t- target)
                    ans = t
                
                if t<target:
                    j+=1
                elif t>target:
                    k-=1
                else:
                    return t

        return ans