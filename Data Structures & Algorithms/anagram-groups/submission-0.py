class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = {}
        for i in strs:
            sorted_i = str(sorted(i))
            if sorted_i in anagram_dict:
                anagram_dict[sorted_i]+= [i]
            else:
                anagram_dict[sorted_i] = [i]
        return anagram_dict.values()
        