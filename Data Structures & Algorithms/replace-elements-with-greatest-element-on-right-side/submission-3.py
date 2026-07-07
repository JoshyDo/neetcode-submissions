class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        i = len(arr) - 1
        current_max = -1
        
        while i >= 0: 
            temp = arr[i]
            arr[i] = current_max
            current_max = max(current_max, temp)
            i -= 1

        return arr