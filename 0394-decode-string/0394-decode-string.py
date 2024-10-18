class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curS = ""
        curI = ""
        for c in s:
            if c != "]":
                stack.append(c)
            else:
                while stack[-1] != "[":
                    curS  = stack.pop() + curS
                
                stack.pop()
                while stack and stack[-1].isdigit():
                    curI = stack.pop() + curI

                curS = curS * int(curI)
                stack.append(curS)
                curS =""
                curI = ""

        return "".join(stack)             
