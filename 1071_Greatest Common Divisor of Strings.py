class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        if len(str1) > len(str2):
            str1, str2 = str2, str1 

        len1, len2 = len(str1), len(str2)

        for i in range (len(str1), 0, -1):
            divisor = str1[:i]

            if (len(str2) % len(divisor) == 0) and (len(str1) % len(divisor) == 0):
                if (divisor * (len(str2) // len(divisor)) == str2) and (divisor * (len(str1) // len(divisor)) == str1):
                    return divisor

        return ""
