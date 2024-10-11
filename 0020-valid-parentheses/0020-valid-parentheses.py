class Solution:
    def isValid(self, s: str) -> bool:
        opening = "([{"
        closing = ")]}"
        bracket_map = {")":"(","]":"[","}":"{"}
        stack = []

        if s[0] not in opening:
            return False
        
        for p in s:
            if p in opening:
                stack.append(p)
            elif p in closing:
                if len(stack) == 0:
                    return False
                
                poped = stack.pop()
                if bracket_map[p] != poped:
                    return False
        
        return True if len(stack) == 0 else False