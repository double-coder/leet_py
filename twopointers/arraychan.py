def sortedSquares(self, nums: list[int]) -> list[int]:
        l, r = 0, len(nums) - 1
        res = []
        while l <= r:
            if nums[l]*nums[l] > nums[r]*nums[r]:
                res.append(nums[l]*nums[l])
                l = l + 1
            else:
                res.append(nums[r]*nums[r])
                r = r - 1
        print(res)
        return sorted(res)