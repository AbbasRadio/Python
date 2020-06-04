import random
# Stone Paper Scissors
# chances = 0
# ComputerScore = 0
# PlayerScore = 0
# Move = ['Stone','Paper','Scissors']
# while chances != 10:
#     chances+=1
#     CompChance = random.choice(Move)
#     PlayerChance = random.choice(Move)
#     if CompChance == PlayerChance :
#         ComputerScore+=1
#         PlayerScore+=1
#         print('Match Tied')
#     elif PlayerChance == 'Stone' and CompChance == 'Paper':
#         ComputerScore+=1
#         print("Computer Won")
#     elif PlayerChance == 'Stone' and CompChance == 'Scissors':
#         PlayerScore+=1
#         print("Player Won")
#     elif PlayerChance == 'Paper' and CompChance == 'Stone':
#         PlayerScore+=1
#         print("Player Won")
#     elif PlayerChance == 'Paper' and CompChance == 'Scissors':
#         ComputerScore+=1
#         print("Computer Won")
#     elif PlayerChance == 'Scissors' and CompChance == 'Paper':
#         PlayerScore+=1
#         print("Player Won")
#     elif PlayerChance == 'Scissors' and CompChance == 'Stone':
#         ComputerScore+=1
#         print("Computer Won")
# print("Total Score of Player :",PlayerScore)
# print("Total Score of Computer :",ComputerScore)
# if PlayerScore>ComputerScore :
#     print("And the Winner is : Player")
# elif PlayerScore<ComputerScore :
#     print("And the Winner is : Computer")
# else :
#     print("Series is Tied")
#=============================================================================================================

moves = ['Stone','Paper','Scissors']
PossibleOutcome = [['Stone','Scissor'],['Scissor','Paper'],['Paper','Stone']]
playerScore = 0
compScore = 0
chance = 0
print("For Stone Press S")
print("For Paper Press P")
print("For Scissors Press X")
while chance != 10 :
    chance+=1
    computer = random.choice(moves)
    playerGet = input("Enter Your Choice S/P/X :")
    playerAsk = playerGet.lower()
    if playerAsk == 's':
        player = 'Snake'
    elif playerAsk == 'p':
        player = 'Paper'
    else:
        player = 'Scissors'
    # player = random.choice(moves)
    if computer == player:
        print("Match Tied and Score Stands as => [Computer]=>[",compScore,"] [Player]=>[",playerScore,"]")
    elif [player,computer] in PossibleOutcome :
        playerScore+=1
        print("Match Won by Player and Score Stands as => [Computer]=>[", compScore, "] [Player]=>[", playerScore, "]")
    else :
        compScore+=1
        print("Match Won by Computer and Score Stands as => [Computer]=>[", compScore, "] [Player]=>[", playerScore, "]")

print("Total Score of Player :",playerScore)
print("Total Score of Computer :",compScore)
if playerScore>compScore :
    print("And the Winner is : Player")
elif playerScore<compScore :
    print("And the Winner is : Computer")
else :
    print("Series is Tied")