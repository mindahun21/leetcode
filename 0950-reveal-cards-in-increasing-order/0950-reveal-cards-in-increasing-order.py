class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        dq = deque([i for i in range(len(deck))])
        res = [0] * len(deck)
        for n in deck:
            index=dq.popleft()
            res[index] = n
            if dq:
                dq.append(dq.popleft())
        
        return res