from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Ensure nums1 is the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
            
        x, y = len(nums1), len(nums2)
        low, high = 0, x

        while low <= high:
            partitionX = (low + high) // 2  # Partition index for nums1
            partitionY = (x + y + 1) // 2 - partitionX  # Partition index for nums2

            # If partition is at the beginning or end, assign -inf or inf
            maxX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
            minX = float('inf') if partitionX == x else nums1[partitionX]
            
            maxY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
            minY = float('inf') if partitionY == y else nums2[partitionY]

            # Check if we have found the correct partition
            if maxX <= minY and maxY <= minX:
                # We have partitioned the arrays correctly
                if (x + y) % 2 == 0:
                    return (max(maxX, maxY) + min(minX, minY)) / 2
                else:
                    return max(maxX, maxY)
            elif maxX > minY:
                # We are too far on the right side for partitionX. Go on the left side.
                high = partitionX - 1
            else:
                # We are too far on the left side for partitionX. Go on the right side.
                low = partitionX + 1

        raise ValueError("Input arrays are not sorted or are invalid.")
