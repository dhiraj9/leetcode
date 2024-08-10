class Solution:
  def isValidSudoku(self, board: List[List[str]]) -> bool:
    for i in board:
      a = set()
      for j in i:
        if j in a:
          return False
        if j != ".":
          a.add(j)
      for i in range(len(board)):
        a = set()
        for j in range(9):
          if board[j][i] in a:
            return False
          if board[j][i] != ".":
            a.add(board[j][i])
      a = set()
      for i in range(3):
        for j in range(3):
          if board[i][j] in a:
            return False
          if board[i][j] != ".":
            a.add(board[i][j])
      a = set()
      for i in range(3):
        for j in range(3, 6):
          if board[i][j] in a:
            return False
          if board[i][j] != ".":
            a.add(board[i][j])  
      a = set()
      for i in range(3):
        for j in range(6, 9):
          if board[i][j] in a:
            return False
          if board[i][j] != ".":
            a.add(board[i][j])   
      a = set()
      for i in range(3, 6):
        for j in range(3):
          if board[i][j] in a:
            return False
          if board[i][j] != ".":
            a.add(board[i][j])
      a = set()
      for i in range(3, 6):
        for j in range(3, 6):
          if board[i][j] in a:
            return False
          if board[i][j] != ".":
            a.add(board[i][j])  
      a = set()
      for i in range(3, 6):
        for j in range(6, 9):
          if board[i][j] in a:
            return False
          if board[i][j] != ".":
            a.add(board[i][j])   
      a = set()
      for i in range(6, 9):
        for j in range(3):
          if board[i][j] in a:
            return False
          if board[i][j] != ".":
            a.add(board[i][j])
      a = set()
      for i in range(6, 9):
        for j in range(3, 6):
          if board[i][j] in a:
            return False
          if board[i][j] != ".":
            a.add(board[i][j])  
      a = set()
      for i in range(6, 9):
        for j in range(6, 9):
          if board[i][j] in a:
            return False
          if board[i][j] != ".":
            a.add(board[i][j])         
    return True




