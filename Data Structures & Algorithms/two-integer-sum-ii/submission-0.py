class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        num_dict= {}
        for idx, num in enumerate(numbers):
            if num in num_dict:
                return [num_dict[num], idx+1]
            else:
                num_dict[target - num] = idx+1
        