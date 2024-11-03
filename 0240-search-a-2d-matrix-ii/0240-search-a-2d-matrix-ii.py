class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = len(matrix), len(matrix[0])
        if target < matrix[0][0] or target > matrix[row-1][col-1]:
            return False
        m, n = row-1, 0
        while m >=0 and n <=col-1:
            if matrix[m][n] == target:
                return True
            elif  matrix[m][n] > target:
                m-=1
            else:
                n+=1