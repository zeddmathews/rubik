import sys

from move_handler import *
from copy import deepcopy

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
		['1red', '2red', '3red'], #edge with front
		['4red', '5red', '6red'],
		['7red', '8red', '9red'] #edge with back
	]
	i = 1
	for move in moves:
		if (move.upper().startswith('F')):
			front_handler(move, rotated_front, front, rotated_left, down, rotated_up, left, rotated_right, up, rotated_down, right)

		elif (move.upper().startswith('B')):
			back_handler(move, rotated_back, back, rotated_left, down, rotated_up, left, rotated_right, up, rotated_down, right)

		elif (move.upper().startswith('L')):
			left_handler(move, rotated_back, back, rotated_left, down, rotated_up, left, rotated_front, up, rotated_down, front)

		elif (move.upper().startswith('R')):
			right_handler(move, rotated_back, back, rotated_right, down, rotated_up, right, rotated_front, up, rotated_down, front)

		elif (move.upper().startswith('U')):
			up_handler(move, rotated_back, back, rotated_right, left, rotated_up, right, rotated_front, up, rotated_left, front)

		elif (move.upper().startswith('D')):
			down_handler(move, rotated_back, back, rotated_right, left, rotated_down, right, rotated_front, down, rotated_left, front)
		front = deepcopy(rotated_front)
		back = deepcopy(rotated_back)
		right = deepcopy(rotated_right)
		left = deepcopy(rotated_left)
		up = deepcopy(rotated_up)
		down = deepcopy(rotated_down)
		# print(f'{i} rotation: {front}\n')
		# print(f'{i} rotation: {back}\n')
		# print(f'{i} rotation: {right}\n')
		# print(f'{i} rotation: {left}\n')
		# print(f'{i} rotation: {up}\n')
		# print(f'{i} rotation: {down}\n')
		consolidated_base_cube = [front, back, right, left, up, down]
		# consolidated_rotated_cube = [rotated_front, rotated_back, rotated_right, rotated_left, rotated_up, rotated_down]
		for face in consolidated_base_cube:
			for row in face:
				print(f'{i} rotation: {row}')
			print('')
		print('\n')
		# for face in consolidated_rotated_cube:
		# 	for row in face:
		# 		print(f'{i} rotation: {row}')
		# 	print('')
		i += 1



def rubik(av):
	av.pop(0) #remove rubik.py from list
	valid_rotations(av)
	print(f'sum\'ing')

if (__name__ == '__main__'):
	limit_argv(av)
	rubik(av)