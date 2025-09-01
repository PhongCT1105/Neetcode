class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel = ["a", "e", "i", "o", "u"]
        s = list(s)
        reverse_vowel = []
        for i in s:
            if i.lower() in vowel:
                reverse_vowel.append(i)

        for i in range (len(s)):
            if s[i].lower() in vowel:
                s[i] = reverse_vowel.pop()

        return "".join(s)
        
