board = [["R2", "N2", "B2", "Q2", "K2", "B2", "N2", "R2"],
		 ["P2", "P2", "P2", "P2", "P2", "P2", "P2", "P2"],
		 ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
		 ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
		 ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
		 ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
		 ["P1", "P1", "P1", "P1", "P1", "P1", "P1", "P1"],
		 ["R1", "N1", "B1", "Q1", "K1", "B1", "N1", "R1"]]

coordinates = [["A ", "B ", "C ", "D ", "E ", "F ", "G ", "H "],
			   ["8", "7", "6", "5", "4", "3", "2", "1"]]

end = False
dec = False
p1_score = 0
p2_score = 0

no_error = True
piece_class1 = ""
piece_class2 = ""
capt_piece = ""  # Captured piece classifier

king_x = ""
king_y = ""

checked = False

# Checks if King or Rooks made their first move
white_k = False
white_r1 = False
white_r2 = False

black_k = False
black_r1 = False
black_r2 = False


def find_king(alt):
	global king_x
	global king_y

	for i in range(8):
		for j in range(8):
			if alt == 1:
				if (board[i][j]) == "K1":
					king_x = coordinates[0][j]
					king_y = coordinates[1][i]
					return
			if alt == 2:
				if (board[i][j]) == "K2":
					king_x = coordinates[0][j]
					king_y = coordinates[1][i]
					return


def board_print(x, y):
	print()
	print(" " * 71, "This is a Chess Board!")
	print()
	print(" " * 59, "-" * 50, end="")
	print()
	for i in range(len(x)):
		print(" " * 52, y[1][i], " " * 5, end="")
		for j in range(8):
			print("|", x[i][j], end="")
			print("  ", end="")
		print(" ", end="")
		print("|", " " * 4, y[1][i])
		print(" " * 59, "-" * 50)

	print()
	print(" " * 60, end="")
	for i in range(len(x)):
		print(" ", y[0][i], end="  ")
	print()


def pawn(x1, y1, x2, y2, white_pawn, alt):
	global no_error
	global checked
	global piece_class1
	global piece_class2
	global capt_piece
	global king_x
	global king_y
	global dec

	# determine which player is making the move
	if (board[coordinates[1].index(y1)][coordinates[0].index(x1)])[1] == "1":
		piece_class1 = "Player 1"
	elif (board[coordinates[1].index(y1)][coordinates[0].index(x1)])[1] == "2":
		piece_class1 = "Player 2"

	if (board[coordinates[1].index(y2)][coordinates[0].index(x2)])[1] == "1":
		piece_class2 = "Player 1"
	elif (board[coordinates[1].index(y2)][coordinates[0].index(x2)])[1] == "2":
		piece_class2 = "Player 2"

	# Determine which piece is captured
	if (board[coordinates[1].index(y2)][coordinates[0].index(x2)])[0] == "P":
		capt_piece = " Pawn"
	elif (board[coordinates[1].index(y2)][coordinates[0].index(x2)])[0] == "R":
		capt_piece = " Rook"
	elif (board[coordinates[1].index(y2)][coordinates[0].index(x2)])[0] == "B":
		capt_piece = " Bishop"
	elif (board[coordinates[1].index(y2)][coordinates[0].index(x2)])[0] == "N":
		capt_piece = " Knight"
	elif (board[coordinates[1].index(y2)][coordinates[0].index(x2)])[0] == "Q":
		capt_piece = " Queen"
	elif (board[coordinates[1].index(y2)][coordinates[0].index(x2)])[0] == "K":
		capt_piece = " King"
	
	if capt_piece == " King":
		dec = True

	virtual_move(x1, y1, x2, y2, alt)  # Assumes that the move is executed then determine if king is still checked or not

	if checked:
		print("Invalid Move! King will be checked after execution of move.")
		return

	if not checked:

		# error catching phase
		if white_pawn:
			if coordinates[1].index(y1) < coordinates[1].index(y2):  # White Pawn Backward Move
				print("\nInvalid Move! Pawns cannot move backwards. ")
				no_error = False

			elif y1 == y2 and x1 != x2:  # if pawn tries to move horizontally
				print("\nInvalid Move! Pawns cannot move sidewards. ")
				no_error = False

			elif coordinates[1].index(y1) - coordinates[1].index(y2) > 2:  # if pawn tries to move a long range vertical move
				print("\nInvalid Move! Pawns cannot move more than 2 spaces. ")
				no_error = False

			elif ((coordinates[0].index(x1) + 2 < coordinates[0].index(x2)) and (coordinates[1].index(y1) - 2 > coordinates[1].index(y2))) or ((coordinates[0].index(x1) - 2 > coordinates[0].index(x2)) and (coordinates[1].index(y1) - 2 > coordinates[1].index(y2))):  # if pawn tries to do a long range diagonal move
				print("\nInvalid Move! Pawns cannot move more than 1 space diagonally. ")
				no_error = False

			elif (board[coordinates[1].index(y2)][coordinates[0].index(x2)])[1] == "1":  # Ally Replace and Move Repetition
				print("\nInvalid Move! Pawns cannot capture allied piece. ")
				no_error = False

		elif not white_pawn:
			if coordinates[1].index(y1) > coordinates[1].index(y2):  # Black Pawn Backward Move
				print("\nInvalid Move! Pawns cannot move backwards. ")
				no_error = False

			elif y1 == y2 and x1 != x2:  # if pawn tries to move horizontally
				print("\nInvalid Move! Pawns cannot move sidewards. ")
				no_error = False

			elif coordinates[1].index(y1) - coordinates[1].index(y2) < -2:  # if pawn tries to move a long range vertical move
				print("\nInvalid Move! Pawns cannot move more than 2 spaces. ")
				no_error = False

			elif ((coordinates[0].index(x1) + 2 < coordinates[0].index(x2)) and (coordinates[1].index(y1) + 2 < coordinates[1].index(y2))) or ((coordinates[0].index(x1) - 2 > coordinates[0].index(x2)) and (coordinates[1].index(y1) + 2 < coordinates[1].index(y2))):  # if pawn tries to do a long range diagonal move
				print("\nInvalid Move! Pawns cannot move more than 1 space diagonally. ")
				no_error = False

			elif (board[coordinates[1].index(y2)][coordinates[0].index(x2)])[1] == "2":  # Ally Replace and Move Repetition
				print("\nInvalid Move! Pawns cannot capture allied piece. ")
				no_error = False

		if no_error:
			if white_pawn:
				if coordinates[1].index(y1) == 6:
					if (coordinates[1].index(y1) - 2 == coordinates[1].index(y2) or coordinates[1].index(y1) - 1 == coordinates[1].index(y2)) and (x1 == x2):  # if pawn tries to move 1 or 2 spaces forward
						if board[coordinates[1].index(y1) - 1][coordinates[0].index(x1)] == "  ":  # Collision checker

							virtual_move(x1, y1, x2, y2, alt)  # Assumes that the move is executed then determine if king is still checked or not

							if checked:
								return

							elif not checked:
								print("\n" + piece_class1 + "\'s " + "Pawn " + "will move from " + x1[0] + y1 + " to " + x2[0] + y2 + ".")
								board[coordinates[1].index(y2)][coordinates[0].index(x2)] = board[coordinates[1].index(y1)][coordinates[0].index(x1)]
								board[coordinates[1].index(y1)][coordinates[0].index(x1)] = "  "
								return
						else:
							print("\nInvalid Move! Pawns cannot move over other pieces. ")
							no_error = False

				elif coordinates[1].index(y1) != 6:
					if (coordinates[1].index(y1) - 1 == coordinates[1].index(y2)) and (x1 == x2):  # if pawn tries to move 1 space forward
						if board[coordinates[1].index(y1) - 1][coordinates[0].index(x1)] == "  ":  # Collision checker
							print("\n" + piece_class1 + "\'s " + "Pawn " + "will move from " + x1[0] + y1 + " to " + x2[0] + y2 + ".")
							board[coordinates[1].index(y2)][coordinates[0].index(x2)] = board[coordinates[1].index(y1)][coordinates[0].index(x1)]
							board[coordinates[1].index(y1)][coordinates[0].index(x1)] = "  "
							return
						else:
							print("\nInvalid Move! Pawns cannot move over other pieces. ")
							no_error = False

				if no_error:
					if coordinates[1].index(y1) - 1 == coordinates[1].index(y2) and (coordinates[0].index(x1) - 1 == coordinates[0].index(x2) or coordinates[0].index(x1) + 1 == coordinates[0].index(x2)):  # pawn tries to move 1 space diagonally
						if (board[coordinates[1].index(y2)][coordinates[0].index(x2)])[1] == "2":
							scorer(x2, y2, alt)
							print("\n" + piece_class1 + "\'s " + "Pawn" + " captured " + piece_class2 + "\'s" + capt_piece + ".")
							board[coordinates[1].index(y2)][coordinates[0].index(x2)] = board[coordinates[1].index(y1)][coordinates[0].index(x1)]
							board[coordinates[1].index(y1)][coordinates[0].index(x1)] = "  "
						else:
							print("\nInvalid Move! Pawns cannot move diagonally unless attempting to capture. ")
							no_error = False
					else:
						if (coordinates[0].index(x1) + coordinates[1].index(y1) == coordinates[0].index(x2) + coordinates[1].index(y2)) or (coordinates[0].index(x1) - coordinates[1].index(y1) == coordinates[0].index(x2) - coordinates[1].index(y2)):  # Determine if chosen movement is diagonal in nature
							print("\nInvalid Move! Pawns cannot move more than one space diagonally. ")
							no_error = False
						else:
							print("\nInvalid Move! Pawns cannot move that way. ")
							no_error = False

			elif not white_pawn:
				if coordinates[1].index(y1) == 1:
					if (coordinates[1].index(y1) + 2 == coordinates[1].index(y2) or coordinates[1].index(y1) + 1 == coordinates[1].index(y2)) and (x1 == x2):  # if pawn tries to move 1 or 2 spaces forward
						if board[coordinates[1].index(y1) + 1][coordinates[0].index(x1)] == "  ":  # Collision checker
							print("\n" + piece_class1 + "\'s " + "Pawn " + "will move from " + x1[0] + y1 + " to " + x2[0] + y2 + ".")
							board[coordinates[1].index(y2)][coordinates[0].index(x2)] = board[coordinates[1].index(y1)][coordinates[0].index(x1)]
							board[coordinates[1].index(y1)][coordinates[0].index(x1)] = "  "
							return
						else:
							print("\nInvalid Move! Pawns cannot move over other pieces. ")
							no_error = False
					elif coordinates[0].index(x1) + 1 != coordinates[0].index(x2) and coordinates[0].index(x1) - 1 != coordinates[0].index(x2):
						print("\nInvalid Move! Pawns cannot move that way. ")
						no_error = False

				elif coordinates[1].index(y1) != 1:
					if (coordinates[1].index(y1) + 1 == coordinates[1].index(y2)) and (x1 == x2):  # if pawn tries to move 1 space forward
						if board[coordinates[1].index(y1) + 1][coordinates[0].index(x1)] == "  ":  # Collision checker
							print("\n" + piece_class1 + "\'s " + "Pawn " + "will move from " + x1[0] + y1 + " to " + x2[0] + y2 + ".")
							board[coordinates[1].index(y2)][coordinates[0].index(x2)] = board[coordinates[1].index(y1)][coordinates[0].index(x1)]
							board[coordinates[1].index(y1)][coordinates[0].index(x1)] = "  "
							return
						else:
							print("\nInvalid Move! Pawns cannot move over other pieces. ")
							no_error = False
					elif coordinates[0].index(x1) + 1 != coordinates[0].index(x2) and coordinates[0].index(x1) - 1 != coordinates[0].index(x2):
						print("\nInvalid Move! Pawns cannot move that way. ")
						no_error = False

				if no_error:
					if (coordinates[1].index(y1) + 1 == coordinates[1].index(y2)) and ((coordinates[0].index(x1) - 1 == coordinates[0].index(x2)) or (coordinates[0].index(x1) + 1 == coordinates[0].index(x2))):  # pawn tries to move 1 space diagonally
						if (board[coordinates[1].index(y2)][coordinates[0].index(x2)])[1] == "1":
							scorer(x2, y2, alt)
							print("\n" + piece_class1 + "\'s " + "Pawn" + " captured " + piece_class2 + "\'s" + capt_piece + ".")
							board[coordinates[1].index(y2)][coordinates[0].index(x2)] = board[coordinates[1].index(y1)][coordinates[0].index(x1)]
							board[coordinates[1].index(y1)][coordinates[0].index(x1)] = "  "
						else:
							print("\nInvalid Move! Pawns cannot move diagonally unless attempting to capture. ")
							no_error = False
					else:
						if (coordinates[0].index(x1) + coordinates[1].index(y1) == coordinates[0].index(x2) + coordinates[1].index(y2)) or (coordinates[0].index(x1) - coordinates[1].index(y1) == coordinates[0].index(x2) - coordinates[1].index(y2)):  # Determine if chosen movement is diagonal in nature
							print("\nInvalid Move! Pawns cannot move more than one space diagonally. ")
							no_error = False
						else:
							print("\nInvalid Move! Pawns cannot mov87e that way. ")
							no_error = False


