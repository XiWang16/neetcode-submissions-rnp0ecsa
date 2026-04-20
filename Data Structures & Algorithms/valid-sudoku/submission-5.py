from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(list)
        cols = defaultdict(list)
        squares = defaultdict(list)
        for i in range(len(board)):
            for j in range(len(board)):
                item = board[i][j]
                if item != '.' and (item in rows[i] or item in cols[j] or item in squares[(i//3, j//3)]):
                    return False
                else: 
                    rows[i].append(item)
                    cols[j].append(item)
                    squares[(i//3, j//3)].append(item)
            print(f'Row is {rows}')
            print(f'Columns is {cols}')
            print(f'Squares is {squares}')
        return True