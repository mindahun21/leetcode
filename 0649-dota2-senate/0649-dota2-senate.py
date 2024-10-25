from queue import Queue

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        qr = Queue(0)
        qd = Queue(0)
        for i, l in enumerate(senate):
            if l == "D":
                qd.put(i)
            else:
                qr.put(i)
        
        while not qr.empty() and not qd.empty():
            d=qd.get()
            r= qr.get()
            if d<r:
                qd.put(len(senate) + d)
            else:
                qr.put(len(senate) + r)
        
        if qr.empty():
            return "Dire"
        else:
            return "Radiant"