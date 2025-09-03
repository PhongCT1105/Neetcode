class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        dict_row = {}

        for i in range (len(grid)):
            string = ""
            for j in range (len(grid)):
                string += ","
                string += str(grid[i][j])

            if string in dict_row:
                dict_row[string] += 1
            else:
                dict_row[string] = 1

        res = 0

        for i in range (len(grid)):
            string = ""
            for j in range (len(grid)):
                string += ","
                string += str(grid[j][i])

            if string in dict_row:
                res += dict_row[string]
                
        return res 
