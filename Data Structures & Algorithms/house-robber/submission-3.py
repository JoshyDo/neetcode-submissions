class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = set()

        def backtrack(n, score):
            if n >= len(nums): return score
            score += nums[n]
            if (n, score) in memo: return score
            memo.add((n, score))
            return max(backtrack(n+2, score), backtrack(n+3, score))
        
        return max(backtrack(0,0), backtrack(1,0))