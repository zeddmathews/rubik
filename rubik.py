import sys

av = sys.argv

def limit_argv(av):
	if (len(av) != 2):
		sys.exit('Invalid number of args')

def valid_rotations(av):
	valid_notations = ['F', 'R', 'U', 'B', 'L', 'D'] #front, right, up, back, left, down
	valid_prime = ['\'', '2'] #
	err = []
	cube = av[0].split()
	print(f'cube: {cube}')
	for notation in cube:
		if (len(notation) > 2):
			err.append('length of \"' + notation + '\" must be <= 2')
		if (notation[0].upper() not in valid_notations):
			err.append('notation \"' + notation[0] + ' (' + notation + ')\" not found')
		if (len(notation) == 2):
			if (notation[1] not in valid_prime):
				err.append('prime \"' + notation[1] + ' (' + notation + ')\" not found')
	if (len(err) > 0):
		for error in err:
			print(f'Invalid: {error}')
		sys.exit()
	display_scrambled_cube(cube)

def display_scrambled_cube(moves):
	front = [
		['1white', '2white', '3white'], #edge with up
		['4white', '5white', '6white'],
		['7white', '8white', '9white'] #edge with down
	]
	back = [
		['1yellow', '2yellow', '3yellow'], #edge with up
		['4yellow', '5yellow', '6yellow'],
		['7yellow', '8yellow', '9yellow'] #edge with down
	]
	right = [
		['1blue', '2blue', '3blue'], #edge with up
		['4blue', '5blue', '6blue'],
		['7blue', '8blue', '9blue'] #edge with down
	]
	left = [
		['1green', '2green', '3green'], #edge with up
		['4green', '5green', '6green'],
		['7green', '8green', '9green'] #edge with down
	]
	up = [
		['1orange', '2orange', '3orange'], #edge with back
		['4orange', '5orange', '6orange'],
		['7orange', '8orange', '9orange'] #edge with front
	]
	down = [
		['1red', '2red', '3red'], #edge with back
		['4red', '5red', '6red'],
		['7red', '8red', '9red'] #edge with front
	]

	rotated_front = [
		['1white', '2white', '3white'], #edge with up
		['4white', '5white', '6white'],
		['7white', '8white', '9white'] #edge with down
	]
	rotated_back = [
		['1yellow', '2yellow', '3yellow'], #edge with up
		['4yellow', '5yellow', '6yellow'],
		['7yellow', '8yellow', '9yellow'] #edge with down
	]
	rotated_right = [
		['1blue', '2blue', '3blue'], #edge with up
		['4blue', '5blue', '6blue'],
		['7blue', '8blue', '9blue'] #edge with down
	]
	rotated_left = [
		['1green', '2green', '3green'], #edge with up
		['4green', '5green', '6green'],
		['7green', '8green', '9green'] #edge with down
	]
	rotated_up = [
		['1orange', '2orange', '3orange'], #edge with back
		['4orange', '5orange', '6orange'],
		['7orange', '8orange', '9orange'] #edge with front
	]
	rotated_down = [
		['1red', '2red', '3red'], #edge with back
		['4red', '5red', '6red'],
		['7red', '8red', '9red'] #edge with front
	]

	#[row][block]
	for move in moves:
		if (move.upper().startswith('F')):
			if (len(move) == 1):
				# front
				rotated_front[0][0] = front[2][0]
				rotated_front[0][1] = front[1][0]
				rotated_front[0][2] = front[0][0]

				rotated_front[1][2] = front[0][1]

				rotated_front[2][2] = front[0][2]
				rotated_front[2][1] = front[1][2]
				rotated_front[2][0] = front[2][2]

				rotated_front[1][0] = front[2][1]

				#left
				rotated_left[0][2] = down[0][0]
				rotated_left[1][2] = down[0][1]
				rotated_left[2][2] = down[0][2]

				#up
				rotated_up[2][0] = left[2][2]
				rotated_up[2][1] = left[1][2]
				rotated_up[2][2] = left[0][2]

				#right
				rotated_right[0][0] = up[2][0]
				rotated_right[1][0] = up[2][1]
				rotated_right[2][0] = up[2][2]

				#down
				rotated_down[0][0] = right[2][0]
				rotated_down[0][1] = right[1][0]
				rotated_down[0][2] = right[0][0]

		if (move.upper().startswith('B')):
			if (len(move) == 1):
				# back
				rotated_back[0][0] = back[2][0]
				rotated_back[0][1] = back[1][0]
				rotated_back[0][2] = back[0][0]

				rotated_back[1][2] = back[0][1]

				rotated_back[2][2] = back[0][2]
				rotated_back[2][1] = back[1][2]
				rotated_back[2][0] = back[2][2]

				rotated_back[1][0] = back[2][1]

				#right
				rotated_right[0][2] = down[2][2]
				rotated_right[1][2] = down[2][1]
				rotated_right[2][2] = down[2][0]

				#up
				rotated_up[0][0] = right[2][2]
				rotated_up[0][1] = right[1][2]
				rotated_up[0][2] = right[0][2]

				#left
				rotated_left[0][0] = up[0][2]
				rotated_left[1][0] = up[0][1]
				rotated_left[2][0] = up[0][0]

				#down
				rotated_down[2][2] = left[2][0]
				rotated_down[2][1] = left[1][0]
				rotated_down[2][0] = left[0][0]

		if (move.upper().startswith('L')):
			if (len(move) == 1):
				# left
				rotated_left[0][0] = left[2][0]
				rotated_left[0][1] = left[1][0]
				rotated_left[0][2] = left[0][0]

				rotated_left[1][2] = left[0][1]

				rotated_left[2][2] = left[0][2]
				rotated_left[2][1] = left[1][2]
				rotated_left[2][0] = left[2][2]

				rotated_left[1][0] = left[2][1]

		if (move.upper().startswith('R')):
			if (len(move) == 1):
				# right
				rotated_right[0][0] = right[2][0]
				rotated_right[0][1] = right[1][0]
				rotated_right[0][2] = right[0][0]

				rotated_right[1][2] = right[0][1]

				rotated_right[2][2] = right[0][2]
				rotated_right[2][1] = right[1][2]
				rotated_right[2][0] = right[2][2]

				rotated_right[1][0] = right[2][1]

		if (move.upper().startswith('U')):
			if (len(move) == 1):
				# up
				rotated_up[0][0] = up[2][0]
				rotated_up[0][1] = up[1][0]
				rotated_up[0][2] = up[0][0]

				rotated_up[1][2] = up[0][1]

				rotated_up[2][2] = up[0][2]
				rotated_up[2][1] = up[1][2]
				rotated_up[2][0] = up[2][2]

				rotated_up[1][0] = up[2][1]

		if (move.upper().startswith('D')):
			if (len(move) == 1):
				# down
				rotated_down[0][0] = down[2][0]
				rotated_down[0][1] = down[1][0]
				rotated_down[0][2] = down[0][0]

				rotated_down[1][2] = down[0][1]

				rotated_down[2][2] = down[0][2]
				rotated_down[2][1] = down[1][2]
				rotated_down[2][0] = down[2][2]

				rotated_down[1][0] = down[2][1]

	# print(f'face: {base_cube[0]}')
	# for face in base_cube:
	# 	for row in face:
	# 		print(f'cube: {row}')
	# for face in rotated_cube:
	# 	for row in face:
	# 		print(f'rotated: {row}')


def rubik(av):
	av.pop(0) #remove rubik.py from list
	valid_rotations(av)
	print(f'sum\'ing')

if (__name__ == '__main__'):
	limit_argv(av)
	rubik(av)