class Solution:
    def minOperations(self, nums: List[int]) -> int:
        res = 0
        dq = deque([i for i, x in enumerate(nums) if x == 0])
        
        while dq:
            i = dq.popleft()

            if i > len(nums) -3 or nums[i] !=0:
                continue
            
            for j in range(3):
                nums[i+j] = (nums[i+j] + 1) % 2

                if nums[i+j] ==0:
                    dq.append(i+j)
            
            res+=1
        
        return -1 if 0 in nums else res
