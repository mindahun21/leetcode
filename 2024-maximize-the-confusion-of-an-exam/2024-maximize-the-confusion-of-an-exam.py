class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        counter = defaultdict(int)

        l=0
        res =0
        for r in range(len(answerKey)):
            counter[answerKey[r]] = 1+ counter.get(answerKey[r],0)

            while (r-l+1) - max(counter.values())>k:
                counter[answerKey[l]]-=1
                l+=1

            res=max(res, r-l+1)
        return res