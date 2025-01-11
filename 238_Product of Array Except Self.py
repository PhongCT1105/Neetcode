# Prefix and condition 
class Solution1(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        mul = 1
        mul_0 = 1
        cnt_0 = 0
        
        for i in nums:
            mul *= i
            if i != 0:
                mul_0 *= i
            else:
                cnt_0 += 1

        res = []

        if cnt_0 > 1:
            res = [0 for _ in range (len(nums))]
            return res

        for i in nums:
            if i != 0:
                res.append(mul / i)
            else:
                res.append(mul_0)
        
        return res

# Prefix and suffix
# class Solution(object):
#     def productExceptSelf(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[int]
#         """
        
#         res =  [1] * len(nums) 
#         prefix = 1

#         for i in range (len(nums)):
#             res[i] *= prefix
#             prefix *= nums[i]

#         suffix = 1
#         for i in range (len(nums) - 1, 0, -1):
#             res[i] *= suffix
#             suffix *= nums[i]

#         res[0] = res[0] * suffix

#         return res                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        

