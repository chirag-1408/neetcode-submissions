class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        str_list = []
        for i in s:
            if i in str_list:
                str_list = str_list[str_list.index(i)+1:]
                print(str_list)
            str_list.append(i)
            maxLength = max(maxLength, len(str_list))
        return maxLength

        