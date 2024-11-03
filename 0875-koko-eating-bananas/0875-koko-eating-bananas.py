class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        res = float("inf")
        while left<=right:
            mid = (left+right)//2
            temp_h = 0
            for p in piles:
                temp_h += math.ceil(p/mid)
            if temp_h <= h:
                res = mid  # Update the result with the current mid
                right = mid - 1  # Try to find a smaller valid speed
            else:
                left = mid + 1  # Increase the speed since temp_h > h

        return res