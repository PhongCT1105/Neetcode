# O(n) complexity

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        # Create a bucket sort => have boundary of n
        bucket = [[] for _ in range (len(nums) + 1)]
        
        # Count the frequency of all number first by using hash dictionary
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        # Get the frequency into the bucket sort
        for key,value in freq.items():
            bucket[value].append(key)

        res = []

        for i in range (len(bucket) - 1, 0, -1):
            for num in bucket[i]:
                res.append(num)
                if len(res) >= k:
                    return res

        return res

            
# O(n logn) complexity

# class Solution(object):
#     def topKFrequent(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: List[int]
#         """

#         top_k = defaultdict(int)

#         for num in nums:
#             top_k[num] += 1

#         top_k_sort  = sorted(top_k.keys(), key=lambda x: top_k[x], reverse=True)

#         return top_k_sort[:k]        

