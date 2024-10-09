class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l=0
        r=len(height)-1
        area = 0
        max_height = max(height)
        while l<r:
            curent_area=min(height[l],height[r])*(r-l)
            area = max(curent_area, area)
            if height[l]<height[r]:
                l+=1
            else:
                r-=1

            if area >= max_height * (r-l):
                break
            
        return area