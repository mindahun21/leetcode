class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        res = ""

        for s in path.split("/"):
            if s== "" or s== ".":
                continue
            
            if s == "..":
                if stack:
                    stack.pop()

                continue
            
            stack.append(s)
        
        return "/" + "/".join(stack)