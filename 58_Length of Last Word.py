class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        arr = s.split(" ")
        ptr = len(arr) - 1 
        while ptr >= 0:
            if arr[ptr]:
                return len(arr[ptr])
            ptr -= 1
