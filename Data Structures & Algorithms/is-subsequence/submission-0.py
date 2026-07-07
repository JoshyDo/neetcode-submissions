class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        it = iter(t)
        
        for char in s:
            if char not in it:
                return False  
                
        return True 