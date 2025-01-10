class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        count = {}

        if len(s) != len(t):
            return False

        for i in range (len (s)):
            if s[i] not in count:
                count[s[i]] = 1
            else:
                count[s[i]] += 1
            
            if t[i] not in count:
                count[t[i]] = -1
            else:
                count[t[i]] -= 1

        for i in count.values():
            if i != 0:
                return False
        return True
