class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = len(matrix), len(matrix[0])

        top, bottom = 0, row-1
        

        while top <= bottom:
            mid = (top + bottom)//2

            if matrix[mid][0] <= target and matrix[mid][col] >=target:

            
            if matrix[mid][0] == target :
                return True
            elif matrix[mid][col-1] > target:
                bottom = mid-1
            else:
                top = mid+1