def bishop(x1, y1, x2, y2, white_bishop, alt):
	global no_error
	global piece_class1
	global piece_class2
	global capt_piece
	global dec
	
	# determine which player is making the move
	if (board[coordinates[1].index(y1)][coordinates[0].index(x1)])[1] == "1":
		piece_class1 = "Player 1"
	elif (board[coordinates[1].index(y1)][coordinates[0].index(x1)])[1] == "2":
		piece_class1 = "Player 2"

	if (board[coordinates[1].index(y2)][coordinates[0].index(x2)])[1] == "1":
		piece_class2 = "Player 1"
	elif (board[coordinates[1].index(y2)][coordinates[0].index(x2)])[1] == "2":
		piece_class2 = "Player 2"

	# Determine which piece is captured
	if (board[coordinates[1].index(y2)][coordinates[0].index(x2)])[0] == "P":
		capt_piece = " Pawn"
	elif (board[coordinates[1].index(y2)][coordinates[0].index(x2)])[0] == "R":
		capt_piece = " Rook"
	elif (board[coordinates[1].index(y2)][coordinates[0].index(x2)])[0] == "B":
		capt_piece = " Bishop"
	elif (board[coordinates[1].index(y2)][coordinates[0].index(x2)])[0] == "N":
		capt_piece = " Knight"
	elif (board[coordinates[1].index(y2)][coordinates[0].index(x2)])[0] == "Q":
		capt_piece = " Queen"
	elif (board[coordinates[1].index(y2)][coordinates[0].index(x2)])[0] == "K":
		capt_piece = " King"
		
	if capt_piece == " King":
		dec = True

	space = True
	a = 1

	virtual_move(x1, y1, x2, y2, alt)  # Assumes that the move is executed then determine if king is still checked or not

	if not checked:

		if white_bishop:
			if (board[coordinates[1].index(y2)][coordinates[0].index(x2)])[1] == "1":
				print("\nInvalid Move! Bishops cannot capture allied piece.")
				no_error = False
				return
		if not white_bishop:
			if (board[coordinates[1].index(y2)][coordinates[0].index(x2)])[1] == "2":
				print("\nInvalid Move! Bishops cannot capture allied piece.")
				no_error = False
				return

		if (coordinates[0].index(x1) + coordinates[1].index(y1) == coordinates[0].index(x2) + coordinates[1].index(y2)) or (coordinates[0].index(x1) - coordinates[1].index(y1) == coordinates[0].index(x2) - coordinates[1].index(y2)):  # Determine if chosen movement is diagonal in nature
			if coordinates[1].index(y1) > coordinates[1].index(y2) and coordinates[0].index(x1) < coordinates[0].index(x2):  # North-East Movement of Bishop
				if ((coordinates[1].index(y1) - coordinates[1].index(y2)) - 1) == 0:  # Check if bishop is moving for only 1 space diagonally
					if white_bishop:
						if board[coordinates[1].index(y2)][coordinates[0].index(x2)] == "  ":  # Check if adjacent location tile is empty
							print("\n" + piece_class1 + "\'s " + "Bishop " + "will move from " + x1[0] + y1 + " to " + x2[0] + y2 + ".")
							board[coordinates[1].index(y2)][coordinates[0].index(x2)] = board[coordinates[1].index(y1)][coordinates[0].index(x1)]
							board[coordinates[1].index(y1)][coordinates[0].index(x1)] = "  "
							space = False
						elif (board[coordinates[1].index(y2)][coordinates[0].index(x2)])[1] == "2":  # Check if adjacent location tile occupied by enemy piece
							scorer(x2, y2, alt)
							print("\n" + piece_class1 + "\'s " + "Bishop" + " captured " + piece_class2 + "\'s" + capt_piece + ".")
							board[coordinates[1].index(y2)][coordinates[0].index(x2)] = board[coordinates[1].index(y1)][coordinates[0].index(x1)]
							board[coordinates[1].index(y1)][coordinates[0].index(x1)] = "  "
							space = False

					elif not white_bishop:
						if board[coordinates[1].index(y2)][coordinates[0].index(x2)] == "  ":  # Check if adjacent location tile is empty
							print("\n" + piece_class1 + "\'s " + "Bishop " + "will move from " + x1[0] + y1 + " to " + x2[0] + y2 + ".")
							board[coordinates[1].index(y2)][coordinates[0].index(x2)] = board[coordinates[1].index(y1)][coordinates[0].index(x1)]
							board[coordinates[1].index(y1)][coordinates[0].index(x1)] = "  "
							space = False
						elif (board[coordinates[1].index(y2)][coordinates[0].index(x2)])[1] == "1":  # Check if adjacent location tile occupied by enemy piece
							scorer(x2, y2, alt)
							print("\n" + piece_class1 + "\'s " + "Bishop" + " captured " + piece_class2 + "\'s" + capt_piece + ".")
							board[coordinates[1].index(y2)][coordinates[0].index(x2)] = board[coordinates[1].index(y1)][coordinates[0].index(x1)]
							board[coordinates[1].index(y1)][coordinates[0].index(x1)] = "  "
							space = False

				for i in range((coordinates[1].index(y1) - coordinates[1].index(y2)) - 1):  # Tiles between bishop and target location
					if board[coordinates[1].index(y1) - a][coordinates[0].index(x1) + a] != "  ":  # Collision Checker
						print("\nInvalid Move! Bishops cannot move over other pieces.")
						no_error = False

						space = False
						break
					a += 1

				if space:
					if board[coordinates[1].index(y2)][coordinates[0].index(x2)] != "  ":
						scorer(x2, y2, alt)
						print("\n" + piece_class1 + "\'s " + "Bishop" + " captured " + piece_class2 + "\'s" + capt_piece + ".")
					elif board[coordinates[1].index(y2)][coordinates[0].index(x2)] == "  ":
						print("\n" + piece_class1 + "\'s " + "Bishop " + "will move from " + x1[0] + y1 + " to " + x2[0] + y2 + ".")
					board[coordinates[1].index(y2)][coordinates[0].index(x2)] = board[coordinates[1].index(y1)][coordinates[0].index(x1)]
					board[coordinates[1].index(y1)][coordinates[0].index(x1)] = "  "

			elif coordinates[1].index(y1) > coordinates[1].index(y2) and coordinates[0].index(x1) > coordinates[0].index(x2):  # North-West Movement of Bishop
				if ((coordinates[1].index(y1) - coordinates[1].index(y2)) - 1) == 0:  # Check if bishop is moving for only 1 space diagonally
					if white_bishop:
						if board[coordinates[1].index(y2)][coordinates[0].index(x2)] == "  ":  # Check if adjacent location tile is empty
							print("\n" + piece_class1 + "\'s " + "Bishop " + "will move from " + x1[0] + y1 + " to " + x2[0] + y2 + ".")
							board[coordinates[1].index(y2)][coordinates[0].index(x2)] = board[coordinates[1].index(y1)][coordinates[0].index(x1)]
							board[coordinates[1].index(y1)][coordinates[0].index(x1)] = "  "
							space = False
						elif (board[coordinates[1].index(y2)][coordinates[0].index(x2)])[1] == "2":  # Check if adjacent location tile occupied by enemy piece
							scorer(x2, y2, alt)
							print("\n" + piece_class1 + "\'s " + "Bishop" + " captured " + piece_class2 + "\'s" + capt_piece + ".")
							board[coordinates[1].index(y2)][coordinates[0].index(x2)] = board[coordinates[1].index(y1)][coordinates[0].index(x1)]
							board[coordinates[1].index(y1)][coordinates[0].index(x1)] = "  "
							space = False

					elif not white_bishop:
						if not checked:
							if board[coordinates[1].index(y2)][coordinates[0].index(x2)] == "  ":  # Check if adjacent location tile is empty
								print("\n" + piece_class1 + "\'s " + "Bishop " + "will move from " + x1[0] + y1 + " to " + x2[0] + y2 + ".")
								board[coordinates[1].index(y2)][coordinates[0].index(x2)] = board[coordinates[1].index(y1)][coordinates[0].index(x1)]
								board[coordinates[1].index(y1)][coordinates[0].index(x1)] = "  "
								space = False
							elif (board[coordinates[1].index(y2)][coordinates[0].index(x2)])[1] == "1":  # Check if adjacent location tile occupied by enemy piece
								scorer(x2, y2, alt)
								print("\n" + piece_class1 + "\'s " + "Bishop" + " captured " + piece_class2 + "\'s" + capt_piece + ".")
								board[coordinates[1].index(y2)][coordinates[0].index(x2)] = board[coordinates[1].index(y1)][coordinates[0].index(x1)]
								board[coordinates[1].index(y1)][coordinates[0].index(x1)] = "  "
								space = False

				for i in range((coordinates[1].index(y1) - coordinates[1].index(y2)) - 1):  # Tiles between bishop and target location
					if board[coordinates[1].index(y1) - a][coordinates[0].index(x1) - a] != "  ":  # Collision Checker
						print("\nInvalid Move! Bishops cannot move over other pieces.")
						no_error = False
						space = False
						break
					a += 1

				if space:
					if board[coordinates[1].index(y2)][coordinates[0].index(x2)] != "  ":
						scorer(x2, y2, alt)
						print("\n" + piece_class1 + "\'s " + "Bishop" + " captured " + piece_class2 + "\'s" + capt_piece + ".")
					elif board[coordinates[1].index(y2)][coordinates[0].index(x2)] == "  ":
						if not checked:
							print("\n" + piece_class1 + "\'s " + "Bishop " + "will move from " + x1[0] + y1 + " to " + x2[0] + y2 + ".")
						board[coordinates[1].index(y2)][coordinates[0].index(x2)] = board[coordinates[1].index(y1)][coordinates[0].index(x1)]
						board[coordinates[1].index(y1)][coordinates[0].index(x1)] = "  "

			elif coordinates[1].index(y1) < coordinates[1].index(y2) and coordinates[0].index(x1) > coordinates[0].index(x2):  # South-West Movement of Bishop
				if ((coordinates[1].index(y2) - coordinates[1].index(y1)) - 1) == 0:  # Check if bishop is moving for only 1 space diagonally
					if white_bishop:
						if board[coordinates[1].index(y2)][coordinates[0].index(x2)] == "  ":  # Check if adjacent location tile is empty
							print("\n" + piece_class1 + "\'s " + "Bishop " + "will move from " + x1[0] + y1 + " to " + x2[0] + y2 + ".")
							board[coordinates[1].index(y2)][coordinates[0].index(x2)] = board[coordinates[1].index(y1)][coordinates[0].index(x1)]
							board[coordinates[1].index(y1)][coordinates[0].index(x1)] = "  "
							space = False
						elif (board[coordinates[1].index(y2)][coordinates[0].index(x2)])[1] == "2":  # Check if adjacent location tile occupied by enemy piece
							scorer(x2, y2, alt)
							print("\n" + piece_class1 + "\'s " + "Bishop" + " captured " + piece_class2 + "\'s" + capt_piece + ".")
							board[coordinates[1].index(y2)][coordinates[0].index(x2)] = board[coordinates[1].index(y1)][coordinates[0].index(x1)]
							board[coordinates[1].index(y1)][coordinates[0].index(x1)] = "  "
							space = False

					elif not white_bishop:
						if board[coordinates[1].index(y2)][coordinates[0].index(x2)] == "  ":  # Check if adjacent location tile is empty
							print("\n" + piece_class1 + "\'s " + "Bishop " + "will move from " + x1[0] + y1 + " to " + x2[0] + y2 + ".")
							board[coordinates[1].index(y2)][coordinates[0].index(x2)] = board[coordinates[1].index(y1)][coordinates[0].index(x1)]
							board[coordinates[1].index(y1)][coordinates[0].index(x1)] = "  "
							space = False
						elif (board[coordinates[1].index(y2)][coordinates[0].index(x2)])[1] == "1":  # Check if adjacent location tile occupied by enemy piece
							scorer(x2, y2, alt)
							print("\n" + piece_class1 + "\'s " + "Bishop" + " captured " + piece_class2 + "\'s" + capt_piece + ".")
							board[coordinates[1].index(y2)][coordinates[0].index(x2)] = board[coordinates[1].index(y1)][coordinates[0].index(x1)]
							board[coordinates[1].index(y1)][coordinates[0].index(x1)] = "  "
							space = False

				for i in range((coordinates[1].index(y2) - coordinates[1].index(y1)) - 1):  # Tiles between bishop and target location
					if board[coordinates[1].index(y1) + a][coordinates[0].index(x1) - a] != "  ":  # Collision Checker
						print("\nInvalid Move! Bishops cannot move over other pieces.")
						no_error = False
						space = False
						break
					a += 1

				if space:
					if board[coordinates[1].index(y2)][coordinates[0].index(x2)] != "  ":
						scorer(x2, y2, alt)
						print("\n" + piece_class1 + "\'s " + "Bishop" + " captured " + piece_class2 + "\'s" + capt_piece + ".")
					elif board[coordinates[1].index(y2)][coordinates[0].index(x2)] == "  ":
						print("\n" + piece_class1 + "\'s " + "Bishop " + "will move from " + x1[0] + y1 + " to " + x2[0] + y2 + ".")
					board[coordinates[1].index(y2)][coordinates[0].index(x2)] = board[coordinates[1].index(y1)][coordinates[0].index(x1)]
					board[coordinates[1].index(y1)][coordinates[0].index(x1)] = "  "

			elif coordinates[1].index(y1) < coordinates[1].index(y2) and coordinates[0].index(x1) < coordinates[0].index(x2):  # South-East Movement of Bishop
				if ((coordinates[1].index(y2) - coordinates[1].index(y1)) - 1) == 0:  # Check if bishop is moving for only 1 space diagonally
					if white_bishop:
						if board[coordinates[1].index(y2)][coordinates[0].index(x2)] == "  ":  # Check if adjacent location tile is empty
							print("\n" + piece_class1 + "\'s " + "Bishop " + "will move from " + x1[0] + y1 + " to " + x2[0] + y2 + ".")
							board[coordinates[1].index(y2)][coordinates[0].index(x2)] = board[coordinates[1].index(y1)][coordinates[0].index(x1)]
							board[coordinates[1].index(y1)][coordinates[0].index(x1)] = "  "
							space = False
						elif (board[coordinates[1].index(y2)][coordinates[0].index(x2)])[1] == "2":  # Check if adjacent location tile occupied by enemy piece
							scorer(x2, y2, alt)
							print("\n" + piece_class1 + "\'s " + "Bishop" + " captured " + piece_class2 + "\'s" + capt_piece + ".")
							board[coordinates[1].index(y2)][coordinates[0].index(x2)] = board[coordinates[1].index(y1)][coordinates[0].index(x1)]
							board[coordinates[1].index(y1)][coordinates[0].index(x1)] = "  "
							space = False

					elif not white_bishop:
						if board[coordinates[1].index(y2)][coordinates[0].index(x2)] == "  ":  # Check if adjacent location tile is empty
							print("\n" + piece_class1 + "\'s " + "Bishop " + "will move from " + x1[0] + y1 + " to " + x2[0] + y2 + ".")
							board[coordinates[1].index(y2)][coordinates[0].index(x2)] = board[coordinates[1].index(y1)][coordinates[0].index(x1)]
							board[coordinates[1].index(y1)][coordinates[0].index(x1)] = "  "
							space = False
						elif (board[coordinates[1].index(y2)][coordinates[0].index(x2)])[1] == "1":  # Check if adjacent location tile occupied by enemy piece
							scorer(x2, y2, alt)
							print("\n" + piece_class1 + "\'s " + "Bishop" + " captured " + piece_class2 + "\'s" + capt_piece + ".")
							board[coordinates[1].index(y2)][coordinates[0].index(x2)] = board[coordinates[1].index(y1)][coordinates[0].index(x1)]
							board[coordinates[1].index(y1)][coordinates[0].index(x1)] = "  "
							space = False

				for i in range((coordinates[1].index(y2) - coordinates[1].index(y1)) - 1):  # Tiles between bishop and target location
					if board[coordinates[1].index(y1) + a][coordinates[0].index(x1) + a] != "  ":  # Collision Checker
						print("\nInvalid Move! Bishops cannot move over other pieces.")
						no_error = False
						space = False
						break
					a += 1

				if space:
					if board[coordinates[1].index(y2)][coordinates[0].index(x2)] != "  ":
						scorer(x2, y2, alt)
						print("\n" + piece_class1 + "\'s " + "Bishop" + " captured " + piece_class2 + "\'s" + capt_piece + ".")
					elif board[coordinates[1].index(y2)][coordinates[0].index(x2)] == "  ":
						print("\n" + piece_class1 + "\'s " + "Bishop " + "will move from " + x1[0] + y1 + " to " + x2[0] + y2 + ".")
					board[coordinates[1].index(y2)][coordinates[0].index(x2)] = board[coordinates[1].index(y1)][coordinates[0].index(x1)]
					board[coordinates[1].index(y1)][coordinates[0].index(x1)] = "  "

		else:
			print("\nInvalid Move! Bishops can only move diagonally.")
			no_error = False


