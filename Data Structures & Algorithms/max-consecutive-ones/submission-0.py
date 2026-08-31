class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_counts = []
        max_count = 0
        for num in nums:
            if num == 1:
                max_count += 1
            else:
                max_counts.append(max_count)
                max_count = 0
        
        if max_count > 0:
            max_counts.append(max_count)

        return max(max_counts)
        