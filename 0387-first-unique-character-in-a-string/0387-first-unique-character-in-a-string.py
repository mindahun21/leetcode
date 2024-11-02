class Solution:
    def firstUniqChar(self, s: str) -> int:
        dq = deque()

        for i in range(len(s)):
            if s[i] not in s[:i]:
                dq.append(i)
            else:
                # remove all s[i] from dq if it is there
                dq =  deque([j for j in dq if s[j] != s[i]])
                
        return dq.popleft() if dq else -1