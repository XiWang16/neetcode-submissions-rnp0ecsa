class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # copy of row/col/3x3 grid, see if item alr in
        for row in board:
            tmp = []
            for item in row:
                if item in tmp: return False
                if item != ".": 
                    tmp.append(item)
        for i in range(len(board)):
            tmp = []
            for j in range(len(board)):
                if board[j][i] in tmp: return False
                if board[j][i] != ".": 
                    tmp.append(board[j][i])
        # check 3 x 3 area
        for row_start_idx in [0, 3, 6]:
            for col_start_idx in [0, 3, 6]:
                tmp = []
                for i in range(row_start_idx, row_start_idx + 3):
                    for j in range(col_start_idx, col_start_idx + 3):
                        if board[i][j] in tmp: return False
                        if board[i][j] != ".": 
                            tmp.append(board[i][j])
        return True