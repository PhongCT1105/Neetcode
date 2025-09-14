class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        prev = [1, 1]
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return prev

        for _ in range(2, rowIndex + 1):
            c = [1]
            for i in range(len(prev) - 1):
                c.append(prev[i] + prev[i + 1])

            c.append(1)
            prev = c

        return prev
