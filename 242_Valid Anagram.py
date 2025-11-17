class Solution:

    def get_char_map(self, s: str) -> []:
        char_map = [0] * 26
        for c in s:
            char_map[ord(c)-ord('a')] += 1
        
        return char_map


    def isAnagram(self, s: str, t: str) -> bool:

        char_map_s = self.get_char_map(s)
        char_map_t = self.get_char_map(t)

        return char_map_s == char_map_t
