class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        r=0
        
        while r < len(flowerbed):
            if flowerbed[r] == 0:
                left = (r==0 or flowerbed[r-1] == 0)
                right = (r==len(flowerbed) or flowerbed[r+1] ==0)

                if left and right:
                    flowerbed[r] =1
                    n-=1
                
            r+=1
            
            if n<=0:
                return True
        
        return False
                


