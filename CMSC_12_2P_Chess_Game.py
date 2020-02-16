import os
import ChessFunc

alternator = 1 

while True:
	if ChessFunc.dec:
		break
		
	x_pos = ""
	y_pos = ""
	x_loc = ""
	y_loc = ""

	valid_move = True

	ChessFunc.board_print(ChessFunc.board, ChessFunc.coordinates)

	ChessFunc.find_king(alternator)
	ChessFunc.checkmate(ChessFunc.king_x, ChessFunc.king_y, alternator)
	if ChessFunc.end:
		break
	ChessFunc.check(ChessFunc.king_x, ChessFunc.king_y, alternator)

	print("Type \"Save\" to save current Game Data.")
	print("Type \"Load\" to load a saved Game Data.")

	if ChessFunc.checked:
		if alternator == 1:
			print("\nPlayer 2 says you are Checked.")
		elif alternator == 2:
			print("\nPlayer 1 says you are Checked.")

	if alternator == 1:
		print("\nIt\'s Player 1\'s turn!")
	else:
		print("\nIt\'s Player 2\'s turn!")
	
	if alternator == 1:
		piece_pos = input("\nEnter Position of Piece to Move: ")
		if piece_pos == "Save":
			file_name = input("Enter File name for Game Data to Save: ")
			ChessFunc.save_board(file_name)
			break
		elif piece_pos == "Load":
			file_name = input("Enter File name of Game Data to Load: ")
			ChessFunc.load_board(file_name)
			continue
		else:
			x_pos = piece_pos[0] + " "
			y_pos = piece_pos[1]
		
		if (ChessFunc.board[ChessFunc.coordinates[1].index(y_pos)][ChessFunc.coordinates[0].index(x_pos)])[1] != "1":
			print("\nInvalid Move! It\'s Player 1\'s turn to move.")
			valid_move = False
		else:
			board_loc = input("\nWhere do you want to move " + ChessFunc.board[ChessFunc.coordinates[1].index(y_pos)][ChessFunc.coordinates[0].index(x_pos)] + " : ")
			x_loc = board_loc[0] + " "
			y_loc = board_loc[1]
	else:
		piece_pos = input("\nEnter Position of Piece to Move: ")
		if piece_pos == "Save":
			file_name = input("Enter File name for Game Data to Save: ")
			ChessFunc.save_board(file_name)
			break
		elif piece_pos == "Load":
			file_name = input("Enter File name of Game Data to Load: ")
			ChessFunc.load_board(file_name)
			continue
		else:
			x_pos = piece_pos[0] + " "
			y_pos = piece_pos[1]
		
		if (ChessFunc.board[ChessFunc.coordinates[1].index(y_pos)][ChessFunc.coordinates[0].index(x_pos)])[1] != "2":
			print("\nInvalid Move! It\'s Player 2\'s turn to move.")
			valid_move = False
		else:
			board_loc = input("\nWhere do you want to move " + ChessFunc.board[ChessFunc.coordinates[1].index(y_pos)][ChessFunc.coordinates[0].index(x_pos)] + " : ")
			x_loc = board_loc[0] + " "
			y_loc = board_loc[1]

	if valid_move:

		# Pawn Function
		if ChessFunc.board[ChessFunc.coordinates[1].index(y_pos)][ChessFunc.coordinates[0].index(x_pos)] == "P1":
			white_pawn = True
			ChessFunc.pawn(x_pos, y_pos, x_loc, y_loc, white_pawn, alternator)
			ChessFunc.pawn_promotion(y_pos, x_loc, y_loc, alternator)
		elif ChessFunc.board[ChessFunc.coordinates[1].index(y_pos)][ChessFunc.coordinates[0].index(x_pos)] == "P2":
			white_pawn = False
			ChessFunc.pawn(x_pos, y_pos, x_loc, y_loc, white_pawn, alternator)
			ChessFunc.pawn_promotion(y_pos, x_loc, y_loc, alternator)

		# Bishop Function
		elif ChessFunc.board[ChessFunc.coordinates[1].index(y_pos)][ChessFunc.coordinates[0].index(x_pos)] == "B1":
			white_bishop = True
			ChessFunc.bishop(x_pos, y_pos, x_loc, y_loc, white_bishop, alternator)
		elif ChessFunc.board[ChessFunc.coordinates[1].index(y_pos)][ChessFunc.coordinates[0].index(x_pos)] == "B2":
			white_bishop = False
			ChessFunc.bishop(x_pos, y_pos, x_loc, y_loc, white_bishop, alternator)

		# Rook Function
		elif ChessFunc.board[ChessFunc.coordinates[1].index(y_pos)][ChessFunc.coordinates[0].index(x_pos)] == "R1":
			white_rook = True
			ChessFunc.rook(x_pos, y_pos, x_loc, y_loc, white_rook, alternator)
		elif ChessFunc.board[ChessFunc.coordinates[1].index(y_pos)][ChessFunc.coordinates[0].index(x_pos)] == "R2":
			white_rook = False
			ChessFunc.rook(x_pos, y_pos, x_loc, y_loc, white_rook, alternator)

		# Knight Function
		elif ChessFunc.board[ChessFunc.coordinates[1].index(y_pos)][ChessFunc.coordinates[0].index(x_pos)] == "N1":
			white_knight = True
			ChessFunc.knight(x_pos, y_pos, x_loc, y_loc, white_knight, alternator)
		elif ChessFunc.board[ChessFunc.coordinates[1].index(y_pos)][ChessFunc.coordinates[0].index(x_pos)] == "N2":
			white_knight = False
			ChessFunc.knight(x_pos, y_pos, x_loc, y_loc, white_knight, alternator)

		# Queen Function
		elif ChessFunc.board[ChessFunc.coordinates[1].index(y_pos)][ChessFunc.coordinates[0].index(x_pos)] == "Q1":
			white_queen = True
			ChessFunc.queen(x_pos, y_pos, x_loc, y_loc, white_queen, alternator)
		elif ChessFunc.board[ChessFunc.coordinates[1].index(y_pos)][ChessFunc.coordinates[0].index(x_pos)] == "Q2":
			white_queen = False
			ChessFunc.queen(x_pos, y_pos, x_loc, y_loc, white_queen, alternator)

		# King Function
		elif ChessFunc.board[ChessFunc.coordinates[1].index(y_pos)][ChessFunc.coordinates[0].index(x_pos)] == "K1":
			white_king = True
			ChessFunc.king(x_pos, y_pos, x_loc, y_loc, white_king, alternator)
		elif ChessFunc.board[ChessFunc.coordinates[1].index(y_pos)][ChessFunc.coordinates[0].index(x_pos)] == "K2":
			white_king = False
			ChessFunc.king(x_pos, y_pos, x_loc, y_loc, white_king, alternator)

		ChessFunc.find_king(alternator)
		ChessFunc.check(ChessFunc.king_x, ChessFunc.king_y, alternator)

		if ChessFunc.checked:
			print("\nInvalid Move! Your King is Checked.")
			ChessFunc.no_error = False

		if ChessFunc.no_error:  # Determine if move is valid and executed properly
			# Switches after every valid player's move
			if alternator == 1:
				alternator = 2
			else:
				alternator = 1

	ChessFunc.no_error = True

	ChessFunc.checked = False

	input("\nPress anything to continue...")

	os.system("clear")

if piece_pos != "Save":
	if alternator == 1:
		print("\nGame Ended! It's a Checkmate. Player 2 won the game.")

	elif alternator == 2:
		print("\nGame Ended! It's a Checkmate. Player 1 won the game.")

	print("------SCORES-----")
	print("Player 1 Score: ", ChessFunc.p1_score)
	print("Player 2 Score: ", ChessFunc.p2_score)
