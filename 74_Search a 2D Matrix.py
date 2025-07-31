class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        if not matrix:
            return False

        n_row, n_col = len(matrix), len(matrix[0])
        l, r = 0, n_row * n_col - 1

        while l <= r:
            m = (l + r) // 2
            row, col = m // n_col, m % n_col
            print("Row: ", row, "Col: ",  col)

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                r = m - 1
            elif matrix[row][col] < target:
                l = m + 1

        return False
