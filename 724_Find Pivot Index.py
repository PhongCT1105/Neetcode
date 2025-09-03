class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        suffix = []
        pre_tot, sum_tot = 0, 0

        for i in range(len(nums) - 1, -1, -1):
            sum_tot += nums[i]
            suffix.append(sum_tot)
        

        for i in range(len(nums)):
            pre_tot += nums[i]
            print(pre_tot)
            if pre_tot == suffix[len(nums) - i - 1]:
                return i

        return -1
            
