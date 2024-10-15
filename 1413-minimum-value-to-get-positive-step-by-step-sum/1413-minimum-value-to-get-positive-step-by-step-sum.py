class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        ans = 1
        s = 1

        for n in nums:
            s= s + n
            if s <1:
                diff = 1 -s
                s += diff
                ans +=diff

        return ans