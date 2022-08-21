class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        flag_i = 0
        flag_j = 0
        while flag_i < len(nums):
            if nums[flag_i] == val:
                flag_i += 1
                continue
            if flag_i != flag_j:
                nums[flag_j] = nums[flag_i]
            flag_i += 1
            flag_j += 1
        return flag_j 
