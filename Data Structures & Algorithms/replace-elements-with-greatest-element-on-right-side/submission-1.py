class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        current_max = arr[-1]

        for i in range(len(arr) - 2, -1, -1):
            tmp = arr[i]
            arr[i] = current_max

            current_max = max(tmp, current_max)

        arr[-1] = -1

        return arr
        