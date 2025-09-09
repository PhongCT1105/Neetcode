class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        total = []

        def dfs(i, total, num):
            # Break case:
            if sum(total) > n:
                return
            if num == k:
                if sum(total) == n:
                    res.append(total[:] )
                return

            if i > 9:
                return

            total.append(i)
            dfs(i + 1, total, num + 1)
            total.pop()
            dfs(i + 1, total, num)
            

        dfs(1, [], 0)

        return res
