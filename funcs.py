# Put your functions in here.
# Feel free to run your design past me before beginning to implement.

def check_up(puzzle, row, col, word): # row and col given by the searcher that finds the index of the first char in the words
    i = 0;

    while puzzle[row][col] == word[i]:
    	i += 1;
    	row -= 1;
    	if i == len(word):
    		return True;
    	elif row < 0 and i != len(word):
    		break

    return False;

def check_down(puzzle, row, col, word):
    i = 0; 

    while puzzle[row][col] == word[i]:
    	i += 1;
    	row += 1;
    	if i == len(word):
    		return True;
    	elif row > 9 and i != len(word):
    		return False;

    return False
   
def check_forward(puzzle, row, col, word):
    i = 0;

    while puzzle[row][col] == word[i]:
    	i += 1;
    	col += 1;
    	if i == len(word):
    		return True;
    	elif col > 9 and i != len(word):
    		return False;

    return False;

def check_backward(puzzle, row, col, word):
    i = 0;

    while puzzle[row][col] == word[i]:
    	i += 1;
    	col -= 1;
    	if i == len(word):
    		return True;
    	elif col < 0 and i != len(word):
    		return False;

    return False;

def check_diagonal(puzzle, row, col, word):
    i = 0;

    while puzzle[row][col] == word[i]:
    	i += 1;
    	row += 1;
    	col += 1;
    	if i == len(word):
    		return True;
    	elif (row > 9 or col > 9) and i != len(word):
    		return False;

    return False;

def get_locations_c(puzzle, c): #c is the first char in every word
	# return loc as tuple in a list
	loc = []
	for row in range(10):
		for char in range(10):
			if puzzle[row][char] == c:
				loc.append((row, char));

	return loc;

def check_all(puzzle, row, col, word):
	if check_up(puzzle, row, col, word):
		print("%s: (UP) row: %d column: %d" % (word, row, col))

	elif check_down(puzzle, row, col, word):
		print("%s: (DOWN) row: %d column: %d" % (word, row, col))

	elif check_forward(puzzle, row, col, word):
		print("%s: (FORWARD) row: %d column: %d" % (word, row, col))

	elif check_backward(puzzle, row, col, word):
		print("%s: (BACKWARD) row: %d column: %d" % (word, row, col))

	elif check_diagonal(puzzle, row, col, word):
		print("%s: (DIAGONAL) row: %d column: %d" % (word, row, col))
	else:
		return False

	return True



	 






