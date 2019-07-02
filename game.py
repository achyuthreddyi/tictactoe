

# board
# display the board
# play game

# winning logic
  # check rows
  # check columsn
  # check diagonal
# check tie
#  flip the player 
board = ["-","-","-",
          "-","-","-",
          "-","-","-"]
game_still_going =True

winner = None

#  whose turn is it 
current_player = "x"

def display_board():
  print(board[0]+" | " + board[1] + " | "+ board[2] + " | ")
  print(board[3]+" | " + board[4] + " | "+ board[5] + " | ")
  print(board[6]+" | " + board[7] + " | "+ board[8] + " | ")
def play_game():

  # display the board
  display_board()


  while game_still_going:
    handle_turn(current_player)

    check_if_game_over()

    flip_player()

    #  game ended 

    


def handle_turn(current_player):
  print(current_player+"'s turn")
  position  = input("choose a position from 1 to 9   ")
  valid =False
  while not valid:

    while position not in ["1","2","3","4","5","6","7","8","9"]:
      display_board()
      position = input("invalid input choose a position from 1 to 9 ")
      

    position  = int(position) - 1 

    if board[position] == "-":
      valid =True
    else:
      print ("you cant go there")



  board[position ] = current_player
  display_board()

def flip_player():
  global current_player
  if current_player == "x":
    current_player = "o"
   
  elif current_player == "o":
    current_player = "x"
    
  return


def check_if_game_over():
  check_if_win()
  check_if_tie()
  if (check_if_win or check_if_tie):
    game_still_going =False
  

  if check_if_win:
    if winner == "x" or winner == "o" :
      print(winner + "won!!!")
    # elif winner == None:
      # print(" tie ...")




def check_if_win():

  global winner
  
  # check rows
  row_winner = check_rows()
  # check columsn
  colwinner = check_cols()
  # check diagonal
  diawinner = check_dia()

  if row_winner:
    #  there was a winner
    winner = row_winner
  elif colwinner:
    # there was a winner
    winner = colwinner
  else: 
    #  there was a winner
    winner = diawinner

  return 

def check_rows():
  global game_still_going
  row_1 = board[0] == board[1] == board[2] != "-"
  row_2 = board[3] == board[4] == board[5] != "-"
  row_3 = board[6] == board[7] == board[8] != "-"

  if row_1 or row_2 or row_3:
    game_still_going = False
  if row_1:
    return board[0]
  if row_2:
    return board[3]
  if row_3:
    return board[6]
  return
  

  
def check_cols():
  global game_still_going

  col_1 = board[0] == board[3] == board[6] != "-"
  col_2 = board[1] == board[4] == board[7] != "-"
  col_3 = board[2] == board[5] == board[8] != "-"

  if col_1 or col_2 or col_3:
    game_still_going = False
  if col_1:
    return board[0]
  if col_2:
    return board[1]
  if col_3:
    return board[2]
  return
  

def check_dia():

  global game_still_going

  dia_1 = board[0] == board[4] == board[8] != "-"
  dia_2 = board[2] == board[4] == board[6] != "-"
  

  if dia_1 or dia_2 :
    game_still_going = False
  if dia_1:
    return board[0]
  if dia_2:
    return board[2]
  
  return
  




def check_if_tie():
  global game_still_going
  if "-" not in board:
    game_still_going = False
    print("match tie")
  

  

# def game_still_going():
  # pass



# def current_player():
#   pass



play_game()