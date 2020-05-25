import math

def bestMove():
	bestScore = -math.inf
	for i in range(3):
		for j in range(3):
			if board[i][j] == "-":
				board[i][j] = "x"
				score = minimax(board, 0, False)
				board[i][j] = "-"
				if(score > bestScore):
					bestScore = score
					move = [i, j]

	board[move[0]][move[1]] = "x"


scores = {X:10, O:-10, tie:0}

def minimax(board, depth, maximizing):
	res = checkWin()
	if res != False:
		return scores[res]

	if (maximizing):
		bestScore = -math.inf

		for i in range (3):
			for j in range (3):
				if board[i][j] == "-":
					board[i][j] = "x"
					score = minimax(board, depth+1, False)
					board[i][j] = "-"
					bestScore = max(score, bestScore)
		return bestScore

	else:
		bestScore = math.inf
		for i in range (3):
			for j in range(3):
				if board[i][j] == "-":
					board[i][j] = "o"
					score = minimax(board, depth+1, True)
					board[i][j] = "-"
					bestScore = min(score, bestScore)

		return bestScore

