class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        group = {}

        for word in strs:
            count = [0] * 26
            for letter in word:
                count[ord(letter) - ord('a')] += 1
            count_tuple = tuple(count)
            if count_tuple in group:
                group[count_tuple].append(word)
            else:
                group[count_tuple] = [word]

        return list(group.values())
