class Solution:
    def reverseWords(self, s: str) -> str:
        s.strip()
        return " ".join(reversed([w.strip() for w in s.split(" ") if not w.strip() == "" ]))