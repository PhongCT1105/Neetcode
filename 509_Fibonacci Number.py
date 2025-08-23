class Solution:
    def fib(self, n: int) -> int:

        # Recursion solution
        # if n == 1:
        #     return 1
        # if n == 0:
        #     return 0

        # return self.fib(n-1) + self.fib(n-2)

        # Memoization
        def memoization(n, cache):
            if n <= 1:
                return n
            
            if n in cache:
                return cache[n]

            cache[n] = memoization(n-1, cache) + memoization(n-2, cache)
            return cache[n]

        ans = memoization(n, {})
        return ans
