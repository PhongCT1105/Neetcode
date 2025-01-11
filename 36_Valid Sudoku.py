class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        row_set = defaultdict(set)
        col_set = defaultdict(set)
        sqr_set = defaultdict(set)

            valid = [str(i + 1) for i in range (9)]

        for row in range (9):
            for col in range (9):
                if board[row][col] == ".":
                    continue

                if board[row][col] in valid:
                    if (board[row][col] in row_set[row]) or (board[row][col] in col_set[col]) or (board[row][col] in sqr_set[(row // 3, col // 3)]):
                        return False

                    row_set[row].add(board[row][col])
                    col_set[col].add(board[row][col])
                    sqr_set[(row // 3, col // 3)].add(board[row][col])

                else:
                    return False

        print(valid)

        return True
