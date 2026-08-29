class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return self.validateBoxes(board) and self.validateRows(board) and self.validateColumns(board)

    def validateBoxes(self, board: List[List[str]]) -> bool:
        i=0
        j=0
        while i<len(board):
            while j<len(board[i]):
                if not self.validateBox(board,i,j):
                    return False
                j+=3
            i+=3
            j=0
        return True
            
    def validateBox(self,board: List[List[str]], row:int , col:int) -> bool:
        numbers = set()
        i=row
        j=col
        while i<row+3:
            while j<col+3:
                if board[i][j]!='.' and board[i][j] in numbers:
                    return False
                numbers.add(board[i][j])
                j+=1
            i+=1
            j=col
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
            for i in range(len(board[j])):
                if board[i][j]!='.' and board[i][j] in numbers:
                    return False
                numbers.add(board[i][j])
        return True




