class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return self.validateBoxes(board) and self.validateRows(board) and self.validateColumns(board)

    def validateBoxes(self, board: List[List[str]]) -> bool:

        for i in range(0,len(board),3):
            for j in range(0,len(board[i]),3):
                if not self.validateBox(board,i,j):
                    return False
        return True
            
    def validateBox(self,board: List[List[str]], row:int , col:int) -> bool:
        numbers = set()
        for i in range(row,row+3):
            for j in range(col,col+3):
                if board[i][j]!='.' and board[i][j] in numbers:
                    return False
                numbers.add(board[i][j])
        return True

    def validateRows(self, board: List[List[str]]) -> bool:
        for row in board:
            numbers=set()
            for num in row:
                if num!='.' and num in numbers:
                    return False
                numbers.add(num)
        return True



    def validateColumns(self, board: List[List[str]]) -> bool:

        for j in range(len(board)):
            numbers=set()
            for i in range(len(board)):
                if board[i][j]!='.' and board[i][j] in numbers:
                    return False
                numbers.add(board[i][j])
        return True




