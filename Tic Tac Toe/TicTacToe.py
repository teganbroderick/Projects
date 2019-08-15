#!/usr/bin/env python3
#Tic Tac Toe game
#Tegan Broderick, 20190815
#Combined exercises from practicepython.org
#Game runs in the terminal using python 3

def game(gameboard, positionlist, running_position_list, turnlist):
	"""Function calculates what turn the game is up to, assigns a player (1 or 2) to that turn, asks for userinput, analyzes whether the input move is valid, converts the player input into a valid list position, and appends the move to the nested gameboard list. The function also calls the 'checkwinner' function to see if anyone has won the game"""

	#calculates what turn the game is up to, and therefore what player is making a move
	if turnlist[-1] % 2 == 0:
		player = "Player 2" #O
	else:
		player = "Player 1" #X
	turn = turnlist[-1] + 1
	turnlist.append(turn)

	#player input
	player_input = input(player + ", where would you like to place your piece? ")

	#Conditional, repeats if player chooses a position that's already taken or invalid
	while (player_input not in positionlist) or (player_input in running_position_list):
		print("That's not a valid position.")
		player_input = input(player + ", where would you like to place your piece? ")

	#convert userinput to correct format for python lists (starting at zero)
	running_position_list.append(player_input)#append input position to running position list, refer to in subsequent moves
	player_input = player_input.split(",") #split string into a list

	player_position = [] #list for player position in python list format
	for i in player_input:
		tempnumber = int(i) - 1 #minus one from each value to get correct nested list location
		player_position.append(tempnumber)

	#'place piece' into nested list
	x = player_position[0]
	y = player_position[1]
	if player == "Player 1":
		gameboard[x][y] = "X"
	else:
		gameboard[x][y] = "O"

	#print gameboard
	print()
	print("Gameboard:")
	print(" " + (" ---" * 3))
	for i in range (0,3):
		for j in range(0,3):
			print(" | ", end='')
			print(gameboard[i][j], end='')
		print(" |")
		print(" " + (" ---" * 3))
	print()

	checkforwinner(gameboard)

def checkforwinner(nestedlist):
	"""Function analyses nestedlist (gameboard) to see if anyone has won the game."""
	winner = " " #space " " will be analyed as the winner with an empty or near empty board

	#horizontal win options
	if nestedlist[0][0] == nestedlist[0][1]  == nestedlist[0][2]:
		winner = nestedlist[0][0]
	elif nestedlist[1][0] == nestedlist[1][1] == nestedlist[1][2]:
		winner = nestedlist[1][0]
	elif nestedlist[2][0] == nestedlist[2][1] == nestedlist[2][2]:
		winner = nestedlist[2][0]

	#vertical win options
	elif nestedlist[0][0] == nestedlist[1][0] == nestedlist[2][0]:
		winner = nestedlist[0][0]
	elif nestedlist[0][1] == nestedlist[1][1] == nestedlist[2][1]:
		winner = nestedlist[0][1]
	elif nestedlist[0][2] == nestedlist[1][2] == nestedlist[2][2]:
		winner = nestedlist[0][2]

	#diagonal win options
	elif nestedlist[0][0] == nestedlist[1][1] == nestedlist[2][2]:
		winner = nestedlist[0][0]
	elif nestedlist[2][0] == nestedlist[1][1] == nestedlist[0][2]:
		winner = nestedlist[2][0]

	#tie - game is out of spaces and there is no winner
	elif " " not in nestedlist[0] and " " not in nestedlist[1] and " " not in nestedlist[2]:
		print("You are out of spaces. The game is a tie.")
		return True

	else:
		print()

	#results
	if winner == "X":
		print("Player 1 wins!")
		return True
	elif winner == "O":
		print("Player 2 wins!")
		return True
	else:
		return False


#introduction
print("Welcome to Tic Tac Toe. Player one is 'X', and player two is 'O'. To play, specify your desired position using the format 'row, column'.")
print()
print("Here is an example board showing positions: ")
dottedline = (" " + (" ---" * 3))
print(dottedline)
print(" |1,1|1,2|1,3|")
print(dottedline)
print(" |2,1|2,2|2,3|")
print(dottedline)
print(" |3,1|3,2|3,3|")
print(dottedline)

#Play game
repeat = "yes"
while repeat == "yes":
	#setup
	gameboard = [[" "," "," "], [" "," "," "], [" "," "," "]]
	positionlist = ["1,1", "1,2", "1,3", "2,1", "2,2", "2,3", "3,1", "3,2", "3,3" ] #every possible position, used to verify user input
	running_position_list = [] #to store positions as they are chosen by the users, and reference to see if the requested position is already taken
	turnlist = [1] #used for calcuating which player is making a move
	print()
	print("Gameboard:")
	print(" " + (" ---" * 3))
	for i in range (0,3):
		for j in range(0,3):
			print(" | ", end='')
			print(gameboard[i][j], end='')
		print(" |")
		print(" " + (" ---" * 3))
	print()

	while checkforwinner(gameboard) == False:
		game(gameboard, positionlist, running_position_list, turnlist)
	print("-" * 60)
	repeat = input("Would you like to play again? yes or no: ")
