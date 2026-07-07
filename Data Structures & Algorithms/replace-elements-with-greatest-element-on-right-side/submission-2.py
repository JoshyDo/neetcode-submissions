class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        i = len(arr) - 1
        current_max = -1
        
        # Änderung: > wird zu >=, damit Index 0 auch bearbeitet wird
        while i >= 0: 
            temp = arr[i]
            arr[i] = current_max
            current_max = max(current_max, temp)
            i -= 1

        # arr[-1] = -1  <- Kannst du jetzt weglassen, da es in der Schleife passiert
        return arr