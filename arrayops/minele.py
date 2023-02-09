class Solution:
    def minElements(self, nums: list[int], limit: int, goal: int) -> int:
        s = sum(nums)
        c = 0
        while s != goal:
            if goal < 0:
                s = s - abs(limit//s)
            else:
                s = s + limit//s
            c += 1

        return c