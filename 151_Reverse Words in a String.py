class Solution:
    def reverseWords(self, s: str) -> str:

        word = ""
        arr = []

        for i in range (len(s)):
            if s[i] != " ":
                word += s[i]
            elif s[i] == " " and word != "":
                arr.append(word)
                word = ""
        if word:
            arr.append(word)

        arr.reverse()

        return " ".join(arr)
