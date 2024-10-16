class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack =  []

        for a in asteroids:
            isCollide = False
            while stack and stack[-1]>0 and a<0:
                top = stack.pop()
                if abs(top) == abs(a):
                    isCollide = True
                    break
                elif abs(top) > abs(a):
                    isCollide = True
                    stack.append(top)
                    break

            if not isCollide:
                stack.append(a)

        return stack