import re

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        cleaned_s = re.sub("[^a-zA-Z0-9]", "", s)
        cleaned_s = cleaned_s.lower()
        l = 0
        r = len(cleaned_s) - 1
        while l <= r:
            if cleaned_s[l] != cleaned_s[r]:
                return False
            else:
                l += 1
                r -= 1

        return True
