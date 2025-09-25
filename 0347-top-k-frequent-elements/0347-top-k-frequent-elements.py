class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(int)

        for num in nums:
            counter[num]+=1

        result = sorted(counter.items(), key=lambda item: item[1], reverse=True) 
        return [item[0] for item in result][0:k]