def rook(x1, y1, x2, y2, white_rook, alt):
	global no_error
	global piece_class1
	global piece_class2
	global capt_piece
	global dec

	space = True
	a = 1

	virtual_move(x1, y1, x2, y2, alt)  # Assumes that the move is executed then determine if king is still checked or not

	if not checked:

		# determine which player is making the move
		if (board[coordinates[1].index(y1)][coordinates[0].index(x1)])[1] == "1":
			piece_class1 = "Player 1"
		elif (board[coordinates[1].index(y1)][coordinates[0].index(x1)])[1] == "2":
			piece_class1 = "Player 2"

		if (board[coordinates[1].index(y2)][coordinates[0].index(x2)])[1] == "1":
			piece_class2 = "Player 1"
		elif (board[coordinates[1].index(y2)][coordinates[0].index(x2)])[1] == "2":
			piece_class2 = "Player 2"

		# Determine which piece is captured
		if (board[coordinates[1].index(y2)][coordinates[0].index(x2)])[0] == "P":
			capt_piece = " Pawn"
		elif (board[coordinates[1].index(y2)][coordinates[0].index(x2)])[0] == "R":
			capt_piece = " Rook"
		elif (board[coordinates[1].index(y2)][coordinates[0].index(x2)])[0] == "B":
			capt_piece = " Bishop"
		elif (board[coordinates[1].index(y2)][coordinates[0].index(x2)])[0] == "N":
			capt_piece = " Knight"
		elif (board[coordinates[1].index(y2)][coordinates[0].index(x2)])[0] == "Q":
			capt_piece = " Queen"
		elif (board[coordinates[1].index(y2)][coordinates[0].index(x2)])[0] == "K":
			capt_piece = " King"
			
		if capt_piece == " King":
			dec = True

		if white_rook:
			if (board[coordinates[1].index(y2)][coordinates[0].index(x2)])[1] == "1":
				print("\nInvalid Move! Rooks cannot capture allied piece.")
				no_error = False
				return
		elif not white_rook:
			if (board[coordinates[1].index(y2)][coordinates[0].index(x2)])[1] == "2":
				print("\nInvalid Move! Rooks cannot capture allied piece.")
				no_error = False
				return

		if (x1 == x2) or (y1 == y2):  # Check if move is horizontal in nature
			if (x1 == x2) and (coordinates[1].index(y1) > coordinates[1].index(y2)):  # Northward movement of Rook
				if (coordinates[1].index(y1) - coordinates[1].index(y2)) - 1 == 0:  # Check if Rook is moving 1 space northward
					if white_rook:
						if board[coordinates[1].index(y2)][coordinates[0].index(x2)] == "  ":  # Check if adjacent location tile is empty
							print("\n" + piece_class1 + "\'s " + "Rook " + "will move from " + x1[0] + y1 + " to " + x2[0] + y2 + ".")
							board[coordinates[1].index(y2)][coordinates[0].index(x2)] = board[coordinates[1].index(y1)][coordinates[0].index(x1)]
							board[coordinates[1].index(y1)][coordinates[0].index(x1)] = "  "
							space = False
						elif (board[coordinates[1].index(y2)][coordinates[0].index(x2)])[1] == "2":  # Check if adjacent location tile occupied by enemy piece
							scorer(x2, y2, alt)
							print("\n" + piece_class1 + "\'s " + "Rook" + " captured " + piece_class2 + "\'s" + capt_piece + ".")
							board[coordinates[1].index(y2)][coordinates[0].index(x2)] = board[coordinates[1].index(y1)][coordinates[0].index(x1)]
							board[coordinates[1].index(y1)][coordinates[0].index(x1)] = "  "
							space = False

					elif not white_rook:
						if board[coordinates[1].index(y2)][coordinates[0].index(x2)] == "  ":  # Check if adjacent location tile is empty
							print("\n" + piece_class1 + "\'s " + "Rook " + "will move from " + x1[0] + y1 + " to " + x2[0] + y2 + ".")
							board[coordinates[1].index(y2)][coordinates[0].index(x2)] = board[coordinates[1].index(y1)][coordinates[0].index(x1)]
							board[coordinates[1].index(y1)][coordinates[0].index(x1)] = "  "
							space = False
						elif (board[coordinates[1].index(y2)][coordinates[0].index(x2)])[1] == "1":  # Check if adjacent location tile occupied by enemy piece
							scorer(x2, y2, alt)
							print("\n" + piece_class1 + "\'s " + "Rook" + " captured " + piece_class2 + "\'s" + capt_piece + ".")
							board[coordinates[1].index(y2)][coordinates[0].index(x2)] = board[coordinates[1].index(y1)][coordinates[0].index(x1)]
							board[coordinates[1].index(y1)][coordinates[0].index(x1)] = "  "
							space = False

				for i in range((coordinates[1].index(y1) - coordinates[1].index(y2)) - 1):  # Tiles between rook and target location
					if board[coordinates[1].index(y1) - a][coordinates[0].index(x1)] != "  ":  # Collision Checker
						print("\nInvalid Move! Rooks cannot move over other pieces.")
						no_error = False
						space = False
						break
					a += 1

				if space:
					if board[coordinates[1].index(y2)][coordinates[0].index(x2)] != "  ":
						scorer(x2, y2, alt)
						print("\n" + piece_class1 + "\'s " + "Rook" + " captured " + piece_class2 + "\'s" + capt_piece + ".")
					elif board[coordinates[1].index(y2)][coordinates[0].index(x2)] == "  ":
						print("\n" + piece_class1 + "\'s " + "Rook " + "will move from " + x1[0] + y1 + " to " + x2[0] + y2 + ".")
					board[coordinates[1].index(y2)][coordinates[0].index(x2)] = board[coordinates[1].index(y1)][coordinates[0].index(x1)]
					board[coordinates[1].index(y1)][coordinates[0].index(x1)] = "  "

			elif (x1 == x2) and (coordinates[1].index(y1) < coordinates[1].index(y2)):  # Southward movement of Rook
				if (coordinates[1].index(y2) - coordinates[1].index(y1)) - 1 == 0:  # Check if Rook is moving 1 space northward
					if white_rook:
						if board[coordinates[1].index(y2)][coordinates[0].index(x2)] == "  ":  # Check if adjacent location tile is empty
							print("\n" + piece_class1 + "\'s " + "Rook " + "will move from " + x1[0] + y1 + " to " + x2[0] + y2 + ".")
							board[coordinates[1].index(y2)][coordinates[0].index(x2)] = board[coordinates[1].index(y1)][coordinates[0].index(x1)]
							board[coordinates[1].index(y1)][coordinates[0].index(x1)] = "  "
							space = False
						elif (board[coordinates[1].index(y2)][coordinates[0].index(x2)])[1] == "2":  # Check if adjacent location tile occupied by enemy piece
							scorer(x2, y2, alt)
							print("\n" + piece_class1 + "\'s " + "Rook" + " captured " + piece_class2 + "\'s" + capt_piece + ".")
							board[coordinates[1].index(y2)][coordinates[0].index(x2)] = board[coordinates[1].index(y1)][coordinates[0].index(x1)]
							board[coordinates[1].index(y1)][coordinates[0].index(x1)] = "  "
							space = False

					elif not white_rook:
						if board[coordinates[1].index(y2)][coordinates[0].index(x2)] == "  ":  # Check if adjacent location tile is empty
							print("\n" + piece_class1 + "\'s " + "Rook " + "will move from " + x1[0] + y1 + " to " + x2[0] + y2 + ".")
							board[coordinates[1].index(y2)][coordinates[0].index(x2)] = board[coordinates[1].index(y1)][coordinates[0].index(x1)]
							board[coordinates[1].index(y1)][coordinates[0].index(x1)] = "  "
							space = False
						elif (board[coordinates[1].index(y2)][coordinates[0].index(x2)])[1] == "1":  # Check if adjacent location tile occupied by enemy piece
							scorer(x2, y2, alt)
							print("\n" + piece_class1 + "\'s " + "Rook" + " captured " + piece_class2 + "\'s" + capt_piece + ".")
							board[coordinates[1].index(y2)][coordinates[0].index(x2)] = board[coordinates[1].index(y1)][coordinates[0].index(x1)]
							board[coordinates[1].index(y1)][coordinates[0].index(x1)] = "  "
							space = False

				for i in range((coordinates[1].index(y1) - coordinates[1].index(y2)) - 1):  # Tiles between rook and target location
					if board[coordinates[1].index(y1) - a][coordinates[0].index(x1)] != "  ":  # Collision Checker
						print("\nInvalid Move! Rooks cannot move over other pieces.")
						no_error = False
						space = False
						break
					a += 1

				if space:
					if board[coordinates[1].index(y2)][coordinates[0].index(x2)] != "  ":
						scorer(x2, y2, alt)
						print("\n" + piece_class1 + "\'s " + "Rook" + " captured " + piece_class2 + "\'s" + capt_piece + ".")
					elif board[coordinates[1].index(y2)][coordinates[0].index(x2)] == "  ":
						print("\n" + piece_class1 + "\'s " + "Rook " + "will move from " + x1[0] + y1 + " to " + x2[0] + y2 + ".")
					board[coordinates[1].index(y2)][coordinates[0].index(x2)] = board[coordinates[1].index(y1)][coordinates[0].index(x1)]
					board[coordinates[1].index(y1)][coordinates[0].index(x1)] = "  "

			elif (y1 == y2) and (coordinates[0].index(x1) < coordinates[0].index(x2)):  # Eastward Movement of Rook
				if (coordinates[0].index(x2) - coordinates[0].index(x1)) - 1 == 0:  # Check if Rook is moving 1 space eastward
					if white_rook:
						if board[coordinates[1].index(y2)][coordinates[0].index(x2)] == "  ":  # Check if adjacent location tile is empty
							print("\n" + piece_class1 + "\'s " + "Rook " + "will move from " + x1[0] + y1 + " to " + x2[0] + y2 + ".")
							board[coordinates[1].index(y2)][coordinates[0].index(x2)] = board[coordinates[1].index(y1)][coordinates[0].index(x1)]
							board[coordinates[1].index(y1)][coordinates[0].index(x1)] = "  "
							space = False
						elif (board[coordinates[1].index(y2)][coordinates[0].index(x2)])[1] == "2":  # Check if adjacent location tile occupied by enemy piece
							scorer(x2, y2, alt)
							print("\n" + piece_class1 + "\'s " + "Rook" + " captured " + piece_class2 + "\'s" + capt_piece + ".")
							board[coordinates[1].index(y2)][coordinates[0].index(x2)] = board[coordinates[1].index(y1)][coordinates[0].index(x1)]
							board[coordinates[1].index(y1)][coordinates[0].index(x1)] = "  "
							space = False

					elif not white_rook:
						if board[coordinates[1].index(y2)][coordinates[0].index(x2)] == "  ":  # Check if adjacent location tile is empty
							print("\n" + piece_class1 + "\'s " + "Rook " + "will move from " + x1[0] + y1 + " to " + x2[0] + y2 + ".")
							board[coordinates[1].index(y2)][coordinates[0].index(x2)] = board[coordinates[1].index(y1)][coordinates[0].index(x1)]
							board[coordinates[1].index(y1)][coordinates[0].index(x1)] = "  "
							space = False
						elif (board[coordinates[1].index(y2)][coordinates[0].index(x2)])[1] == "1":  # Check if adjacent location tile occupied by enemy piece
							scorer(x2, y2, alt)
							print("\n" + piece_class1 + "\'s " + "Rook" + " captured " + piece_class2 + "\'s" + capt_piece + ".")
							board[coordinates[1].index(y2)][coordinates[0].index(x2)] = board[coordinates[1].index(y1)][coordinates[0].index(x1)]
							board[coordinates[1].index(y1)][coordinates[0].index(x1)] = "  "
							space = False

				for i in range((coordinates[0].index(x2) - coordinates[0].index(x1)) - 1):  # Tiles between rook and target location
					if board[coordinates[1].index(y1)][coordinates[0].index(x1) + a] != "  ":  # Collision Checker
						print("\nInvalid Move! Rooks cannot move over other pieces.")
						no_error = False
						space = False
						break
					a += 1

				if space:
					if board[coordinates[1].index(y2)][coordinates[0].index(x2)] != "  ":
						scorer(x2, y2, alt)
						print("\n" + piece_class1 + "\'s " + "Rook" + " captured " + piece_class2 + "\'s" + capt_piece + ".")
					elif board[coordinates[1].index(y2)][coordinates[0].index(x2)] == "  ":
						print("\n" + piece_class1 + "\'s " + "Rook " + "will move from " + x1[0] + y1 + " to " + x2[0] + y2 + ".")
					board[coordinates[1].index(y2)][coordinates[0].index(x2)] = board[coordinates[1].index(y1)][coordinates[0].index(x1)]
					board[coordinates[1].index(y1)][coordinates[0].index(x1)] = "  "

			elif (y1 == y2) and (coordinates[0].index(x1) > coordinates[0].index(x2)):  # Westward Movement of Rook
				if (coordinates[0].index(x1) - coordinates[0].index(x2)) - 1 == 0:  # Check if Rook is moving 1 space eastward
					if white_rook:
						if board[coordinates[1].index(y2)][coordinates[0].index(x2)] == "  ":  # Check if adjacent location tile is empty
							print("\n" + piece_class1 + "\'s " + "Rook " + "will move from " + x1[0] + y1 + " to " + x2[0] + y2 + ".")
							board[coordinates[1].index(y2)][coordinates[0].index(x2)] = board[coordinates[1].index(y1)][coordinates[0].index(x1)]
							board[coordinates[1].index(y1)][coordinates[0].index(x1)] = "  "
							space = False
						elif (board[coordinates[1].index(y2)][coordinates[0].index(x2)])[1] == "2":  # Check if adjacent location tile occupied by enemy piece
							scorer(x2, y2, alt)
							print("\n" + piece_class1 + "\'s " + "Rook" + " captured " + piece_class2 + "\'s" + capt_piece + ".")
							board[coordinates[1].index(y2)][coordinates[0].index(x2)] = board[coordinates[1].index(y1)][coordinates[0].index(x1)]
							board[coordinates[1].index(y1)][coordinates[0].index(x1)] = "  "
							space = False

					elif not white_rook:
						if board[coordinates[1].index(y2)][coordinates[0].index(x2)] == "  ":  # Check if adjacent location tile is empty
							print("\n" + piece_class1 + "\'s " + "Rook " + "will move from " + x1[0] + y1 + " to " + x2[0] + y2 + ".")
							board[coordinates[1].index(y2)][coordinates[0].index(x2)] = board[coordinates[1].index(y1)][coordinates[0].index(x1)]
							board[coordinates[1].index(y1)][coordinates[0].index(x1)] = "  "
							space = False
						elif (board[coordinates[1].index(y2)][coordinates[0].index(x2)])[1] == "1":  # Check if adjacent location tile occupied by enemy piece
							scorer(x2, y2, alt)
							print("\n" + piece_class1 + "\'s " + "Rook" + " captured " + piece_class2 + "\'s" + capt_piece + ".")
							board[coordinates[1].index(y2)][coordinates[0].index(x2)] = board[coordinates[1].index(y1)][coordinates[0].index(x1)]
							board[coordinates[1].index(y1)][coordinates[0].index(x1)] = "  "
							space = False

				for i in range((coordinates[0].index(x1) - coordinates[0].index(x2)) - 1):  # Tiles between rook and target location
					if board[coordinates[1].index(y1)][coordinates[0].index(x1) - a] != "  ":  # Collision Checker
						print("\nInvalid Move! Rooks cannot move over other pieces.")
						no_error = False
						space = False
						break
					a += 1

				if space:
					if board[coordinates[1].index(y2)][coordinates[0].index(x2)] != "  ":
						scorer(x2, y2, alt)
						print("\n" + piece_class1 + "\'s " + "Rook" + " captured " + piece_class2 + "\'s" + capt_piece + ".")
					elif board[coordinates[1].index(y2)][coordinates[0].index(x2)] == "  ":
						print("\n" + piece_class1 + "\'s " + "Rook " + "will move from " + x1[0] + y1 + " to " + x2[0] + y2 + ".")
					board[coordinates[1].index(y2)][coordinates[0].index(x2)] = board[coordinates[1].index(y1)][coordinates[0].index(x1)]
					board[coordinates[1].index(y1)][coordinates[0].index(x1)] = "  "

		else:
			print("\nInvalid Move! Rooks can only move vertically or horizontally.")
			no_error = False


