class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dict_arr = {}

        for i in arr:
            if i in dict_arr:
                dict_arr[i] += 1
            else:
                dict_arr[i] = 1

        occurence = list(dict_arr.values())

        return len(occurence) == len(list(set(occurence)))
