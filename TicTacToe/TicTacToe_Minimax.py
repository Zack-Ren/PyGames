board = [
	['', '', ''],
	['', '', ''],
	['', '', '']
	]

ai = "x"
player = "o"
currentPlayer = player


def displayBoard():
	for i in range (3):
		for j in range (3):
			print(board[i][j])


def threeInRow(a, b, c):
	return a == b and b == c and a != ''


def checkForWinner():
	winner = None

	# Horizontal check
	for i in range (3):
		if (threeInRow(board[i][0], board[i][1], board[i][2])):
			winner = board[i][0]

	# Vertical check
	for i in range (3):
		if (threeInRow(board[0][i], board[1][i], board[2][i])):
			winner = board[0][i]

	if (threeInRow(board[0][0], board[1][1], board[2][2])):
		winner = board[0][0]
	if (threeInRow(board[2][0], board[1][1], board[0][2])):
		winner = board[2][0]

	openSpace = 0
	for i in range (3):
		for j in range (3):
			if (board[i][j] == ''):
				openSpace += 1

	if (winner == None and openSpace == 0):
		return "tie"
	else: 
		return winner

def bestMove():
	bestScore = -100000
	for i in range(3):
		for j in range(3):
			if (board[i][j] == ""):
				board[i][j] = ai
				score = minimax(board, 0, False)
				board[i][j] = ""
				if(score > bestScore):
					bestScore = score
					move = [i, j]

	board[move[0]][move[1]] = ai
	currentPlayer = player


scores = {"x":10, "o":-10, "tie":0}

def minimax(board, depth, maximizing):
	res = checkForWinner()
	if (res != None):
		return scores[res]

	if (maximizing):
		bestScore = -100000

		for i in range (3):
			for j in range (3):
				if (board[i][j] == ''):
					board[i][j] = ai
					score = minimax(board, depth+1, False)
					board[i][j] = ''
					bestScore = max(score, bestScore)
		return bestScore

	else:
		bestScore = 100000
		for i in range (3):
			for j in range(3):
				if (board[i][j] == ''):
					board[i][j] = player
					score = minimax(board, depth+1, True)
					board[i][j] = ""
					bestScore = min(score, bestScore)

		return bestScore

bestMove()
displayBoard()

move = input("Your turn")

while (move != "q"):
	board[move/3][move%0] = player
	displayBoard()
	bestMove()
	move = input("Your turn")