class Solution:
    def tribonacci(self, n: int) -> int:
        prev = [0, 1, 1]
        if n == 0:
            return 0
        elif n < 3:
            return 1

        for _ in range(2, n):
            prev[0], prev[1], prev[2] = prev[1], prev[2], sum(prev)
            

        return prev[-1]
