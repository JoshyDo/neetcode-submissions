from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        
        # 1. Schritt: Einsortieren (Cyclic Sort)
        for i in range(n):
            while 0 < nums[i] <= n:
                wunsch_index = nums[i] - 1
                
                if nums[i] == nums[wunsch_index]:
                    break
                
                nums[i], nums[wunsch_index] = nums[wunsch_index], nums[i]
        
        # 2. Schritt: Lücke suchen
        for j in range(n):
            if nums[j] != j + 1:
                return j + 1
                
        # Wenn alle Zahlen von 1 bis n perfekt da sind
        return n + 1