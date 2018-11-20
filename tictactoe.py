
# coding: utf-8

# In[1]:



from IPython.display import clear_output

def display_board(board):
    clear_output()
    
    print( board[1] +'|'+board[2]+'|'+board[3])
    print( board[4] +'|'+board[5]+'|'+board[6])
    print( board[7] +'|'+board[8]+'|'+board[9])


# In[2]:


def player_input():
    
    marker =''
    while ((marker !='X') and (marker !='O')) :
     marker= input ('Player1 , Do you want to be X or O?')       
     player1=marker
    if player1 =='X':
           player2='O'
    else : 
           player2='X'
    return(player1,player2)
       
            


# In[3]:



def place_marker(board, marker, position):
    
    board[position] = marker
        


# In[4]:


def win_check(board, marker):
    if((board[7] == board[8] == board[9] == marker) or
       (board[4] == board[5] == board[6] == marker) or
       (board[1] == board[2] == board[3] == marker) or
       (board[1] == board[5] == board[9] == marker)) : 
     return True
    else: 
     return False


# In[5]:


import random

def choose_first():
    
      return('Player1')
 
    


# In[6]:


def space_check(board, position):
    
    return(board[position]==' ')


# In[7]:


def full_board_check(board):
    sp = 0
    for char in board :
      if char == ' ' :
           sp = sp +1
      if (sp >0):
        return(False)
      else:
        return(True)
    


# In[8]:


def player_choice(board):
     pos1 = int(input('Please enter a number between 0,9 as a position')) 
     if space_check(board,pos1):
        return(pos1)
        


# In[9]:


def replay():
     ans = ' '
     ans = input ('Do you want to play again (Y/N)') 
     if (ans.lower()== "y"):
            return(True)
     else :
            return(False)
    


# In[10]:


print('Welcome to Tic Tac Toe!')
while True:
    # Reset the board
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')
    play_game = input('Are you ready to play? Enter Yes or No.')
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            # Player1's turn.
            
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('Congratulations! You have won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player2's turn.
            
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break

