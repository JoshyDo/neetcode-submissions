class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        all_products = 1
        zero_count = 0

        for x in nums:
            if x == 0:
                zero_count += 1
            else:
                all_products *= x

        for x in nums:
            if zero_count > 1:
                res.append(0)
            elif zero_count == 1:
                if x == 0:
                    res.append(all_products)
                else:
                    res.append(0)
            else:
                res.append(all_products // x)

        return res