class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        left, right = nums[0], nums[0]
        
        while True:
            left = nums[left]
            right = nums[nums[right]]

            if left == right:
                break

        left = nums[0]
        while left != right:
            left = nums[left]
            right = nums[right]
                            
        return left
