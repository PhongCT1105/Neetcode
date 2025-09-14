class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1], [1,1]]
        if numRows == 1:
            return [res[0]]
        if numRows == 2:
            return res

        for i in range(2, numRows):
            a = res[-1]
            b = [1]
            for j in range (len(a) - 1):
                b.append(a[j] + a[j + 1])

            b.append(1)
            res.append(b)

        return res
