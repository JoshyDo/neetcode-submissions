class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        i = len(arr) - 1# e.g. 10
        current_max = -1
        while i >= 0: # 10 > 0
            temp = arr[i]
            arr[i] = current_max
            current_max = max(current_max, temp)
            i -= 1

        arr[-1] = -1 # letztes Element -1
        return arr