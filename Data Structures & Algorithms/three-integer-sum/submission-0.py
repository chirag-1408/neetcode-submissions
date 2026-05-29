class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)
        i = 0
        while i < n:
            if nums[i] > 0: break
            l = i+ 1 
            r = n- 1
            while l < r:
                sum3 = nums[i]+nums[l]+nums[r]
                if sum3 == 0:
                    res.append([nums[i],nums[l],nums[r]])
                    while l+ 1 < n and nums[l+ 1] == nums[l]: # Check if the next element after the middle index is a duplicate
                        l += 1 # Skip the duplicate  
                    l += 1
                    r -= 1
                elif sum3 < 0: # Because the list is sorted , if sum is <0 then the lower index number is responsible
                    l += 1
                else:
                    r -= 1
            while i+ 1 <n and nums[i+ 1] == nums[i]: # Check if the nexy element after the starting index is a duplicate
                i += 1 # Skip the duplicate
            i += 1
        return res
        