def knight(x1, y1, x2, y2, white_knight, alt):
	global no_error
	global piece_class1
	global piece_class2
	global capt_piece
	global dec

	# determine which player is making the move
	if (board[coordinates[1].index(y1)][coordinates[0].index(x1)])[1] == "1":
		piece_class1 = "Player 1"
	elif (board[coordinates[1].index(y1)][coordinates[0].index(x1)])[1] == "2":
		piece_class1 = "Player 2"

	if (board[coordinates[1].index(y2)][coordinates[0].index(x2)])[1] == "1":
		piece_class2 = "Player 1"
	elif (board[coordinates[1].index(y2)][coordinates[0].index(x2)])[1] == "2":
		piece_class2 = "Player 2"

	# Determine which piece is captured
	if (board[coordinates[1].index(y2)][coordinates[0].index(x2)])[0] == "P":
		capt_piece = " Pawn"
	elif (board[coordinates[1].index(y2)][coordinates[0].index(x2)])[0] == "R":
		capt_piece = " Rook"
	elif (board[coordinates[1].index(y2)][coordinates[0].index(x2)])[0] == "B":
		capt_piece = " Bishop"
	elif (board[coordinates[1].index(y2)][coordinates[0].index(x2)])[0] == "N":
		capt_piece = " Knight"
	elif (board[coordinates[1].index(y2)][coordinates[0].index(x2)])[0] == "Q":
		capt_piece = " Queen"
	elif (board[coordinates[1].index(y2)][coordinates[0].index(x2)])[0] == "K":
		capt_piece = " King"
	
	if capt_piece == " King":
		dec = True

	if white_knight:
		if (board[coordinates[1].index(y2)][coordinates[0].index(x2)])[1] == "1":
			print("\nInvalid Move! Knights cannot capture allied piece.")
			no_error = False
			return
	elif not white_knight:
		if (board[coordinates[1].index(y2)][coordinates[0].index(x2)])[1] == "2":
			print("\nInvalid Move! Knights cannot capture allied piece.")
			no_error = False
			return

	virtual_move(x1, y1, x2, y2, alt)  # Assumes that the move is executed then determine if king is still checked or not

	if not checked:

		if coordinates[0].index(x1) + 1 == coordinates[0].index(x2) and coordinates[1].index(y1) - 2 == coordinates[1].index(y2):  # If Knight is moving North-North-East
			if board[coordinates[1].index(y2)][coordinates[0].index(x2)] == "  ":  # Check if destination is unoccupied
				print("\n" + piece_class1 + "\'s " + "Knight " + "will move from " + x1[0] + y1 + " to " + x2[0] + y2 + ".")
				board[coordinates[1].index(y2)][coordinates[0].index(x2)] = board[coordinates[1].index(y1)][coordinates[0].index(x1)]
				board[coordinates[1].index(y1)][coordinates[0].index(x1)] = "  "
			else:
				scorer(x2, y2, alt)
				print("\n" + piece_class1 + "\'s " + "Knight" + " captured " + piece_class2 + "\'s" + capt_piece + ".")
				board[coordinates[1].index(y2)][coordinates[0].index(x2)] = board[coordinates[1].index(y1)][coordinates[0].index(x1)]
				board[coordinates[1].index(y1)][coordinates[0].index(x1)] = "  "

		elif coordinates[0].index(x1) + 2 == coordinates[0].index(x2) and coordinates[1].index(y1) - 1 == coordinates[1].index(y2):  # If Knight is moving East-North-East
			if board[coordinates[1].index(y2)][coordinates[0].index(x2)] == "  ":  # Check if destination is unoccupied
				print("\n" + piece_class1 + "\'s " + "Knight " + "will move from " + x1[0] + y1 + " to " + x2[0] + y2 + ".")
				board[coordinates[1].index(y2)][coordinates[0].index(x2)] = board[coordinates[1].index(y1)][coordinates[0].index(x1)]
				board[coordinates[1].index(y1)][coordinates[0].index(x1)] = "  "
			else:
				scorer(x2, y2, alt)
				print("\n" + piece_class1 + "\'s " + "Knight" + " captured " + piece_class2 + "\'s" + capt_piece + ".")
				board[coordinates[1].index(y2)][coordinates[0].index(x2)] = board[coordinates[1].index(y1)][coordinates[0].index(x1)]
				board[coordinates[1].index(y1)][coordinates[0].index(x1)] = "  "

		elif coordinates[0].index(x1) - 1 == coordinates[0].index(x2) and coordinates[1].index(y1) - 2 == coordinates[1].index(y2):  # If Knight is moving North-North-West
			if board[coordinates[1].index(y2)][coordinates[0].index(x2)] == "  ":  # Check if destination is unoccupied
				print("\n" + piece_class1 + "\'s " + "Knight " + "will move from " + x1[0] + y1 + " to " + x2[0] + y2 + ".")
				board[coordinates[1].index(y2)][coordinates[0].index(x2)] = board[coordinates[1].index(y1)][coordinates[0].index(x1)]
				board[coordinates[1].index(y1)][coordinates[0].index(x1)] = "  "
			else:
				scorer(x2, y2, alt)
				print("\n" + piece_class1 + "\'s " + "Knight" + " captured " + piece_class2 + "\'s" + capt_piece + ".")
				board[coordinates[1].index(y2)][coordinates[0].index(x2)] = board[coordinates[1].index(y1)][coordinates[0].index(x1)]
				board[coordinates[1].index(y1)][coordinates[0].index(x1)] = "  "

		elif coordinates[0].index(x1) - 2 == coordinates[0].index(x2) and coordinates[1].index(y1) - 1 == coordinates[1].index(y2):  # If Knight is moving West-North-West
			if board[coordinates[1].index(y2)][coordinates[0].index(x2)] == "  ":  # Check if destination is unoccupied
				print("\n" + piece_class1 + "\'s " + "Knight " + "will move from " + x1[0] + y1 + " to " + x2[0] + y2 + ".")
				board[coordinates[1].index(y2)][coordinates[0].index(x2)] = board[coordinates[1].index(y1)][coordinates[0].index(x1)]
				board[coordinates[1].index(y1)][coordinates[0].index(x1)] = "  "
			else:
				scorer(x2, y2, alt)
				print("\n" + piece_class1 + "\'s " + "Knight" + " captured " + piece_class2 + "\'s" + capt_piece + ".")
				board[coordinates[1].index(y2)][coordinates[0].index(x2)] = board[coordinates[1].index(y1)][coordinates[0].index(x1)]
				board[coordinates[1].index(y1)][coordinates[0].index(x1)] = "  "

		elif coordinates[0].index(x1) + 1 == coordinates[0].index(x2) and coordinates[1].index(y1) + 2 == coordinates[1].index(y2):  # If Knight is moving South-South-East
			if board[coordinates[1].index(y2)][coordinates[0].index(x2)] == "  ":  # Check if destination is unoccupied
				print("\n" + piece_class1 + "\'s " + "Knight " + "will move from " + x1[0] + y1 + " to " + x2[0] + y2 + ".")
				board[coordinates[1].index(y2)][coordinates[0].index(x2)] = board[coordinates[1].index(y1)][coordinates[0].index(x1)]
				board[coordinates[1].index(y1)][coordinates[0].index(x1)] = "  "
			else:
				scorer(x2, y2, alt)
				print("\n" + piece_class1 + "\'s " + "Knight" + " captured " + piece_class2 + "\'s" + capt_piece + ".")
				board[coordinates[1].index(y2)][coordinates[0].index(x2)] = board[coordinates[1].index(y1)][coordinates[0].index(x1)]
				board[coordinates[1].index(y1)][coordinates[0].index(x1)] = "  "

		elif coordinates[0].index(x1) + 2 == coordinates[0].index(x2) and coordinates[1].index(y1) + 1 == coordinates[1].index(y2):  # If Knight is moving East-South-East
			if board[coordinates[1].index(y2)][coordinates[0].index(x2)] == "  ":  # Check if destination is unoccupied
				print("\n" + piece_class1 + "\'s " + "Knight " + "will move from " + x1[0] + y1 + " to " + x2[0] + y2 + ".")
				board[coordinates[1].index(y2)][coordinates[0].index(x2)] = board[coordinates[1].index(y1)][coordinates[0].index(x1)]
				board[coordinates[1].index(y1)][coordinates[0].index(x1)] = "  "
			else:
				scorer(x2, y2, alt)
				print("\n" + piece_class1 + "\'s " + "Knight" + " captured " + piece_class2 + "\'s" + capt_piece + ".")
				board[coordinates[1].index(y2)][coordinates[0].index(x2)] = board[coordinates[1].index(y1)][coordinates[0].index(x1)]
				board[coordinates[1].index(y1)][coordinates[0].index(x1)] = "  "

		elif coordinates[0].index(x1) - 1 == coordinates[0].index(x2) and coordinates[1].index(y1) + 2 == coordinates[1].index(y2):  # If Knight is moving South-South-West
			if board[coordinates[1].index(y2)][coordinates[0].index(x2)] == "  ":  # Check if destination is unoccupied
				print("\n" + piece_class1 + "\'s " + "Knight " + "will move from " + x1[0] + y1 + " to " + x2[0] + y2 + ".")
				board[coordinates[1].index(y2)][coordinates[0].index(x2)] = board[coordinates[1].index(y1)][coordinates[0].index(x1)]
				board[coordinates[1].index(y1)][coordinates[0].index(x1)] = "  "
			else:
				scorer(x2, y2, alt)
				print("\n" + piece_class1 + "\'s " + "Knight" + " captured " + piece_class2 + "\'s" + capt_piece + ".")
				board[coordinates[1].index(y2)][coordinates[0].index(x2)] = board[coordinates[1].index(y1)][coordinates[0].index(x1)]
				board[coordinates[1].index(y1)][coordinates[0].index(x1)] = "  "

		elif coordinates[0].index(x1) - 2 == coordinates[0].index(x2) and coordinates[1].index(y1) + 1 == coordinates[1].index(y2):  # If Knight is moving West-South-West
			if board[coordinates[1].index(y2)][coordinates[0].index(x2)] == "  ":  # Check if destination is unoccupied
				print("\n" + piece_class1 + "\'s " + "Knight " + "will move from " + x1[0] + y1 + " to " + x2[0] + y2 + ".")
				board[coordinates[1].index(y2)][coordinates[0].index(x2)] = board[coordinates[1].index(y1)][coordinates[0].index(x1)]
				board[coordinates[1].index(y1)][coordinates[0].index(x1)] = "  "
			else:
				scorer(x2, y2, alt)
				print("\n" + piece_class1 + "\'s " + "Knight" + " captured " + piece_class2 + "\'s" + capt_piece + ".")
				board[coordinates[1].index(y2)][coordinates[0].index(x2)] = board[coordinates[1].index(y1)][coordinates[0].index(x1)]
				board[coordinates[1].index(y1)][coordinates[0].index(x1)] = "  "

		else:
			print("\nInvalid Move! Knights cannot move like that.")
			no_error = False


