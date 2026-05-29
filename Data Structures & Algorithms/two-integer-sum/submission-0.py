class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        for idx,i in enumerate(nums):
            if i in nums_dict:
                return [nums_dict[i],idx]
            else:
                nums_dict[target - i] = idx


        