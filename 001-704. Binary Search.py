class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def bi_se(nums, target, tmp_l):
        
            if nums[len(nums)//2] == target:
                return len(nums)//2 + tmp_l
            elif len(nums) == 1:
                return -1
            elif nums[len(nums)//2] > target:
                return bi_se(nums[:len(nums)//2], target, tmp_l)
            else:
                return bi_se(nums[len(nums)//2:], target, tmp_l+len(nums)//2)
        return bi_se(nums, target, 0)