def queen(x1, y1, x2, y2, white_queen, alt):
	global no_error
	global piece_class1
	global piece_class2
	global capt_piece
	global dec

	space = True
	a = 1

	# determine which player is making the move
	if (board[coordinates[1].index(y1)][coordinates[0].index(x1)])[1] == "1":
		piece_class1 = "Player 1"
	elif (board[coordinates[1].index(y1)][coordinates[0].index(x1)])[1] == "2":
		piece_class1 = "Player 2"

	if (board[coordinates[1].index(y2)][coordinates[0].index(x2)])[1] == "1":
		piece_class2 = "Player 1"
	elif (board[coordinates[1].index(y2)][coordinates[0].index(x2)])[1] == "2":
		piece_class2 = "Player 2"

	# Determine which piece is captured
	if (board[coordinates[1].index(y2)][coordinates[0].index(x2)])[0] == "P":
		capt_piece = " Pawn"
	elif (board[coordinates[1].index(y2)][coordinates[0].index(x2)])[0] == "R":
		capt_piece = " Rook"
	elif (board[coordinates[1].index(y2)][coordinates[0].index(x2)])[0] == "B":
		capt_piece = " Bishop"
	elif (board[coordinates[1].index(y2)][coordinates[0].index(x2)])[0] == "N":
		capt_piece = " Knight"
	elif (board[coordinates[1].index(y2)][coordinates[0].index(x2)])[0] == "Q":
		capt_piece = " Queen"
	elif (board[coordinates[1].index(y2)][coordinates[0].index(x2)])[0] == "K":
		capt_piece = " King"
		
	if capt_piece == " King":
		dec = True

	if white_queen:
		if (board[coordinates[1].index(y2)][coordinates[0].index(x2)])[1] == "1":
			print("\nInvalid Move! Queens cannot capture allied piece.")
			no_error = False
			return
	elif not white_queen:
		if (board[coordinates[1].index(y2)][coordinates[0].index(x2)])[1] == "2":
			print("\nInvalid Move! Queens cannot capture allied piece.")
			no_error = False
			return

	virtual_move(x1, y1, x2, y2, alt)  # Assumes that the move is executed then determine if king is still checked or not

	if not checked:

		if (coordinates[0].index(x1) + coordinates[1].index(y1) == coordinates[0].index(x2) + coordinates[1].index(y2)) or (coordinates[0].index(x1) - coordinates[1].index(y1) == coordinates[0].index(x2) - coordinates[1].index(y2)):  # Determine if chosen movement is diagonal in nature
			if coordinates[1].index(y1) > coordinates[1].index(y2) and coordinates[0].index(x1) < coordinates[0].index(x2):  # North-East Movement of Queen
				if ((coordinates[1].index(y1) - coordinates[1].index(y2)) - 1) == 0:  # Check if Queen is moving for only 1 space diagonally
					if white_queen:
						if board[coordinates[1].index(y2)][coordinates[0].index(x2)] == "  ":  # Check if adjacent location tile is empty
							print("\n" + piece_class1 + "\'s " + "Queen " + "will move from " + x1[0] + y1 + " to " + x2[0] + y2 + ".")
							board[coordinates[1].index(y2)][coordinates[0].index(x2)] = board[coordinates[1].index(y1)][coordinates[0].index(x1)]
							board[coordinates[1].index(y1)][coordinates[0].index(x1)] = "  "
							space = False
						elif (board[coordinates[1].index(y2)][coordinates[0].index(x2)])[1] == "2":  # Check if adjacent location tile occupied by enemy piece
							scorer(x2, y2, alt)
							print("\n" + piece_class1 + "\'s " + "Queen" + " captured " + piece_class2 + "\'s" + capt_piece + ".")
							board[coordinates[1].index(y2)][coordinates[0].index(x2)] = board[coordinates[1].index(y1)][coordinates[0].index(x1)]
							board[coordinates[1].index(y1)][coordinates[0].index(x1)] = "  "
							space = False

					elif not white_queen:
						if board[coordinates[1].index(y2)][coordinates[0].index(x2)] == "  ":  # Check if adjacent location tile is empty
							print("\n" + piece_class1 + "\'s " + "Queen " + "will move from " + x1[0] + y1 + " to " + x2[0] + y2 + ".")
							board[coordinates[1].index(y2)][coordinates[0].index(x2)] = board[coordinates[1].index(y1)][coordinates[0].index(x1)]
							board[coordinates[1].index(y1)][coordinates[0].index(x1)] = "  "
							space = False
						elif (board[coordinates[1].index(y2)][coordinates[0].index(x2)])[1] == "1":  # Check if adjacent location tile occupied by enemy piece
							scorer(x2, y2, alt)
							print("\n" + piece_class1 + "\'s " + "Queen" + " captured " + piece_class2 + "\'s" + capt_piece + ".")
							board[coordinates[1].index(y2)][coordinates[0].index(x2)] = board[coordinates[1].index(y1)][coordinates[0].index(x1)]
							board[coordinates[1].index(y1)][coordinates[0].index(x1)] = "  "
							space = False

				for i in range((coordinates[1].index(y1) - coordinates[1].index(y2)) - 1):  # Tiles between queen and target location
					if board[coordinates[1].index(y1) - a][coordinates[0].index(x1) + a] != "  ":  # Collision Checker
						print("\nInvalid Move! Queens cannot move over other pieces.")
						no_error = False

						space = False
						break
					a += 1

				if space:
					if board[coordinates[1].index(y2)][coordinates[0].index(x2)] != "  ":
						scorer(x2, y2, alt)
						print("\n" + piece_class1 + "\'s " + "Queen" + " captured " + piece_class2 + "\'s" + capt_piece + ".")
					elif board[coordinates[1].index(y2)][coordinates[0].index(x2)] == "  ":
						print("\n" + piece_class1 + "\'s " + "Queen " + "will move from " + x1[0] + y1 + " to " + x2[0] + y2 + ".")
					board[coordinates[1].index(y2)][coordinates[0].index(x2)] = board[coordinates[1].index(y1)][coordinates[0].index(x1)]
					board[coordinates[1].index(y1)][coordinates[0].index(x1)] = "  "

			elif coordinates[1].index(y1) > coordinates[1].index(y2) and coordinates[0].index(x1) > coordinates[0].index(x2):  # North-West Movement of Queen
				if ((coordinates[1].index(y1) - coordinates[1].index(y2)) - 1) == 0:  # Check if Queen is moving for only 1 space diagonally
					if white_queen:
						if board[coordinates[1].index(y2)][coordinates[0].index(x2)] == "  ":  # Check if adjacent location tile is empty
							print("\n" + piece_class1 + "\'s " + "Queen " + "will move from " + x1[0] + y1 + " to " + x2[0] + y2 + ".")
							board[coordinates[1].index(y2)][coordinates[0].index(x2)] = board[coordinates[1].index(y1)][coordinates[0].index(x1)]
							board[coordinates[1].index(y1)][coordinates[0].index(x1)] = "  "
							space = False
						elif (board[coordinates[1].index(y2)][coordinates[0].index(x2)])[1] == "2":  # Check if adjacent location tile occupied by enemy piece
							scorer(x2, y2, alt)
							print("\n" + piece_class1 + "\'s " + "Queen" + " captured " + piece_class2 + "\'s" + capt_piece + ".")
							board[coordinates[1].index(y2)][coordinates[0].index(x2)] = board[coordinates[1].index(y1)][coordinates[0].index(x1)]
							board[coordinates[1].index(y1)][coordinates[0].index(x1)] = "  "
							space = False

					elif not white_queen:
						if board[coordinates[1].index(y2)][coordinates[0].index(x2)] == "  ":  # Check if adjacent location tile is empty
							print("\n" + piece_class1 + "\'s " + "Queen " + "will move from " + x1[0] + y1 + " to " + x2[0] + y2 + ".")
							board[coordinates[1].index(y2)][coordinates[0].index(x2)] = board[coordinates[1].index(y1)][coordinates[0].index(x1)]
							board[coordinates[1].index(y1)][coordinates[0].index(x1)] = "  "
							space = False
						elif (board[coordinates[1].index(y2)][coordinates[0].index(x2)])[1] == "1":  # Check if adjacent location tile occupied by enemy piece
							scorer(x2, y2, alt)
							print("\n" + piece_class1 + "\'s " + "Queen" + " captured " + piece_class2 + "\'s" + capt_piece + ".")
							board[coordinates[1].index(y2)][coordinates[0].index(x2)] = board[coordinates[1].index(y1)][coordinates[0].index(x1)]
							board[coordinates[1].index(y1)][coordinates[0].index(x1)] = "  "
							space = False

				for i in range((coordinates[1].index(y1) - coordinates[1].index(y2)) - 1):  # Tiles between queen and target location
					if board[coordinates[1].index(y1) - a][coordinates[0].index(x1) - a] != "  ":  # Collision Checker
						print("\nInvalid Move! Queens cannot move over other pieces.")
						no_error = False
						space = False
						break
					a += 1

				if space:
					if board[coordinates[1].index(y2)][coordinates[0].index(x2)] != "  ":
						scorer(x2, y2, alt)
						print("\n" + piece_class1 + "\'s " + "Queen" + " captured " + piece_class2 + "\'s" + capt_piece + ".")
					elif board[coordinates[1].index(y2)][coordinates[0].index(x2)] == "  ":
						print("\n" + piece_class1 + "\'s " + "Queen " + "will move from " + x1[0] + y1 + " to " + x2[0] + y2 + ".")
					board[coordinates[1].index(y2)][coordinates[0].index(x2)] = board[coordinates[1].index(y1)][coordinates[0].index(x1)]
					board[coordinates[1].index(y1)][coordinates[0].index(x1)] = "  "

			elif coordinates[1].index(y1) < coordinates[1].index(y2) and coordinates[0].index(x1) > coordinates[0].index(x2):  # South-West Movement of Queen
				if ((coordinates[1].index(y2) - coordinates[1].index(y1)) - 1) == 0:  # Check if Queen is moving for only 1 space diagonally
					if white_queen:
						if board[coordinates[1].index(y2)][coordinates[0].index(x2)] == "  ":  # Check if adjacent location tile is empty
							print("\n" + piece_class1 + "\'s " + "Queen " + "will move from " + x1[0] + y1 + " to " + x2[0] + y2 + ".")
							board[coordinates[1].index(y2)][coordinates[0].index(x2)] = board[coordinates[1].index(y1)][coordinates[0].index(x1)]
							board[coordinates[1].index(y1)][coordinates[0].index(x1)] = "  "
							space = False
						elif (board[coordinates[1].index(y2)][coordinates[0].index(x2)])[1] == "2":  # Check if adjacent location tile occupied by enemy piece
							scorer(x2, y2, alt)
							print("\n" + piece_class1 + "\'s " + "Queen" + " captured " + piece_class2 + "\'s" + capt_piece + ".")
							board[coordinates[1].index(y2)][coordinates[0].index(x2)] = board[coordinates[1].index(y1)][coordinates[0].index(x1)]
							board[coordinates[1].index(y1)][coordinates[0].index(x1)] = "  "
							space = False

					elif not white_queen:
						if board[coordinates[1].index(y2)][coordinates[0].index(x2)] == "  ":  # Check if adjacent location tile is empty
							print("\n" + piece_class1 + "\'s " + "Queen " + "will move from " + x1[0] + y1 + " to " + x2[0] + y2 + ".")
							board[coordinates[1].index(y2)][coordinates[0].index(x2)] = board[coordinates[1].index(y1)][coordinates[0].index(x1)]
							board[coordinates[1].index(y1)][coordinates[0].index(x1)] = "  "
							space = False
						elif (board[coordinates[1].index(y2)][coordinates[0].index(x2)])[1] == "1":  # Check if adjacent location tile occupied by enemy piece
							scorer(x2, y2, alt)
							print("\n" + piece_class1 + "\'s " + "Queen" + " captured " + piece_class2 + "\'s" + capt_piece + ".")
							board[coordinates[1].index(y2)][coordinates[0].index(x2)] = board[coordinates[1].index(y1)][coordinates[0].index(x1)]
							board[coordinates[1].index(y1)][coordinates[0].index(x1)] = "  "
							space = False

				for i in range((coordinates[1].index(y2) - coordinates[1].index(y1)) - 1):  # Tiles between queen and target location
					if board[coordinates[1].index(y1) + a][coordinates[0].index(x1) - a] != "  ":  # Collision Checker
						print("\nInvalid Move! Queens cannot move over other pieces.")
						no_error = False
						space = False
						break
					a += 1

				if space:
					if board[coordinates[1].index(y2)][coordinates[0].index(x2)] != "  ":
						scorer(x2, y2, alt)
						print("\n" + piece_class1 + "\'s " + "Queen" + " captured " + piece_class2 + "\'s" + capt_piece + ".")
					elif board[coordinates[1].index(y2)][coordinates[0].index(x2)] == "  ":
						print("\n" + piece_class1 + "\'s " + "Queen " + "will move from " + x1[0] + y1 + " to " + x2[0] + y2 + ".")
					board[coordinates[1].index(y2)][coordinates[0].index(x2)] = board[coordinates[1].index(y1)][coordinates[0].index(x1)]
					board[coordinates[1].index(y1)][coordinates[0].index(x1)] = "  "

			elif coordinates[1].index(y1) < coordinates[1].index(y2) and coordinates[0].index(x1) < coordinates[0].index(x2):  # South-East Movement of Queen
				if ((coordinates[1].index(y2) - coordinates[1].index(y1)) - 1) == 0:  # Check if Queen is moving for only 1 space diagonally
					if white_queen:
						if board[coordinates[1].index(y2)][coordinates[0].index(x2)] == "  ":  # Check if adjacent location tile is empty
							print("\n" + piece_class1 + "\'s " + "Queen " + "will move from " + x1[0] + y1 + " to " + x2[0] + y2 + ".")
							board[coordinates[1].index(y2)][coordinates[0].index(x2)] = board[coordinates[1].index(y1)][coordinates[0].index(x1)]
							board[coordinates[1].index(y1)][coordinates[0].index(x1)] = "  "
							space = False
						elif (board[coordinates[1].index(y2)][coordinates[0].index(x2)])[1] == "2":  # Check if adjacent location tile occupied by enemy piece
							scorer(x2, y2, alt)
							print("\n" + piece_class1 + "\'s " + "Queen" + " captured " + piece_class2 + "\'s" + capt_piece + ".")
							board[coordinates[1].index(y2)][coordinates[0].index(x2)] = board[coordinates[1].index(y1)][coordinates[0].index(x1)]
							board[coordinates[1].index(y1)][coordinates[0].index(x1)] = "  "
							space = False

					elif not white_queen:
						if board[coordinates[1].index(y2)][coordinates[0].index(x2)] == "  ":  # Check if adjacent location tile is empty
							print("\n" + piece_class1 + "\'s " + "Queen " + "will move from " + x1[0] + y1 + " to " + x2[0] + y2 + ".")
							board[coordinates[1].index(y2)][coordinates[0].index(x2)] = board[coordinates[1].index(y1)][coordinates[0].index(x1)]
							board[coordinates[1].index(y1)][coordinates[0].index(x1)] = "  "
							space = False
						elif (board[coordinates[1].index(y2)][coordinates[0].index(x2)])[1] == "1":  # Check if adjacent location tile occupied by enemy piece
							scorer(x2, y2, alt)
							print("\n" + piece_class1 + "\'s " + "Queen" + " captured " + piece_class2 + "\'s" + capt_piece + ".")
							board[coordinates[1].index(y2)][coordinates[0].index(x2)] = board[coordinates[1].index(y1)][coordinates[0].index(x1)]
							board[coordinates[1].index(y1)][coordinates[0].index(x1)] = "  "
							space = False

				for i in range((coordinates[1].index(y2) - coordinates[1].index(y1)) - 1):  # Tiles between queen and target location
					if board[coordinates[1].index(y1) + a][coordinates[0].index(x1) + a] != "  ":  # Collision Checker
						print("\nInvalid Move! Queens cannot move over other pieces.")
						no_error = False
						space = False
						break
					a += 1

				if space:
					if board[coordinates[1].index(y2)][coordinates[0].index(x2)] != "  ":
						scorer(x2, y2, alt)
						print("\n" + piece_class1 + "\'s " + "Queen" + " captured " + piece_class2 + "\'s" + capt_piece + ".")
					elif board[coordinates[1].index(y2)][coordinates[0].index(x2)] == "  ":
						print("\n" + piece_class1 + "\'s " + "Queen " + "will move from " + x1[0] + y1 + " to " + x2[0] + y2 + ".")
					board[coordinates[1].index(y2)][coordinates[0].index(x2)] = board[coordinates[1].index(y1)][coordinates[0].index(x1)]
					board[coordinates[1].index(y1)][coordinates[0].index(x1)] = "  "

		elif (x1 == x2) or (y1 == y2):  # Check if move is linear in nature
			if (x1 == x2) and (coordinates[1].index(y1) > coordinates[1].index(y2)):  # Northward movement of Queen
				if (coordinates[1].index(y1) - coordinates[1].index(y2)) - 1 == 0:  # Check if Queen is moving 1 space northward
					if white_queen:
						if board[coordinates[1].index(y2)][coordinates[0].index(x2)] == "  ":  # Check if adjacent location tile is empty
							print("\n" + piece_class1 + "\'s " + "Queen " + "will move from " + x1[0] + y1 + " to " + x2[0] + y2 + ".")
							board[coordinates[1].index(y2)][coordinates[0].index(x2)] = board[coordinates[1].index(y1)][coordinates[0].index(x1)]
							board[coordinates[1].index(y1)][coordinates[0].index(x1)] = "  "
							space = False
						elif (board[coordinates[1].index(y2)][coordinates[0].index(x2)])[1] == "2":  # Check if adjacent location tile occupied by enemy piece
							scorer(x2, y2, alt)
							print("\n" + piece_class1 + "\'s " + "Queen" + " captured " + piece_class2 + "\'s" + capt_piece + ".")
							board[coordinates[1].index(y2)][coordinates[0].index(x2)] = board[coordinates[1].index(y1)][coordinates[0].index(x1)]
							board[coordinates[1].index(y1)][coordinates[0].index(x1)] = "  "
							space = False

					elif not white_queen:
						if board[coordinates[1].index(y2)][coordinates[0].index(x2)] == "  ":  # Check if adjacent location tile is empty
							print("\n" + piece_class1 + "\'s " + "Queen " + "will move from " + x1[0] + y1 + " to " + x2[0] + y2 + ".")
							board[coordinates[1].index(y2)][coordinates[0].index(x2)] = board[coordinates[1].index(y1)][coordinates[0].index(x1)]
							board[coordinates[1].index(y1)][coordinates[0].index(x1)] = "  "
							space = False
						elif (board[coordinates[1].index(y2)][coordinates[0].index(x2)])[1] == "1":  # Check if adjacent location tile occupied by enemy piece
							scorer(x2, y2, alt)
							print("\n" + piece_class1 + "\'s " + "Queen" + " captured " + piece_class2 + "\'s" + capt_piece + ".")
							board[coordinates[1].index(y2)][coordinates[0].index(x2)] = board[coordinates[1].index(y1)][coordinates[0].index(x1)]
							board[coordinates[1].index(y1)][coordinates[0].index(x1)] = "  "
							space = False

				for i in range((coordinates[1].index(y1) - coordinates[1].index(y2)) - 1):  # Tiles between queen and target location
					if board[coordinates[1].index(y1) - a][coordinates[0].index(x1)] != "  ":  # Collision Checker
						print("\nInvalid Move! Queens cannot move over other pieces.")
						no_error = False
						space = False
						break
					a += 1

				if space:
					if board[coordinates[1].index(y2)][coordinates[0].index(x2)] != "  ":
						scorer(x2, y2, alt)
						print("\n" + piece_class1 + "\'s " + "Queen" + " captured " + piece_class2 + "\'s" + capt_piece + ".")
					elif board[coordinates[1].index(y2)][coordinates[0].index(x2)] == "  ":
						print("\n" + piece_class1 + "\'s " + "Queen " + "will move from " + x1[0] + y1 + " to " + x2[0] + y2 + ".")
					board[coordinates[1].index(y2)][coordinates[0].index(x2)] = board[coordinates[1].index(y1)][coordinates[0].index(x1)]
					board[coordinates[1].index(y1)][coordinates[0].index(x1)] = "  "

			elif (x1 == x2) and (coordinates[1].index(y1) < coordinates[1].index(y2)):  # Southward movement of Queen
				if (coordinates[1].index(y2) - coordinates[1].index(y1)) - 1 == 0:  # Check if Queen is moving 1 space northward
					if white_queen:
						if board[coordinates[1].index(y2)][coordinates[0].index(x2)] == "  ":  # Check if adjacent location tile is empty
							print("\n" + piece_class1 + "\'s " + "Queen " + "will move from " + x1[0] + y1 + " to " + x2[0] + y2 + ".")
							board[coordinates[1].index(y2)][coordinates[0].index(x2)] = board[coordinates[1].index(y1)][coordinates[0].index(x1)]
							board[coordinates[1].index(y1)][coordinates[0].index(x1)] = "  "
							space = False
						elif (board[coordinates[1].index(y2)][coordinates[0].index(x2)])[1] == "2":  # Check if adjacent location tile occupied by enemy piece
							scorer(x2, y2, alt)
							print("\n" + piece_class1 + "\'s " + "Queen" + " captured " + piece_class2 + "\'s" + capt_piece + ".")
							board[coordinates[1].index(y2)][coordinates[0].index(x2)] = board[coordinates[1].index(y1)][coordinates[0].index(x1)]
							board[coordinates[1].index(y1)][coordinates[0].index(x1)] = "  "
							space = False

					elif not white_queen:
						if board[coordinates[1].index(y2)][coordinates[0].index(x2)] == "  ":  # Check if adjacent location tile is empty
							print("\n" + piece_class1 + "\'s " + "Queen " + "will move from " + x1[0] + y1 + " to " + x2[0] + y2 + ".")
							board[coordinates[1].index(y2)][coordinates[0].index(x2)] = board[coordinates[1].index(y1)][coordinates[0].index(x1)]
							board[coordinates[1].index(y1)][coordinates[0].index(x1)] = "  "
							space = False
						elif (board[coordinates[1].index(y2)][coordinates[0].index(x2)])[1] == "1":  # Check if adjacent location tile occupied by enemy piece
							scorer(x2, y2, alt)
							print("\n" + piece_class1 + "\'s " + "Queen" + " captured " + piece_class2 + "\'s" + capt_piece + ".")
							board[coordinates[1].index(y2)][coordinates[0].index(x2)] = board[coordinates[1].index(y1)][coordinates[0].index(x1)]
							board[coordinates[1].index(y1)][coordinates[0].index(x1)] = "  "
							space = False

				for i in range((coordinates[1].index(y1) - coordinates[1].index(y2)) - 1):  # Tiles between queen and target location
					if board[coordinates[1].index(y1) - a][coordinates[0].index(x1)] != "  ":  # Collision Checker
						print("\nInvalid Move! Queens cannot move over other pieces.")
						no_error = False
						space = False
						break
					a += 1

				if space:
					if board[coordinates[1].index(y2)][coordinates[0].index(x2)] != "  ":
						scorer(x2, y2, alt)
						print("\n" + piece_class1 + "\'s " + "Queen" + " captured " + piece_class2 + "\'s" + capt_piece + ".")
					elif board[coordinates[1].index(y2)][coordinates[0].index(x2)] == "  ":
						print("\n" + piece_class1 + "\'s " + "Queen " + "will move from " + x1[0] + y1 + " to " + x2[0] + y2 + ".")
					board[coordinates[1].index(y2)][coordinates[0].index(x2)] = board[coordinates[1].index(y1)][coordinates[0].index(x1)]
					board[coordinates[1].index(y1)][coordinates[0].index(x1)] = "  "

			elif (y1 == y2) and (coordinates[0].index(x1) < coordinates[0].index(x2)):  # Eastward Movement of Queen
				if (coordinates[0].index(x2) - coordinates[0].index(x1)) - 1 == 0:  # Check if Queen is moving 1 space eastward
					if white_queen:
						if board[coordinates[1].index(y2)][coordinates[0].index(x2)] == "  ":  # Check if adjacent location tile is empty
							print("\n" + piece_class1 + "\'s " + "Queen " + "will move from " + x1[0] + y1 + " to " + x2[0] + y2 + ".")
							board[coordinates[1].index(y2)][coordinates[0].index(x2)] = board[coordinates[1].index(y1)][coordinates[0].index(x1)]
							board[coordinates[1].index(y1)][coordinates[0].index(x1)] = "  "
							space = False
						elif (board[coordinates[1].index(y2)][coordinates[0].index(x2)])[1] == "2":  # Check if adjacent location tile occupied by enemy piece
							scorer(x2, y2, alt)
							print("\n" + piece_class1 + "\'s " + "Queen" + " captured " + piece_class2 + "\'s" + capt_piece + ".")
							board[coordinates[1].index(y2)][coordinates[0].index(x2)] = board[coordinates[1].index(y1)][coordinates[0].index(x1)]
							board[coordinates[1].index(y1)][coordinates[0].index(x1)] = "  "
							space = False

					elif not white_queen:
						if board[coordinates[1].index(y2)][coordinates[0].index(x2)] == "  ":  # Check if adjacent location tile is empty
							print("\n" + piece_class1 + "\'s " + "Queen " + "will move from " + x1[0] + y1 + " to " + x2[0] + y2 + ".")
							board[coordinates[1].index(y2)][coordinates[0].index(x2)] = board[coordinates[1].index(y1)][coordinates[0].index(x1)]
							board[coordinates[1].index(y1)][coordinates[0].index(x1)] = "  "
							space = False
						elif (board[coordinates[1].index(y2)][coordinates[0].index(x2)])[1] == "1":  # Check if adjacent location tile occupied by enemy piece
							scorer(x2, y2, alt)
							print("\n" + piece_class1 + "\'s " + "Queen" + " captured " + piece_class2 + "\'s" + capt_piece + ".")
							board[coordinates[1].index(y2)][coordinates[0].index(x2)] = board[coordinates[1].index(y1)][coordinates[0].index(x1)]
							board[coordinates[1].index(y1)][coordinates[0].index(x1)] = "  "
							space = False

				for i in range((coordinates[0].index(x2) - coordinates[0].index(x1)) - 1):  # Tiles between queen and target location
					if board[coordinates[1].index(y1)][coordinates[0].index(x1) + a] != "  ":  # Collision Checker
						print("\nInvalid Move! Queens cannot move over other pieces.")
						no_error = False
						space = False
						break
					a += 1

				if space:
					if board[coordinates[1].index(y2)][coordinates[0].index(x2)] != "  ":
						scorer(x2, y2, alt)
						print("\n" + piece_class1 + "\'s " + "Queen" + " captured " + piece_class2 + "\'s" + capt_piece + ".")
					elif board[coordinates[1].index(y2)][coordinates[0].index(x2)] == "  ":
						print("\n" + piece_class1 + "\'s " + "Queen " + "will move from " + x1[0] + y1 + " to " + x2[0] + y2 + ".")
					board[coordinates[1].index(y2)][coordinates[0].index(x2)] = board[coordinates[1].index(y1)][coordinates[0].index(x1)]
					board[coordinates[1].index(y1)][coordinates[0].index(x1)] = "  "

			elif (y1 == y2) and (coordinates[0].index(x1) > coordinates[0].index(x2)):  # Westward Movement of Queen
				if (coordinates[0].index(x1) - coordinates[0].index(x2)) - 1 == 0:  # Check if Queen is moving 1 space eastward
					if white_queen:
						if board[coordinates[1].index(y2)][coordinates[0].index(x2)] == "  ":  # Check if adjacent location tile is empty
							print("\n" + piece_class1 + "\'s " + "Queen " + "will move from " + x1[0] + y1 + " to " + x2[0] + y2 + ".")
							board[coordinates[1].index(y2)][coordinates[0].index(x2)] = board[coordinates[1].index(y1)][coordinates[0].index(x1)]
							board[coordinates[1].index(y1)][coordinates[0].index(x1)] = "  "
							space = False
						elif (board[coordinates[1].index(y2)][coordinates[0].index(x2)])[1] == "2":  # Check if adjacent location tile occupied by enemy piece
							scorer(x2, y2, alt)
							print("\n" + piece_class1 + "\'s " + "Queen" + " captured " + piece_class2 + "\'s" + capt_piece + ".")
							board[coordinates[1].index(y2)][coordinates[0].index(x2)] = board[coordinates[1].index(y1)][coordinates[0].index(x1)]
							board[coordinates[1].index(y1)][coordinates[0].index(x1)] = "  "
							space = False

					elif not white_queen:
						if board[coordinates[1].index(y2)][coordinates[0].index(x2)] == "  ":  # Check if adjacent location tile is empty
							print("\n" + piece_class1 + "\'s " + "Queen " + "will move from " + x1[0] + y1 + " to " + x2[0] + y2 + ".")
							board[coordinates[1].index(y2)][coordinates[0].index(x2)] = board[coordinates[1].index(y1)][coordinates[0].index(x1)]
							board[coordinates[1].index(y1)][coordinates[0].index(x1)] = "  "
							space = False
						elif (board[coordinates[1].index(y2)][coordinates[0].index(x2)])[1] == "1":  # Check if adjacent location tile occupied by enemy piece
							scorer(x2, y2, alt)
							print("\n" + piece_class1 + "\'s " + "Queen" + " captured " + piece_class2 + "\'s" + capt_piece + ".")
							board[coordinates[1].index(y2)][coordinates[0].index(x2)] = board[coordinates[1].index(y1)][coordinates[0].index(x1)]
							board[coordinates[1].index(y1)][coordinates[0].index(x1)] = "  "
							space = False

				for i in range((coordinates[0].index(x1) - coordinates[0].index(x2)) - 1):  # Tiles between queen and target location
					if board[coordinates[1].index(y1)][coordinates[0].index(x1) - a] != "  ":  # Collision Checker
						print("\nInvalid Move! Queens cannot move over other pieces.")
						no_error = False
						space = False
						break
					a += 1

				if space:
					if board[coordinates[1].index(y2)][coordinates[0].index(x2)] != "  ":
						scorer(x2, y2, alt)
						print("\n" + piece_class1 + "\'s " + "Queen" + " captured " + piece_class2 + "\'s" + capt_piece + ".")
					elif board[coordinates[1].index(y2)][coordinates[0].index(x2)] == "  ":
						print("\n" + piece_class1 + "\'s " + "Queen " + "will move from " + x1[0] + y1 + " to " + x2[0] + y2 + ".")
					board[coordinates[1].index(y2)][coordinates[0].index(x2)] = board[coordinates[1].index(y1)][coordinates[0].index(x1)]
					board[coordinates[1].index(y1)][coordinates[0].index(x1)] = "  "

		else:
			print("\nInvalid Move! Queens can only move in a straight line.")
			no_error = False


