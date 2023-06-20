no_of_round = int(input("Enter the no. of rounds: "))



player1_score = 0
player2_score = 0

for i in range(no_of_round):
    player1 = input("Enter the choice from R P S:  ").lower()
    player2 = input("Enter the choice from R P S : ").lower()
    if player1== player2:
        print("Draw")
    elif(player1== "r" and player2 =="s") or (player1=="s" and player2=="p") or (player1=="p" and player2=="r"):
        player1_score +=1
        print("player 1 won in " ,i+1, "game" )
    else:
        player2_score+=1
        print("player 2 won in " ,i+1, "game" )


if player1_score == player2_score:
    print("Game is Draw ")
elif player1_score>player2_score:
    print("Winner is Player 1 ")
else:
    print("Player 2 is Winner")