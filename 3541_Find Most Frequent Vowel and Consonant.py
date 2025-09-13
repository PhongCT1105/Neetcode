class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowel = set(['a', 'e', 'i', 'o', 'u'])
        d_vowel = {}
        d_con = {}

        for c in s:
            if c in vowel:
                d_vowel[c] = d_vowel.get(c, 0) + 1
            else:
                d_con[c] = d_con.get(c, 0) + 1
        res = 0
        if d_vowel.values():
            res += max(list(d_vowel.values()))
        
        if d_con.values():
            res += max(list(d_con.values()))

     
        return res