def king(x1, y1, x2, y2, white_king, alt):
	global no_error
	global checked
	global piece_class1
	global piece_class2
	global capt_piece
	global dec

	# Checks if King or Rooks made their first move
	global white_k
	global white_r1
	global white_r2

	global black_k
	global black_r1
	global black_r2

	# determine which player is making the move
	if (board[coordinates[1].index(y1)][coordinates[0].index(x1)])[1] == "1":
		piece_class1 = "Player 1"
	elif (board[coordinates[1].index(y1)][coordinates[0].index(x1)])[1] == "2":
		piece_class1 = "Player 2"

	if (board[coordinates[1].index(y2)][coordinates[0].index(x2)])[1] == "1":
		piece_class2 = "Player 1"
	elif (board[coordinates[1].index(y2)][coordinates[0].index(x2)])[1] == "2":
		piece_class2 = "Player 2"

	# Determine which piece is captured
	if (board[coordinates[1].index(y2)][coordinates[0].index(x2)])[0] == "P":
		capt_piece = " Pawn"
	elif (board[coordinates[1].index(y2)][coordinates[0].index(x2)])[0] == "R":
		capt_piece = " Rook"
	elif (board[coordinates[1].index(y2)][coordinates[0].index(x2)])[0] == "B":
		capt_piece = " Bishop"
	elif (board[coordinates[1].index(y2)][coordinates[0].index(x2)])[0] == "N":
		capt_piece = " Knight"
	elif (board[coordinates[1].index(y2)][coordinates[0].index(x2)])[0] == "Q":
		capt_piece = " Queen"
	elif (board[coordinates[1].index(y2)][coordinates[0].index(x2)])[0] == "K":
		capt_piece = " King"
		
	if capt_piece == " King":
		dec = True

	if white_king:
		if (board[coordinates[1].index(y2)][coordinates[0].index(x2)])[1] == "1":
			print("\nInvalid Move! Kings cannot an capture allied piece.")
			no_error = False
			return
	elif not white_king:
		if (board[coordinates[1].index(y2)][coordinates[0].index(x2)])[1] == "2":
			print("\nInvalid Move! Kings cannot an capture allied piece.")
			no_error = False
			return

	# Check if chosen move is Castling
	if alt == 1:
		if x2 == "G " and y2 == "1":  # White King, King-Side Castling
			if not checked:
				if not white_k and not white_r2:
					check(x2, y2, alt)
					if checked:
						print("\nInvalid Move! Unable to perform Castling, path in between is under enemy range.")
						no_error = False
						return
					check("F ", "1", alt)
					if checked:
						print("Invalid Move! Unable to perform Castling, path in between is under enemy range.")
						no_error = False
						return
					elif not checked:
						print("\n" + piece_class1 + " performs a Kingside Castling.")
						board[coordinates[1].index(y2)][coordinates[0].index(x2)] = board[coordinates[1].index(y1)][coordinates[0].index(x1)]
						board[coordinates[1].index(y1)][coordinates[0].index(x1)] = "  "
						board[coordinates[1].index("1")][coordinates[0].index("H ")] = "  "
						board[coordinates[1].index("1")][coordinates[0].index("F ")] = "R1"
						return
				else:
					print("Invalid Move! Either King or Rook already moved.")
					no_error = False
					return
			else:
				print("Invalid Move! Cannot perform castling when King is checked.")
				no_error = False
				return

		elif x2 == "C " and y2 == "1":  # White King, Queen-Side Castling
			if not checked:
				if not white_k and not white_r1:
					check(x2, y2, alt)  # Needs triple check filter, check status resets without triple check filter
					if checked:
						print("\nInvalid Move! Unable to perform Castling, path in between is under enemy range.")
						no_error = False
						return
					check("D ", "1", alt)
					if checked:
						print("\nInvalid Move! Unable to perform Castling, path in between is under enemy range.")
						no_error = False
						return
					check("B ", "1", alt)
					if checked:
						print("\nInvalid Move! Unable to perform Castling, path in between is under enemy range.")
						no_error = False
						return
					elif not checked:
						print("\n" + piece_class1 + " performs a Queenside Castling.")
						board[coordinates[1].index(y2)][coordinates[0].index(x2)] = board[coordinates[1].index(y1)][coordinates[0].index(x1)]
						board[coordinates[1].index(y1)][coordinates[0].index(x1)] = "  "
						board[coordinates[1].index("1")][coordinates[0].index("A ")] = "  "
						board[coordinates[1].index("1")][coordinates[0].index("D ")] = "R1"
						return
				else:
					print("Invalid Move! Either King or Rook already moved.")
					no_error = False
					return
			else:
				print("Invalid Move! Cannot perform castling when King is checked.")
				no_error = False
				return

	elif alt == 2:
		if x2 == "G " and y2 == "8":  # Black King, King-Side Castling
			print(checked)
			if not checked:
				print("fdg")
				if not black_k and not black_r2:
					check(x2, y2, alt)
					if checked:
						print("\nInvalid Move! Unable to perform Castling, path in between is under enemy range.")
						no_error = False
						return
					check("F ", "8", alt)
					if checked:
						print("\nInvalid Move! Unable to perform Castling, path in between is under enemy range.")
						no_error = False
						return
					elif not checked:
						print("\n" + piece_class1 + " performs a Kingside Castling.")
						board[coordinates[1].index(y2)][coordinates[0].index(x2)] = board[coordinates[1].index(y1)][coordinates[0].index(x1)]
						board[coordinates[1].index(y1)][coordinates[0].index(x1)] = "  "
						board[coordinates[1].index("8")][coordinates[0].index("H ")] = "  "
						board[coordinates[1].index("8")][coordinates[0].index("F ")] = "R2"
						return
				else:
					print("Invalid Move! Either King or Rook already moved.")
					no_error = False
			else:
				print("Invalid Move! Cannot perform castling when King is checked.")
				no_error = False
				return

		elif x2 == "C " and y2 == "8":  # Black King, Queen-Side Castling
			if not checked:
				if not black_k and not black_r1:
					check(x2, y2, alt)
					if checked:
						print("\nInvalid Move! Unable to perform Castling, path in between is under enemy range.")
						no_error = False
						return
					check("D ", "8", alt)
					if checked:
						print("\nInvalid Move! Unable to perform Castling, path in between is under enemy range.")
						no_error = False
						return
					check("B ", "8", alt)
					if checked:
						print("\nInvalid Move! Unable to perform Castling, path in between is under enemy range.")
						no_error = False
						return
					elif not checked:
						print("\n" + piece_class1 + " performs a Queenside Castling.")
						board[coordinates[1].index(y2)][coordinates[0].index(x2)] = board[coordinates[1].index(y1)][coordinates[0].index(x1)]
						board[coordinates[1].index(y1)][coordinates[0].index(x1)] = "  "
						board[coordinates[1].index("8")][coordinates[0].index("A ")] = "  "
						board[coordinates[1].index("8")][coordinates[0].index("D ")] = "R2"
						return
				else:
					print("Invalid Move! Either King or Rook already moved.")
					no_error = False
					return
			else:
				print("Invalid Move! Cannot perform castling when King is checked.")
				no_error = False
				return

	check(x2, y2, alt)  # Basis of virtual_move function
	virtual_move(x1, y1, x2, y2, alt)
	if checked:
		print("\nInvalid Move! You cannot move your King on spaces which are under enemy range.")
		no_error = False
		checked = False
		return

	# Proper King Function
	if (coordinates[0].index(x1) + coordinates[1].index(y1) == coordinates[0].index(x2) + coordinates[1].index(y2)) or (coordinates[0].index(x1) - coordinates[1].index(y1) == coordinates[0].index(x2) - coordinates[1].index(y2)):  # Determine if chosen movement is diagonal in nature
		if coordinates[1].index(y1) > coordinates[1].index(y2) and coordinates[0].index(x1) < coordinates[0].index(x2):  # North-East Movement of King
			if ((coordinates[1].index(y1) - coordinates[1].index(y2)) - 1) == 0:  # Check if King is moving for only 1 space diagonally
				if white_king:
					if board[coordinates[1].index(y2)][coordinates[0].index(x2)] == "  ":  # Check if adjacent location tile is empty
						print("\n" + piece_class1 + "\'s " + "King " + "will move from " + x1[0] + y1 + " to " + x2[0] + y2 + ".")
						board[coordinates[1].index(y2)][coordinates[0].index(x2)] = board[coordinates[1].index(y1)][coordinates[0].index(x1)]
						board[coordinates[1].index(y1)][coordinates[0].index(x1)] = "  "
					elif (board[coordinates[1].index(y2)][coordinates[0].index(x2)])[1] == "2":  # Check if adjacent location tile occupied by enemy piece
						print("\n" + piece_class1 + "\'s " + "King" + " captured " + piece_class2 + "\'s" + capt_piece + ".")
						board[coordinates[1].index(y2)][coordinates[0].index(x2)] = board[coordinates[1].index(y1)][coordinates[0].index(x1)]
						board[coordinates[1].index(y1)][coordinates[0].index(x1)] = "  "

				elif not white_king:
					if board[coordinates[1].index(y2)][coordinates[0].index(x2)] == "  ":  # Check if adjacent location tile is empty
						print("\n" + piece_class1 + "\'s " + "King " + "will move from " + x1[0] + y1 + " to " + x2[0] + y2 + ".")
						board[coordinates[1].index(y2)][coordinates[0].index(x2)] = board[coordinates[1].index(y1)][coordinates[0].index(x1)]
						board[coordinates[1].index(y1)][coordinates[0].index(x1)] = "  "
					elif (board[coordinates[1].index(y2)][coordinates[0].index(x2)])[1] == "1":  # Check if adjacent location tile occupied by enemy piece
						print("\n" + piece_class1 + "\'s " + "King" + " captured " + piece_class2 + "\'s" + capt_piece + ".")
						board[coordinates[1].index(y2)][coordinates[0].index(x2)] = board[coordinates[1].index(y1)][coordinates[0].index(x1)]
						board[coordinates[1].index(y1)][coordinates[0].index(x1)] = "  "
			else:
				print("\nInvalid Move! Kings can only move 1 space in any direction.")
				no_error = False
				return

		elif coordinates[1].index(y1) > coordinates[1].index(y2) and coordinates[0].index(x1) > coordinates[0].index(x2):  # North-West Movement of King
			if ((coordinates[1].index(y1) - coordinates[1].index(y2)) - 1) == 0:  # Check if King is moving for only 1 space diagonally
				if white_king:
					if board[coordinates[1].index(y2)][coordinates[0].index(x2)] == "  ":  # Check if adjacent location tile is empty
						print("\n" + piece_class1 + "\'s " + "King " + "will move from " + x1[0] + y1 + " to " + x2[0] + y2 + ".")
						board[coordinates[1].index(y2)][coordinates[0].index(x2)] = board[coordinates[1].index(y1)][coordinates[0].index(x1)]
						board[coordinates[1].index(y1)][coordinates[0].index(x1)] = "  "
					elif (board[coordinates[1].index(y2)][coordinates[0].index(x2)])[1] == "2":  # Check if adjacent location tile occupied by enemy piece
						print("\n" + piece_class1 + "\'s " + "King" + " captured " + piece_class2 + "\'s" + capt_piece + ".")
						board[coordinates[1].index(y2)][coordinates[0].index(x2)] = board[coordinates[1].index(y1)][coordinates[0].index(x1)]
						board[coordinates[1].index(y1)][coordinates[0].index(x1)] = "  "

				elif not white_king:
					if board[coordinates[1].index(y2)][coordinates[0].index(x2)] == "  ":  # Check if adjacent location tile is empty
						print("\n" + piece_class1 + "\'s " + "King " + "will move from " + x1[0] + y1 + " to " + x2[0] + y2 + ".")
						board[coordinates[1].index(y2)][coordinates[0].index(x2)] = board[coordinates[1].index(y1)][coordinates[0].index(x1)]
						board[coordinates[1].index(y1)][coordinates[0].index(x1)] = "  "
					elif (board[coordinates[1].index(y2)][coordinates[0].index(x2)])[1] == "1":  # Check if adjacent location tile occupied by enemy piece
						print("\n" + piece_class1 + "\'s " + "King" + " captured " + piece_class2 + "\'s" + capt_piece + ".")
						board[coordinates[1].index(y2)][coordinates[0].index(x2)] = board[coordinates[1].index(y1)][coordinates[0].index(x1)]
						board[coordinates[1].index(y1)][coordinates[0].index(x1)] = "  "
			else:
				print("\nInvalid Move! Kings can only move 1 space in any direction.")
				no_error = False
				return

		elif coordinates[1].index(y1) < coordinates[1].index(y2) and coordinates[0].index(x1) > coordinates[0].index(x2):  # South-West Movement of King
			if ((coordinates[1].index(y2) - coordinates[1].index(y1)) - 1) == 0:  # Check if King is moving for only 1 space diagonally
				if white_king:
					if board[coordinates[1].index(y2)][coordinates[0].index(x2)] == "  ":  # Check if adjacent location tile is empty
						print("\n" + piece_class1 + "\'s " + "King " + "will move from " + x1[0] + y1 + " to " + x2[0] + y2 + ".")
						board[coordinates[1].index(y2)][coordinates[0].index(x2)] = board[coordinates[1].index(y1)][coordinates[0].index(x1)]
						board[coordinates[1].index(y1)][coordinates[0].index(x1)] = "  "
					elif (board[coordinates[1].index(y2)][coordinates[0].index(x2)])[1] == "2":  # Check if adjacent location tile occupied by enemy piece
						print("\n" + piece_class1 + "\'s " + "King" + " captured " + piece_class2 + "\'s" + capt_piece + ".")
						board[coordinates[1].index(y2)][coordinates[0].index(x2)] = board[coordinates[1].index(y1)][coordinates[0].index(x1)]
						board[coordinates[1].index(y1)][coordinates[0].index(x1)] = "  "

				elif not white_king:
					if board[coordinates[1].index(y2)][coordinates[0].index(x2)] == "  ":  # Check if adjacent location tile is empty
						print("\n" + piece_class1 + "\'s " + "King " + "will move from " + x1[0] + y1 + " to " + x2[0] + y2 + ".")
						board[coordinates[1].index(y2)][coordinates[0].index(x2)] = board[coordinates[1].index(y1)][coordinates[0].index(x1)]
						board[coordinates[1].index(y1)][coordinates[0].index(x1)] = "  "
					elif (board[coordinates[1].index(y2)][coordinates[0].index(x2)])[1] == "1":  # Check if adjacent location tile occupied by enemy piece
						print("\n" + piece_class1 + "\'s " + "King" + " captured " + piece_class2 + "\'s" + capt_piece + ".")
						board[coordinates[1].index(y2)][coordinates[0].index(x2)] = board[coordinates[1].index(y1)][coordinates[0].index(x1)]
						board[coordinates[1].index(y1)][coordinates[0].index(x1)] = "  "
			else:
				print("\nInvalid Move! Kings can only move 1 space in any direction.")
				no_error = False
				return

		elif coordinates[1].index(y1) < coordinates[1].index(y2) and coordinates[0].index(x1) < coordinates[0].index(x2):  # South-East Movement of King
			if ((coordinates[1].index(y2) - coordinates[1].index(y1)) - 1) == 0:  # Check if King is moving for only 1 space diagonally
				if white_king:
					if board[coordinates[1].index(y2)][coordinates[0].index(x2)] == "  ":  # Check if adjacent location tile is empty
						print("\n" + piece_class1 + "\'s " + "King " + "will move from " + x1[0] + y1 + " to " + x2[0] + y2 + ".")
						board[coordinates[1].index(y2)][coordinates[0].index(x2)] = board[coordinates[1].index(y1)][coordinates[0].index(x1)]
						board[coordinates[1].index(y1)][coordinates[0].index(x1)] = "  "
					elif (board[coordinates[1].index(y2)][coordinates[0].index(x2)])[1] == "2":  # Check if adjacent location tile occupied by enemy piece
						print("\n" + piece_class1 + "\'s " + "King" + " captured " + piece_class2 + "\'s" + capt_piece + ".")
						board[coordinates[1].index(y2)][coordinates[0].index(x2)] = board[coordinates[1].index(y1)][coordinates[0].index(x1)]
						board[coordinates[1].index(y1)][coordinates[0].index(x1)] = "  "

				elif not white_king:
					if board[coordinates[1].index(y2)][coordinates[0].index(x2)] == "  ":  # Check if adjacent location tile is empty
						print("\n" + piece_class1 + "\'s " + "King " + "will move from " + x1[0] + y1 + " to " + x2[0] + y2 + ".")
						board[coordinates[1].index(y2)][coordinates[0].index(x2)] = board[coordinates[1].index(y1)][coordinates[0].index(x1)]
						board[coordinates[1].index(y1)][coordinates[0].index(x1)] = "  "
					elif (board[coordinates[1].index(y2)][coordinates[0].index(x2)])[1] == "1":  # Check if adjacent location tile occupied by enemy piece
						print("\n" + piece_class1 + "\'s " + "King" + " captured " + piece_class2 + "\'s" + capt_piece + ".")
						board[coordinates[1].index(y2)][coordinates[0].index(x2)] = board[coordinates[1].index(y1)][coordinates[0].index(x1)]
						board[coordinates[1].index(y1)][coordinates[0].index(x1)] = "  "
			else:
				print("\nInvalid Move! Kings can only move 1 space in any direction.")
				no_error = False
				return

	elif (x1 == x2) or (y1 == y2):  # Check if move is linear in nature
		if (x1 == x2) and (coordinates[1].index(y1) > coordinates[1].index(y2)):  # Northward movement of King
			if (coordinates[1].index(y1) - coordinates[1].index(y2)) - 1 == 0:  # Check if King is moving 1 space northward
				if white_king:
					if board[coordinates[1].index(y2)][coordinates[0].index(x2)] == "  ":  # Check if adjacent location tile is empty
						print("\n" + piece_class1 + "\'s " + "King " + "will move from " + x1[0] + y1 + " to " + x2[0] + y2 + ".")
						board[coordinates[1].index(y2)][coordinates[0].index(x2)] = board[coordinates[1].index(y1)][coordinates[0].index(x1)]
						board[coordinates[1].index(y1)][coordinates[0].index(x1)] = "  "
					elif (board[coordinates[1].index(y2)][coordinates[0].index(x2)])[1] == "2":  # Check if adjacent location tile occupied by enemy piece
						print("\n" + piece_class1 + "\'s " + "King" + " captured " + piece_class2 + "\'s" + capt_piece + ".")
						board[coordinates[1].index(y2)][coordinates[0].index(x2)] = board[coordinates[1].index(y1)][coordinates[0].index(x1)]
						board[coordinates[1].index(y1)][coordinates[0].index(x1)] = "  "

				elif not white_king:
					if board[coordinates[1].index(y2)][coordinates[0].index(x2)] == "  ":  # Check if adjacent location tile is empty
						print("\n" + piece_class1 + "\'s " + "King " + "will move from " + x1[0] + y1 + " to " + x2[0] + y2 + ".")
						board[coordinates[1].index(y2)][coordinates[0].index(x2)] = board[coordinates[1].index(y1)][coordinates[0].index(x1)]
						board[coordinates[1].index(y1)][coordinates[0].index(x1)] = "  "
					elif (board[coordinates[1].index(y2)][coordinates[0].index(x2)])[1] == "1":  # Check if adjacent location tile occupied by enemy piece
						print("\n" + piece_class1 + "\'s " + "King" + " captured " + piece_class2 + "\'s" + capt_piece + ".")
						board[coordinates[1].index(y2)][coordinates[0].index(x2)] = board[coordinates[1].index(y1)][coordinates[0].index(x1)]
						board[coordinates[1].index(y1)][coordinates[0].index(x1)] = "  "
			else:
				print("\nInvalid Move! Kings can only move 1 space in any direction.")
				no_error = False
				return

		elif (x1 == x2) and (coordinates[1].index(y1) < coordinates[1].index(y2)):  # Southward movement of King
			if (coordinates[1].index(y2) - coordinates[1].index(y1)) - 1 == 0:  # Check if King is moving 1 space northward
				if white_king:
					if board[coordinates[1].index(y2)][coordinates[0].index(x2)] == "  ":  # Check if adjacent location tile is empty
						print("\n" + piece_class1 + "\'s " + "King " + "will move from " + x1[0] + y1 + " to " + x2[0] + y2 + ".")
						board[coordinates[1].index(y2)][coordinates[0].index(x2)] = board[coordinates[1].index(y1)][coordinates[0].index(x1)]
						board[coordinates[1].index(y1)][coordinates[0].index(x1)] = "  "
					elif (board[coordinates[1].index(y2)][coordinates[0].index(x2)])[1] == "2":  # Check if adjacent location tile occupied by enemy piece
						print("\n" + piece_class1 + "\'s " + "King" + " captured " + piece_class2 + "\'s" + capt_piece + ".")
						board[coordinates[1].index(y2)][coordinates[0].index(x2)] = board[coordinates[1].index(y1)][coordinates[0].index(x1)]
						board[coordinates[1].index(y1)][coordinates[0].index(x1)] = "  "

				elif not white_king:
					if board[coordinates[1].index(y2)][coordinates[0].index(x2)] == "  ":  # Check if adjacent location tile is empty
						print("\n" + piece_class1 + "\'s " + "King " + "will move from " + x1[0] + y1 + " to " + x2[0] + y2 + ".")
						board[coordinates[1].index(y2)][coordinates[0].index(x2)] = board[coordinates[1].index(y1)][coordinates[0].index(x1)]
						board[coordinates[1].index(y1)][coordinates[0].index(x1)] = "  "
					elif (board[coordinates[1].index(y2)][coordinates[0].index(x2)])[1] == "1":  # Check if adjacent location tile occupied by enemy piece
						print("\n" + piece_class1 + "\'s " + "King" + " captured " + piece_class2 + "\'s" + capt_piece + ".")
						board[coordinates[1].index(y2)][coordinates[0].index(x2)] = board[coordinates[1].index(y1)][coordinates[0].index(x1)]
						board[coordinates[1].index(y1)][coordinates[0].index(x1)] = "  "
			else:
				print("\nInvalid Move! Kings can only move 1 space in any direction.")
				no_error = False
				return

		elif (y1 == y2) and (coordinates[0].index(x1) < coordinates[0].index(x2)):  # Eastward Movement of King
			if (coordinates[0].index(x2) - coordinates[0].index(x1)) - 1 == 0:  # Check if King is moving 1 space eastward
				if white_king:
					if board[coordinates[1].index(y2)][coordinates[0].index(x2)] == "  ":  # Check if adjacent location tile is empty
						print("\n" + piece_class1 + "\'s " + "King " + "will move from " + x1[0] + y1 + " to " + x2[0] + y2 + ".")
						board[coordinates[1].index(y2)][coordinates[0].index(x2)] = board[coordinates[1].index(y1)][coordinates[0].index(x1)]
						board[coordinates[1].index(y1)][coordinates[0].index(x1)] = "  "
					elif (board[coordinates[1].index(y2)][coordinates[0].index(x2)])[1] == "2":  # Check if adjacent location tile occupied by enemy piece
						print("\n" + piece_class1 + "\'s " + "King" + " captured " + piece_class2 + "\'s" + capt_piece + ".")
						board[coordinates[1].index(y2)][coordinates[0].index(x2)] = board[coordinates[1].index(y1)][coordinates[0].index(x1)]
						board[coordinates[1].index(y1)][coordinates[0].index(x1)] = "  "

				elif not white_king:
					if board[coordinates[1].index(y2)][coordinates[0].index(x2)] == "  ":  # Check if adjacent location tile is empty
						print("\n" + piece_class1 + "\'s " + "King " + "will move from " + x1[0] + y1 + " to " + x2[0] + y2 + ".")
						board[coordinates[1].index(y2)][coordinates[0].index(x2)] = board[coordinates[1].index(y1)][coordinates[0].index(x1)]
						board[coordinates[1].index(y1)][coordinates[0].index(x1)] = "  "
					elif (board[coordinates[1].index(y2)][coordinates[0].index(x2)])[1] == "1":  # Check if adjacent location tile occupied by enemy piece
						print("\n" + piece_class1 + "\'s " + "King" + " captured " + piece_class2 + "\'s" + capt_piece + ".")
						board[coordinates[1].index(y2)][coordinates[0].index(x2)] = board[coordinates[1].index(y1)][coordinates[0].index(x1)]
						board[coordinates[1].index(y1)][coordinates[0].index(x1)] = "  "
			else:
				print("\nInvalid Move! Kings can only move 1 space in any direction.")
				no_error = False
				return

		elif (y1 == y2) and (coordinates[0].index(x1) > coordinates[0].index(x2)):  # Westward Movement of King
			if (coordinates[0].index(x1) - coordinates[0].index(x2)) - 1 == 0:  # Check if King is moving 1 space eastward
				if white_king:
					if board[coordinates[1].index(y2)][coordinates[0].index(x2)] == "  ":  # Check if adjacent location tile is empty
						print("\n" + piece_class1 + "\'s " + "King " + "will move from " + x1[0] + y1 + " to " + x2[0] + y2 + ".")
						board[coordinates[1].index(y2)][coordinates[0].index(x2)] = board[coordinates[1].index(y1)][coordinates[0].index(x1)]
						board[coordinates[1].index(y1)][coordinates[0].index(x1)] = "  "
					elif (board[coordinates[1].index(y2)][coordinates[0].index(x2)])[1] == "2":  # Check if adjacent location tile occupied by enemy piece
						print("\n" + piece_class1 + "\'s " + "King" + " captured " + piece_class2 + "\'s" + capt_piece + ".")
						board[coordinates[1].index(y2)][coordinates[0].index(x2)] = board[coordinates[1].index(y1)][coordinates[0].index(x1)]
						board[coordinates[1].index(y1)][coordinates[0].index(x1)] = "  "

				elif not white_king:
					if board[coordinates[1].index(y2)][coordinates[0].index(x2)] == "  ":  # Check if adjacent location tile is empty
						print("\n" + piece_class1 + "\'s " + "King " + "will move from " + x1[0] + y1 + " to " + x2[0] + y2 + ".")
						board[coordinates[1].index(y2)][coordinates[0].index(x2)] = board[coordinates[1].index(y1)][coordinates[0].index(x1)]
						board[coordinates[1].index(y1)][coordinates[0].index(x1)] = "  "
					elif (board[coordinates[1].index(y2)][coordinates[0].index(x2)])[1] == "1":  # Check if adjacent location tile occupied by enemy piece
						print("\n" + piece_class1 + "\'s " + "King" + " captured " + piece_class2 + "\'s" + capt_piece + ".")
						board[coordinates[1].index(y2)][coordinates[0].index(x2)] = board[coordinates[1].index(y1)][coordinates[0].index(x1)]
						board[coordinates[1].index(y1)][coordinates[0].index(x1)] = "  "
			else:
				print("\nInvalid Move! Kings can only move 1 space in any direction.")
				no_error = False
				return

	if board[7][4] == "  ":
		white_k = True
	if board[7][0] == "  ":
		white_r1 = True
	if board[7][7] == "  ":
		white_r2 = True
	if board[0][4] == "  ":
		black_k = True
	if board[0][0] == "  ":
		black_r1 = True
	if board[0][7] == "  ":
		black_r2 = True


