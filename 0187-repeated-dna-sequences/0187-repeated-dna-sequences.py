class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        counter = defaultdict(int)
        res = []
        l=0
        for r in range(10,len(s)+1):
            counter[s[l:r]]=1+counter.get(s[l:r],0)
            print(l)
            l+=1

        for key, value in counter.items():
            if value >1:
                res.append(key)

        return res