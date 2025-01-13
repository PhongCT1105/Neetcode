class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """

        res = [0] * len(temperatures)
        stack = []

        for i, value in enumerate(temperatures):
            while stack and value > stack[-1][1]:
                res[stack[-1][0]] = i - stack[-1][0]
                stack.pop(-1)

            stack.append((i, value))

        return res