def check(x1, y1, player):
	global checked
	global no_error

	checked = False

	if coordinates[1].index(y1) > 0:
		# Loop on King's Y+ Side
		for i in range((coordinates[1].index(y1) - 1), -1, -1):
			if board[i][coordinates[0].index(x1)] != "  ":
				if player == 1:
					if board[i][coordinates[0].index(x1)] == "R2" or board[i][coordinates[0].index(x1)] == "Q2":
						checked = True
						no_error = False
						return
				elif player == 2:
					if board[i][coordinates[0].index(x1)] == "R1" or board[i][coordinates[0].index(x1)] == "Q1":
						checked = True
						no_error = False
						return
				break

	if coordinates[1].index(y1) < 7:
		# Loop on King's Y- Side
		for i in range((coordinates[1].index(y1) + 1), 8):
			if board[i][coordinates[0].index(x1)] != "  ":
				if player == 1:
					if board[i][coordinates[0].index(x1)] == "R2" or board[i][coordinates[0].index(x1)] == "Q2":
						checked = True
						no_error = False
						return
				elif player == 2:
					if board[i][coordinates[0].index(x1)] == "R1" or board[i][coordinates[0].index(x1)] == "Q1":
						checked = True
						no_error = False
						return
				break

	if coordinates[0].index(x1) < 7:
		# Loop on King's X+ Side
		for i in range((coordinates[0].index(x1) + 1), 8):
			if board[coordinates[1].index(y1)][i] != "  ":
				if player == 1:
					if board[coordinates[1].index(y1)][i] == "R2" or board[coordinates[1].index(y1)][i] == "Q2":
						checked = True
						no_error = False
						return
				elif player == 2:
					if board[coordinates[1].index(y1)][i] == "R1" or board[coordinates[1].index(y1)][i] == "Q1":
						checked = True
						no_error = False
						return
				break

	if coordinates[0].index(x1) > 0:
		# Loop on King's X- Side
		for i in range((coordinates[0].index(x1) - 1), -1, -1):
			if board[coordinates[1].index(y1)][i] != "  ":
				if player == 1:
					if board[coordinates[1].index(y1)][i] == "R2" or board[coordinates[1].index(y1)][i] == "Q2":
						checked = True
						no_error = False
						return
				elif player == 2:
					if board[coordinates[1].index(y1)][i] == "R1" or board[coordinates[1].index(y1)][i] == "Q1":
						checked = True
						no_error = False
						return
				break

	if coordinates[1].index(y1) > 0 and coordinates[0].index(x1) < 7:  # Loop on King's X+Y+ Side (Cartesian Orientation)
		# X component is disregarded. Only Y component is needed to compute for the number of iteration
		a = 1
		end_y1 = 0
		if coordinates[0].index(x1) + coordinates[1].index(y1) < 7:  # if King is in - Side of Right-Left Diagonal
			end_y1 = 0

		elif coordinates[0].index(x1) + coordinates[1].index(y1) > 7:  # if King is in + Side of Right-Left Diagonal
			end_y1 = 0 + (coordinates[0].index(x1) - (7 - coordinates[1].index(y1)))

		elif coordinates[0].index(x1) + coordinates[1].index(y1) == 7:
			end_y1 = coordinates[1].index(y1)

		for i in range(coordinates[1].index(y1) - end_y1):  # Tiles between King and Max Diagonal location
			if board[coordinates[1].index(y1) - a][coordinates[0].index(x1) + a] != "  ":
				if player == 1:
					if board[coordinates[1].index(y1) - 1][coordinates[0].index(x1) + 1] == "P2":
						checked = True
						no_error = False
						return
					elif board[coordinates[1].index(y1) - a][coordinates[0].index(x1) + a] == "B2" or board[coordinates[1].index(y1) - a][coordinates[0].index(x1) + a] == "Q2":  # Collision Checker
						checked = True
						no_error = False
						return

				elif player == 2:
					if board[coordinates[1].index(y1) - a][coordinates[0].index(x1) + a] == "B1" or board[coordinates[1].index(y1) - a][coordinates[0].index(x1) + a] == "Q1":  # Collision Checker
						checked = True
						no_error = False
						return
				break
			a += 1

	if coordinates[1].index(y1) > 0 and coordinates[0].index(x1) > 0:  # Loop on King's X-Y+ Side (Cartesian Orientation)
		# X component is disregarded. Only Y component is needed to compute for the number of iteration
		b = 1
		end_y2 = 0
		if coordinates[0].index(x1) > coordinates[1].index(y1):  # if King is in + Side of Left-Right Diagonal
			end_y2 = 0

		elif coordinates[0].index(x1) < coordinates[1].index(y1):  # if King is in - Side of Left-Right Diagonal
			end_y2 = 0 + (coordinates[1].index(y1) - (coordinates[0].index(x1) + 1))

		elif coordinates[0].index(x1) == coordinates[1].index(y1):
			end_y2 = coordinates[1].index(y1)

		for i in range(coordinates[1].index(y1) - end_y2):  # Tiles between King and Max Diagonal location
			if board[coordinates[1].index(y1) - b][coordinates[0].index(x1) - b] != "  ":
				if player == 1:
					if board[coordinates[1].index(y1) - 1][coordinates[0].index(x1) - 1] == "P2":
						checked = True
						no_error = False
						return
					elif board[coordinates[1].index(y1) - b][coordinates[0].index(x1) - b] == "B2" or board[coordinates[1].index(y1) - b][coordinates[0].index(x1) - b] == "Q2":  # Collision Checker
						checked = True
						no_error = False
						return
				elif player == 2:
					if board[coordinates[1].index(y1) - b][coordinates[0].index(x1) - b] == "B1" or board[coordinates[1].index(y1) - b][coordinates[0].index(x1) - b] == "Q1":  # Collision Checker
						checked = True
						no_error = False
						return
				break
			b += 1

	if coordinates[1].index(y1) < 7 and coordinates[0].index(x1) > 0:  # Loop on King's X-Y- Side (Cartesian Orientation)
		# X component is disregarded. Only Y component is needed to compute for the number of iteration
		c = 1
		end_y3 = 0
		if coordinates[0].index(x1) + coordinates[1].index(y1) < 7:  # if King is in - Side of Right-Left Diagonal
			end_y3 = 0 + ((7 - coordinates[1].index(y1) + 1) - coordinates[0].index(x1))

		elif coordinates[0].index(x1) + coordinates[1].index(y1) > 7:  # if King is in + Side of Right-Left Diagonal
			end_y3 = 7

		elif coordinates[0].index(x1) + coordinates[1].index(y1) == 7:
			end_y3 = 7 - coordinates[1].index(y1)

		for i in range(end_y3 - coordinates[1].index(y1)):  # Tiles between King and Max Diagonal location
			if board[coordinates[1].index(y1) + c][coordinates[0].index(x1) - c] != "  ":
				if player == 1:
					if board[coordinates[1].index(y1) + c][coordinates[0].index(x1) - c] == "B2" or board[coordinates[1].index(y1) + c][coordinates[0].index(x1) - c] == "Q2":  # Collision Checker
						checked = True
						no_error = False
						return
				elif player == 2:
					if board[coordinates[1].index(y1) + 1][coordinates[0].index(x1) - 1] == "P1":
						checked = True
						no_error = False
						return
					elif board[coordinates[1].index(y1) + c][coordinates[0].index(x1) - c] == "B1" or board[coordinates[1].index(y1) + c][coordinates[0].index(x1) - c] == "Q1":  # Collision Checker
						checked = True
						no_error = False
						return
				break
			c += 1

	if coordinates[1].index(y1) < 7 and coordinates[0].index(x1) < 7:  # Loop on King's X+Y- Side (Cartesian Orientation)
		# X component is disregarded. Only Y component is needed to compute for the number of iteration
		d = 1
		end_y4 = 0
		if coordinates[0].index(x1) > coordinates[1].index(y1):  # if King is in + Side of Left-Right Diagonal
			end_y4 = 7 - (coordinates[0].index(x1) - (coordinates[1].index(y1) + 1) + 1)

		elif coordinates[0].index(x1) < coordinates[1].index(y1):  # if King is in - Side of Left-Right Diagonal
			end_y4 = 7
		elif coordinates[0].index(x1) == coordinates[1].index(y1):
			end_y4 = 7 - coordinates[1].index(y1)

		for i in range(end_y4 - coordinates[1].index(y1)):  # Tiles between King and Max Diagonal location
			if board[coordinates[1].index(y1) + d][coordinates[0].index(x1) + d] != "  ":
				if player == 1:
					if board[coordinates[1].index(y1) + d][coordinates[0].index(x1) + d] == "B2" or board[coordinates[1].index(y1) + d][coordinates[0].index(x1) + d] == "Q2":  # Collision Checker
						checked = True
						no_error = False
						return
				elif player == 2:
					if board[coordinates[1].index(y1) + 1][coordinates[0].index(x1) + 1] == "P1":
						checked = True
						no_error = False
						return
					elif board[coordinates[1].index(y1) + d][coordinates[0].index(x1) + d] == "B1" or board[coordinates[1].index(y1) + d][coordinates[0].index(x1) + d] == "Q1":  # Collision Checker
						checked = True
						return
				break
			d += 1

		if coordinates[1].index(y1) > 0 and coordinates[0].index(x1) < 6:
			# Check for presence of Knight in King's X++Y+ Side
			if player == 1:
				if board[coordinates[1].index(y1) - 1][coordinates[0].index(x1) + 2] == "K2":
					checked = True
					no_error = False
					return
			elif player == 2:
				if board[coordinates[1].index(y1) - 1][coordinates[0].index(x1) + 2] == "K1":
					checked = True
					no_error = False
					return

		if coordinates[1].index(y1) > 1 and coordinates[0].index(x1) < 7:
			# Check for presence of Knight in King's X+Y++ Side
			if player == 1:
				if board[coordinates[1].index(y1) - 2][coordinates[0].index(x1) + 1] == "K2":
					checked = True
					no_error = False
					return
			elif player == 2:
				if board[coordinates[1].index(y1) - 2][coordinates[0].index(x1) + 1] == "K1":
					checked = True
					no_error = False
					return

		if coordinates[1].index(y1) > 0 and coordinates[0].index(x1) > 1:
			# Check for presence of Knight in King's X--Y+ Side
			if player == 1:
				if board[coordinates[1].index(y1) - 1][coordinates[0].index(x1) - 2] == "K2":
					checked = True
					no_error = False
					return
			elif player == 2:
				if board[coordinates[1].index(y1) - 1][coordinates[0].index(x1) - 2] == "K1":
					checked = True
					no_error = False
					return

		if coordinates[1].index(y1) > 1 and coordinates[0].index(x1) > 0:
			# Check for presence of Knight in King's X-Y++ Side
			if player == 1:
				if board[coordinates[1].index(y1) - 2][coordinates[0].index(x1) - 1] == "K2":
					checked = True
					no_error = False
					return
			elif player == 2:
				if board[coordinates[1].index(y1) - 2][coordinates[0].index(x1) - 1] == "K1":
					checked = True
					no_error = False
					return

		if coordinates[1].index(y1) < 7 and coordinates[0].index(x1) > 1:
			# Check for presence of Knight in King's X--Y- Side
			if player == 1:
				if board[coordinates[1].index(y1) + 1][coordinates[0].index(x1) - 2] == "K2":
					checked = True
					no_error = False
					return
			elif player == 2:
				if board[coordinates[1].index(y1) + 1][coordinates[0].index(x1) - 2] == "K1":
					checked = True
					no_error = False
					return

		if coordinates[1].index(y1) < 6 and coordinates[0].index(x1) > 0:
			# Check for presence of Knight in King's X-Y-- Side
			if player == 1:
				if board[coordinates[1].index(y1) + 2][coordinates[0].index(x1) - 1] == "K2":
					checked = True
					no_error = False
					return
			elif player == 2:
				if board[coordinates[1].index(y1) + 2][coordinates[0].index(x1) - 1] == "K1":
					checked = True
					no_error = False
					return

		if coordinates[1].index(y1) < 7 and coordinates[0].index(x1) < 6:
			# Check for presence of Knight in King's X++Y- Side
			if player == 1:
				if board[coordinates[1].index(y1) + 1][coordinates[0].index(x1) + 2] == "K2":
					checked = True
					no_error = False
					return
			elif player == 2:
				if board[coordinates[1].index(y1) + 1][coordinates[0].index(x1) + 2] == "K1":
					checked = True
					no_error = False
					return

		if coordinates[1].index(y1) < 6 and coordinates[0].index(x1) < 7:
			# Check for presence of Knight in King's X+Y-- Side
			if player == 1:
				if board[coordinates[1].index(y1) + 2][coordinates[0].index(x1) + 1] == "K2":
					checked = True
					no_error = False
					return
			elif player == 2:
				if board[coordinates[1].index(y1) + 2][coordinates[0].index(x1) + 1] == "K1":
					checked = True
					no_error = False
					return


