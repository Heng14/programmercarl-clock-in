class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        head = 0
        tail = len(nums) - 1
        res = []
        while head != tail:
            if abs(nums[head]) > abs(nums[tail]):
                res.insert(0, nums[head]**2)
                head += 1
            else:
                res.insert(0, nums[tail]**2)
                tail -= 1
        res.insert(0, nums[tail]**2)
        return res
