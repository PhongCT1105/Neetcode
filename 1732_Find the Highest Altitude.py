class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        
        res = 0
        prefixsum = 0

        for i in range (len(gain)):
            prefixsum += gain[i]
            if prefixsum > res:
                res = prefixsum

        return res
