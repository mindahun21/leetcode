class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l1 = 0
        l2 = 0
        comb = []
        while l1 < len(nums1) and l2 < len(nums2):
            if nums1[l1] < nums2[l2]:
                comb.append(nums1[l1])
                l1+=1
            else:
                comb.append(nums2[l2])
                l2+=1
        
        while l1 < len(nums1):
            comb.append(nums1[l1])
            l1+=1
        
        while l2 < len(nums2):
            comb.append(nums2[l2])
            l2+=1
        
        n = len(comb)
        print(comb)
        
        if n % 2 ==0:
            i = int(n/2)-1
            return (comb[i] + comb[i+1])/2
        else:
            i = int(n/2)
            return comb[i]

