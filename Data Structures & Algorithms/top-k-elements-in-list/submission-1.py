class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_dict = {}
        for i in nums:
            if i in nums_dict:
                nums_dict[i]+= 1
            else:
                nums_dict[i] = 1
        return sorted(nums_dict, key=nums_dict.get , reverse=True)[:k]
        