def virtual_move(x1, y1, x2, y2, alt):
	global board
	global coordinates
	global king_x
	global king_y

	captured_piece = ""

	find_king(alt)  # Find location of a player's King

	# Executes the code
	captured_piece = board[coordinates[1].index(y2)][coordinates[0].index(x2)]
	board[coordinates[1].index(y2)][coordinates[0].index(x2)] = board[coordinates[1].index(y1)][coordinates[0].index(x1)]
	board[coordinates[1].index(y1)][coordinates[0].index(x1)] = "  "

	# Checks if King is in Checked State after making the move
	check(king_x, king_y, alt)

	# Returns the pieces to their original position before move execution
	board[coordinates[1].index(y1)][coordinates[0].index(x1)] = board[coordinates[1].index(y2)][coordinates[0].index(x2)]
	board[coordinates[1].index(y2)][coordinates[0].index(x2)] = captured_piece


def pawn_promotion(y1, x2, y2, alt):
	global board
	global coordinates

	if alt == 1:
		if y1 == "7" and y2 == "8":
			print("\n---Pawn Promotion---")
			print("1. Knight")
			print("2. Bishop")
			print("3. Rook")
			print("4. Queen")
			choice = int(input("Please Select what kind of piece would you want your pawn be promoted: "))
			if choice == 1:
				board[coordinates[1].index(y2)][coordinates[0].index(x2)] = "K1"
				board_print(board, coordinates)
				print("Pawn is Promoted to Knight.")
				return
			elif choice == 2:
				board[coordinates[1].index(y2)][coordinates[0].index(x2)] = "B1"
				board_print(board, coordinates)
				print("Pawn is Promoted to Bishop.")
				return
			elif choice == 3:
				board[coordinates[1].index(y2)][coordinates[0].index(x2)] = "R1"
				board_print(board, coordinates)
				print("Pawn is Promoted to Rook.")
				return
			elif choice == 4:
				board[coordinates[1].index(y2)][coordinates[0].index(x2)] = "Q1"
				board_print(board, coordinates)
				print("Pawn is Promoted to Queen.")
				return

	elif alt == 2:
		if y1 == "2" and y2 == "1":
			print("\n---Pawn Promotion---")
			print("1. Knight")
			print("2. Bishop")
			print("3. Rook")
			print("4. Queen")
			choice = int(input("Please Select what kind of piece would you want your pawn be promoted: "))
			if choice == 1:
				board[coordinates[1].index(y2)][coordinates[0].index(x2)] = "K2"
				board_print(board, coordinates)
				print("Pawn is Promoted to Knight.")
				return
			elif choice == 2:
				board[coordinates[1].index(y2)][coordinates[0].index(x2)] = "B2"
				board_print(board, coordinates)
				print("Pawn is Promoted to Bishop.")
				return
			elif choice == 3:
				board[coordinates[1].index(y2)][coordinates[0].index(x2)] = "R2"
				board_print(board, coordinates)
				print("Pawn is Promoted to Rook.")
				return
			elif choice == 4:
				board[coordinates[1].index(y2)][coordinates[0].index(x2)] = "Q2"
				board_print(board, coordinates)
				print("Pawn is Promoted to Queen.")
				return


def scorer(x2, y2, alt):
	global p1_score
	global p2_score

	if alt == 1:
		if board[coordinates[1].index(y2)][coordinates[0].index(x2)] == "P2":
			p1_score = p1_score + 1
			return
		elif board[coordinates[1].index(y2)][coordinates[0].index(x2)] == "K2":
			p1_score = p1_score + 3
			return
		elif board[coordinates[1].index(y2)][coordinates[0].index(x2)] == "B2":
			p1_score = p1_score + 4
			return
		elif board[coordinates[1].index(y2)][coordinates[0].index(x2)] == "R2":
			p1_score = p1_score + 5
			return
		elif board[coordinates[1].index(y2)][coordinates[0].index(x2)] == "Q2":
			p1_score = p1_score + 7
			return

	elif alt == 2:
		if board[coordinates[1].index(y2)][coordinates[0].index(x2)] == "P1":
			p2_score = p2_score + 1
			return
		elif board[coordinates[1].index(y2)][coordinates[0].index(x2)] == "K1":
			p2_score = p2_score + 3
			return
		elif board[coordinates[1].index(y2)][coordinates[0].index(x2)] == "B1":
			p2_score = p2_score + 4
			return
		elif board[coordinates[1].index(y2)][coordinates[0].index(x2)] == "R1":
			p2_score = p2_score + 5
			return
		elif board[coordinates[1].index(y2)][coordinates[0].index(x2)] == "Q1":
			p2_score = p2_score + 7
			return


def checkmate(x1, y1, alt):
	global checked
	global coordinates
	global board
	global end

	check(x1, y1, alt)
	if checked:
		if coordinates[1].index(y1) > 0 and (board[coordinates[1].index(y1)-1][coordinates[0].index(x1)])[1] != str(alt):  # North
			virtual_move(x1, y1, x1, coordinates[1][coordinates[1].index(y1) - 1], alt)
			if checked:
				end = True
			else:
				end = False
				return

		if coordinates[1].index(y1) > 0 and coordinates[0].index(x1) < 7 and (board[coordinates[1].index(y1)-1][coordinates[0].index(x1) + 1])[1] != str(alt):  # North East
			virtual_move(x1, y1, coordinates[0][coordinates[0].index(x1) + 1], coordinates[1][coordinates[1].index(y1) - 1], alt)
			if checked:
				end = True
			else:
				end = False
				return

		if coordinates[1].index(y1) > 0 and coordinates[0].index(x1) > 0 and (board[coordinates[1].index(y1)-1][coordinates[0].index(x1) - 1])[1] != str(alt):  # North West
			virtual_move(x1, y1, coordinates[0][coordinates[0].index(x1) - 1], coordinates[1][coordinates[1].index(y1) - 1], alt)
			if checked:
				end = True
			else:
				end = False
				return

		if coordinates[0].index(x1) < 7 and (board[coordinates[1].index(y1)][coordinates[0].index(x1) + 1])[1] != str(alt):  # East
			virtual_move(x1, y1, coordinates[0][coordinates[0].index(x1) + 1], y1, alt)
			if checked:
				end = True
			else:
				end = False
				return

		if coordinates[0].index(x1) > 0 and (board[coordinates[1].index(y1)][coordinates[0].index(x1) - 1])[1] != str(alt):  # West
			virtual_move(x1, y1, coordinates[0][coordinates[0].index(x1) - 1], y1, alt)
			if checked:
				end = True
			else:
				end = False
				return

		if coordinates[1].index(y1) < 7 and (board[coordinates[1].index(y1) + 1][coordinates[0].index(x1)])[1] != str(alt):  # South
			virtual_move(x1, y1, x1, coordinates[1][coordinates[1].index(y1) + 1], alt)
			if checked:
				end = True
			else:
				end = False
				return

		if coordinates[1].index(y1) < 7 and coordinates[0].index(x1) < 7 and (board[coordinates[1].index(y1) + 1][coordinates[0].index(x1) + 1])[1] != str(alt):  # South East
			virtual_move(x1, y1, coordinates[0][coordinates[0].index(x1) + 1], coordinates[1][coordinates[1].index(y1) + 1], alt)
			if checked:
				end = True
			else:
				end = False
				return

		if coordinates[1].index(y1) < 7 and coordinates[0].index(x1) > 0 and (board[coordinates[1].index(y1) + 1][coordinates[0].index(x1) - 1]) != str(alt):  # South West
			virtual_move(x1, y1, coordinates[0][coordinates[0].index(x1) - 1], coordinates[1][coordinates[1].index(y1) + 1], alt)
			if checked:
				end = True
			else:
				end = False
				return


def save_board(file):
	global board
	save = open(file, "w")

	for i in board:
		save.write(i[0] + ",")
		save.write(i[1] + ",")
		save.write(i[2] + ",")
		save.write(i[3] + ",")
		save.write(i[4] + ",")
		save.write(i[5] + ",")
		save.write(i[6] + ",")
		save.write(i[7] + "\n")

	save.close()
	print("Game Data Saved Successfully.")


def load_board(file):
	global board
	new_board = []  # Creates a temporary storage of data generated from text file
	load = open(file, "r")

	for line in load:
		data = line[:-1].split(",")
		new_board = new_board + [[data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7]]]

	board = new_board
	load.close()
	print("Game Data Loaded Successfully.")
