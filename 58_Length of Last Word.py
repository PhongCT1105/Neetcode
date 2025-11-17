class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        word = []
        arr = []

        for c in s:
            if c == " ":
                if word:
                    arr.append(word)
                    word = []
                else:
                    continue
            else:
                word.append(c)

        if word:
            arr.append(word)

        return len(arr[-1])
