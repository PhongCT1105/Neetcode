class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        dict1, dict2 = {}, {}

        if set(word1) != set(word2):
            return False
            
        for i in word1:
            if i in dict1:
                dict1[i] += 1
            else:
                dict1[i] = 1

        for i in word2:
            if i in dict2:
                dict2[i] += 1
            else:
                dict2[i] = 1

        dict1 = list(dict1.values())
        dict2 = list(dict2.values())
    
        dict1.sort()
        dict2.sort()

        return dict1 == dict2
