class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if not digits:
            return []
            
        digit_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        res = []

        def backtrack(i: int, c: List[str]):
            if i == len(digits):
                res.append("".join(c[:]))
                return
            
            char_map = digit_map[digits[i]]

            for j in char_map:
                c.append(j)
                backtrack(i + 1, c)        
                c.pop()

        backtrack(0, [])

        return res

