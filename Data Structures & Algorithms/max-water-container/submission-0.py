class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0
        l, r = 0, len(heights) - 1

        max_area = 0
        while l < r:
            area = (r - l) * min(heights[l], heights[r])
            if area > max_area:
                max_area = area

            if heights[l] < heights[r]:
                l += 1
            elif heights[r] < heights[l]:
                r -= 1    
            elif heights[l] == heights[r]:
                l += 1  

        return max_area
