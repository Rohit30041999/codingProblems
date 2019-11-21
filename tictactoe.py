'''
GAME NAME: TicTacToe.
Rules:
1) there will be only two letters to choose they are 'x' and 'o'.
2) player1 will be 'x'.
3) player2 will be 'o'.
4) There will be a 3x3 board.
5) Any letter if it is consecutive diagnally or in a total column or in a total row then that letter's player will win.
6) if there is no winner then the game ends if don't want continue.
'''

#CODE:>>>
#This function is basically to empty the board if required.
def emptyBoard() -> list:
  board = [
    ['_','_','_'], 
    ['_','_','_'], 
    ['_','_','_'], 
  ]
  return board

#Checking if there is a winner or if the board is full.
def checkBoard(board) -> str:
  if (board[0][0] == 'x' and board[1][1] == 'x' and board[2][2] == 'x') or (board[0][0] == 'o' and board[1][1] == 'o' and board[2][2] == 'o'):
    return board[0][0]
  elif (board[0][2] == 'x' and board[1][1] == 'x' and board[2][0] == 'x') or (board[0][2] == 'o' and board[1][1] == 'o' and board[2][0] == 'o'):
    return board[0][2]
  elif (board[0][0] == 'x' and board[0][1] == 'x' and board[0][2] == 'x') or (board[0][0] == 'o' and board[0][1] == 'o' and board[0][2] == 'o'):
    return board[0][0]
  elif (board[1][0] == 'x' and board[1][1] == 'x' and board[1][2] == 'x') or (board[1][0] == 'o' and board[1][1] == 'o' and board[1][2] == 'o'):
    return board[1][0]
  elif (board[2][0] == 'x' and board[2][1] == 'x' and board[2][2] == 'x') or (board[2][0] == 'o' and board[2][1] == 'o' and board[2][2] == 'o'):
    return board[2][0]
  elif (board[0][0] == 'x' and board[1][0] == 'x' and board[2][0] == 'x') or (board[0][0] == 'o' and board[1][0] == 'o' and board[2][0] == 'o'):
    return board[0][0]
  elif (board[0][1] == 'x' and board[1][1] == 'x' and board[2][1] == 'x') or (board[0][1] == 'o' and board[1][1] == 'o' and board[2][1] == 'o'):
    return board[0][1]
  elif (board[0][2] == 'x' and board[1][2] == 'x' and board[2][2] == 'x') or (board[0][2] == 'o' and board[1][2] == 'o' and board[2][2] == 'o'):
    return board[0][2]
  elif '_' not in board[0] and '' not in board[1] and '' not in board[2]:
    return '_'
  return False

def tictactoe():
  board = [
    ['_', '_', '_'],
    ['_', '_', '_'],
    ['_', '_', '_']
  ]

  player1 = 'x'
  player2 = 'o'
  empty = '_'
  turn = 1 #intially the turn will be one.

  print("""
GAME NAME: TicTacToe.
Rules:
1) there will be only two letters to choose they are 'x' and 'o'.
2) player1 will be 'x'.
3) player2 will be 'o'.
4) There will be a 3x3 board.
5) Any letter if it is consecutive diagnally or in a total column or in a total row then that letter's player will win.
6) if there is no winner then the game ends if don't want continue.
  """)

  Player1 = input("Enter your name x's player: ").strip().capitalize()
  Player2 = input("Enter your name o's player: ").strip().capitalize()
  
  while True:
    if turn % 2 == 0:
      print(f"It's {Player2}'s turn.")
    else: print(f"It's {Player1}'s turn.")
    currentPlayer = input("Enter the letter 'x' or 'o': ").strip()
    if turn%2 == 0 and currentPlayer != 'o':
      print(f"Its not your turn {Player1}!")
      continue
    elif turn%2 != 0 and currentPlayer != 'x':
      print(f"Its not your turn {Player2}!")
      continue
    turn += 1
    print("Enter the Row and Column of the board into which you wished to enter the letter('x' or 'o'): ")
    Row = int(input("Enter the row: ").strip())
    Col = int(input("Enter the column: ").strip())
    if board[Row][Col] == '_': board[Row][Col] = currentPlayer
    elif board[Row][Col] != '_':
      print("This place is occupied. Try any other place.")
      continue
    if player1 == checkBoard(board) or player2 == checkBoard(board):
      winner = checkBoard(board)
      if winner == player1: print(f"The Game is over!!! {Player1} is the winner.")
      else: print(f"The Game is over!!! {Player2} is the winner.")
      turn = 1
      for row in range(0, len(board)):
        for col in range(0, len(board[0])):
          print(board[row][col], end = "    ")
        print("")
        print("")
      answerQ = input("Do you guys still want to continue(yes/no)?").strip()
      if answerQ.lower()[0] == 'y':
        board = emptyBoard()
        turn = 1
        continue
      elif answerQ.lower()[0] == 'n':
        print("Then Run the game(code) again if you want to play this game some other time otherwise never come back.")
        break
      break
    if empty == checkBoard(board):
      board = emptyBoard()
      answerQ = input("No one is the winner. Do you guys still want to continue(yes/no)?").strip()
      if answerQ.lower()[0] == 'y':
        board = emptyBoard()
        turn = 1
        continue
      elif answerQ.lower()[0] == 'n':
        print("Then Run the game(code) again if you want to play this game some other time otherwise never come back.")
        break
    for row in range(0, len(board)):
        for col in range(0, len(board[0])):
          print(board[row][col], end = "    ")
        print("")
        print("")
    anyQ = input("Any Questions you wanna ask(like 'stop' to end the game else don't type anything if you still want to play)?").strip()
    if anyQ != '' and anyQ.lower()[0] == 's':
      board = emptyBoard()
      turn = 1
      break

#Running the game through main().
tictactoe()     
