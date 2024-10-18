class Solution:
    def countOfAtoms(self, formula: str) -> str:
        stack = []
        curIsdigit = False
        curI = ""
        depth = 0
        for c in formula:
            if c.isdigit():
                curI+=c
                curIsdigit = True
                continue
            elif curIsdigit:
                if stack[-1][0] ==')':
                    depth = 1
                    stack.pop()
                    r = 1
                    while (depth >1 or stack[-r][0] != "(") and len(stack)>=r:
                        if depth >1:
                            depth -=1
                            del stack[-r]
                            continue
                        stack[-r][1] = stack[-r][1]*int(curI)
                        r+=1
                    if stack[-r][0] == "(":
                        depth =0
                        del stack[-r]
                    
                else:
                    stack[-1][1] += (int(curI) -1)

                curI = ""
                curIsdigit = False
            
            if c.islower(): 
                stack[-1][0] += c
            else:  
                stack.append([c, 1])
            print(stack)
        
        if curIsdigit:
            if stack[-1][0] ==')':
                depth = 1
                stack.pop()
                r = 1
                while (depth >1 or stack[-r][0] != "(") and len(stack)>=r:
                    if depth >1:
                        depth -=1
                        del stack[-r]
                        continue
                    stack[-r][1] = stack[-r][1]*int(curI)
                    r+=1
                if stack[-r][0] == "(":
                    depth = 0
                    del stack[-r]
                
            else:
                stack[-1][1] += (int(curI) -1)
                
            curI = ""
            curIsdigit = False

        stack = [item for item in stack if item[0] not in ('(',')')]


        res = {}
        for key, val in stack:
            if key in res:
                res[key] += val
            else:
                res[key] = val

        res = dict(sorted(res.items()))
        return  "".join(f"{key}{value}" if value >1 else key for key, value in res.items())
         