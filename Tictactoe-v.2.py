score_1 = 0
score_2 = 0
def morpion_game():
    board = [' ' for  _ in range(9)]

    def print_board():
        print(f"{board[0]}  |{board[1]}  |{board[2]}")
        print("---+---+---")
        print(f"{board[3]}  |{board[4]}  |{board[5]}")
        print("---+---+---")
        print(f"{board[6]}  |{board[7]}  |{board[8]}")
    
    def winner(player):
            win_conditions= [(0,1,2), (3,4,5), (6,7,8)
                             ,(0,3,6), (1,4,7), (2,5,8)
                             ,(0,4,8), (2,4,6)
            ]
            for condition in win_conditions:
                if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
                 return True
            return False
            
                 
    
    def equal():
         if ' ' not in board and winner(symbol) is False and winner(symbol2) is False:
           print("Equality!")
           return True
         return False

      
    def symbols():
        global symbol
        global player1
        global name

        player1=(input(f"Player 1, choose X or O: "))
        player1= player1.upper()

        while player1 not in ['X','O']:
            player1=(input(f"Inavlid entry. Player 1, choose X or O only: "))
            player1= player1.upper()
       
        if player1 == "X":
            symbol = "X"
            name="Player 1"
       
        else:
            symbol ="O"
            name="Player 1"
       
        print(f"{name} you are", symbol)
   
    def play():
        symbols()
       
        global score_1
        global score_2
        global symbol2
       
        while True:
        
         try:
         
          position= int(input (f"Player 1, choose a position (0-8): "))  
          
          if position <0 or position >8:
              print("invalid entry. Please choose a valid number 0-8")  
              continue
         
         except ValueError:
          print("invalid entry. Please choose a valid number 0-8") 
          continue
        
         if board[position]!=' ':
          print("Position taken, please choose another position.")
          continue
        
         else:
            board[position]=symbol
            print_board()
           
            if winner(symbol):
                score_1 += 1  
                print(f"Player {name} won!")
                print(f"Total scores are: {name}: {score_1}, {name2}: {score_2}")
             
                replay= input("Do you want to play again? (y/n): ")
                if replay.lower() == 'y':
                 morpion_game()
               
                else:
                 break
            
            elif equal()==True:
            
             replay= input("Do you want to play again? (y/n): ")
             if replay.lower() == 'y':
              morpion_game()
            
             else:
              break
               
       
        
         if player1 == "X":
            symbol2 = "O"
            name2="Player 2"
         
         else:
            symbol2 ="X"
            name2="Player 2"
        
         
         try:
          
           position2= int(input (f"Player 2, choose a position (0-8): "))  
          
           if position2 <0 or position2 >8:
            print("Invalid entry. Please choose a valid number 0-8")  
          
            continue
         except ValueError:
            print("Invalid entry. Please choose a valid number 0-8")  
            continue
        
         if board[position2]!= ' ':
            print("Position taken, please choose another position.")
            continue
        
         else:
            board[position2]=symbol2
            print_board()
        
         if winner(symbol2):
            score_2 += 1  
            print(f"{name2} won!")
            print(f"Total scores are: {name}: {score_1}, {name2}: {score_2}")
           
            replay= input("Do you want to play again? (y/n): ")
            if replay.lower() == 'y':
              morpion_game()
           
            else:
              break
    
         if equal()==True:
          print(f"Total scores are: {name}: {score_1}, {name2}: {score_2}")
      
        return False
        
    play()
    
morpion_game()
