class Solution:
    def swap(self, arr, a, b):
        arr[a], arr[b] = arr[b], arr[a]

    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0 # where to slot in a non val number
        for num in nums:
            if num != val:
                nums[k] = num
                k += 1

        return k
            

        
