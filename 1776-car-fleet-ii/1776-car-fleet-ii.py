class Solution:
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        res = [-1] *len(cars)
        stack = []
        for i in range(len(cars)-1, -1,-1):
            while stack and cars[i][1] <= cars[stack[-1]][1]:
                stack.pop()

            while stack:
                coltime = (cars[stack[-1]][0] - cars[i][0])/ (cars[i][1]-cars[stack[-1]][1])

                if ( coltime <= res[stack[-1]] or res[stack[-1]] == -1):
                    res[i] = coltime
                    break
                
                stack.pop()
            
            stack.append(i)

        return res