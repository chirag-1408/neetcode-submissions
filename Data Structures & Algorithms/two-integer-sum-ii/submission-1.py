class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Since Hashmap does not utilize the sorted property , using a two-pointer approach
        l ,r = 0, len(numbers) -1
        while l < r:
            currSum = numbers[l] + numbers[r]
            if currSum > target:
                r -=1
            elif currSum < target:
                l +=1
            else:
                return [l+1 , r+1]
        