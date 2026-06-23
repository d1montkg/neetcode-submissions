class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        digit = [0] * 10

        for i in range(n):
            for j in range(len(board[i])):
                if board[i][j] != ".":
                    digit[int(board[i][j])] += 1
            if 2 in digit:
                return False
            digit = [0] * 10

        for i in range(n):
            for j in range(n):
                if board[j][i] != ".":
                    digit[int(board[j][i])] += 1
            if 2 in digit:
                return False
            digit = [0] * 10
        
        separate_board = []
        square1, square2, square3 = [], [], []
        for i in range(n):
            square1.append("".join(board[i][ : 3]))
            square2.append("".join(board[i][3 : 6]))
            square3.append("".join(board[i][6 : ]))
            
            if i % 3 == 2:
                square1 = ''.join(square1)
                square2 = ''.join(square2)
                square3 = ''.join(square3)

                for i in range(9):
                    if square1[i] != "." and square1.count(square1[i]) > 1:
                        return False
                    if square2[i] != "." and square2.count(square2[i]) > 1:
                        return False
                    if square3[i] != "." and square3.count(square3[i]) > 1:
                        return False
                    
                square1, square2, square3 = [], [], []
        
        return True
