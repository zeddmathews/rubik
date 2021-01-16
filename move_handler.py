from rotations import *
from ccw_rotations import *
from rotations_180 import *

# seems like more effort than it's worth

def front_handler(move, rotated_front, front, rotated_left, down, rotated_up, left, rotated_right, up, rotated_down, right):
	if (len(move) == 1):
		rotated_front, rotated_left, rotated_up, rotated_right, rotated_down = front_cw(rotated_front, front, rotated_left, down, rotated_up, left, rotated_right, up, rotated_down, right)
	elif (len(move) == 2 and move[1] == '\''):
		rotated_front, rotated_left, rotated_up, rotated_right, rotated_down = front_ccw(rotated_front, front, rotated_left, down, rotated_up, left, rotated_right, up, rotated_down, right)
		print('ccw')
	elif (len(move) == 2 and move[1] == '2'):
		rotated_front, rotated_left, rotated_up, rotated_right, rotated_down = front_180(rotated_front, front, rotated_left, down, rotated_up, left, rotated_right, up, rotated_down, right)
		print('180')

def back_handler(move, rotated_back, back, rotated_left, down, rotated_up, left, rotated_right, up, rotated_down, right):
	if (len(move) == 1):
		rotated_back, rotated_left, rotated_up, rotated_right, rotated_down = back_cw(rotated_back, back, rotated_left, down, rotated_up, left, rotated_right, up, rotated_down, right)
	elif (len(move) == 2 and move[1] == '\''):
		rotated_back, rotated_left, rotated_up, rotated_right, rotated_down = back_ccw(rotated_back, back, rotated_left, down, rotated_up, left, rotated_right, up, rotated_down, right)
		print('ccw')
	elif (len(move) == 2 and move[1] == '2'):
		rotated_back, rotated_left, rotated_up, rotated_right, rotated_down = back_180(rotated_back, back, rotated_left, down, rotated_up, left, rotated_right, up, rotated_down, right)
		print('180')

def left_handler(move, rotated_back, back, rotated_left, down, rotated_up, left, rotated_front, up, rotated_down, front):
	if (len(move) == 1):
		rotated_back, rotated_left, rotated_up, rotated_front, rotated_down = left_cw(rotated_back, back, rotated_left, down, rotated_up, left, rotated_front, up, rotated_down, front)
	elif (len(move) == 2 and move[1] == '\''):
		rotated_back, rotated_left, rotated_up, rotated_front, rotated_down = left_ccw(rotated_back, back, rotated_left, down, rotated_up, left, rotated_front, up, rotated_down, front)
		print('ccw')
	elif (len(move) == 2 and move[1] == '2'):
		rotated_back, rotated_left, rotated_up, rotated_front, rotated_down = left_180(rotated_back, back, rotated_left, down, rotated_up, left, rotated_front, up, rotated_down, front)
		print('180')

def right_handler(move, rotated_back, back, rotated_right, down, rotated_up, right, rotated_front, up, rotated_down, front):
	if (len(move) == 1):
		rotated_back, rotated_right, rotated_up, rotated_front, rotated_down = right_cw(rotated_back, back, rotated_right, down, rotated_up, right, rotated_front, up, rotated_down, front)
	elif (len(move) == 2 and move[1] == '\''):
		rotated_back, rotated_right, rotated_up, rotated_front, rotated_down = right_ccw(rotated_back, back, rotated_right, down, rotated_up, right, rotated_front, up, rotated_down, front)
		print('ccw')
	elif (len(move) == 2 and move[1] == '2'):
		rotated_back, rotated_right, rotated_up, rotated_front, rotated_down = right_180(rotated_back, back, rotated_right, down, rotated_up, right, rotated_front, up, rotated_down, front)
		print('180')

def up_handler(move, rotated_back, back, rotated_right, left, rotated_up, right, rotated_front, up, rotated_left, front):
	if (len(move) == 1):
		rotated_back, rotated_right, rotated_up, rotated_front, rotated_left = up_cw(rotated_back, back, rotated_right, left, rotated_up, right, rotated_front, up, rotated_left, front)
	elif (len(move) == 2 and move[1] == '\''):
		rotated_back, rotated_right, rotated_up, rotated_front, rotated_left = up_ccw(rotated_back, back, rotated_right, left, rotated_up, right, rotated_front, up, rotated_left, front)
		print('ccw')
	elif (len(move) == 2 and move[1] == '2'):
		rotated_back, rotated_right, rotated_up, rotated_front, rotated_left = up_180(rotated_back, back, rotated_right, left, rotated_up, right, rotated_front, up, rotated_left, front)
		print('180')

def down_handler(move, rotated_back, back, rotated_right, left, rotated_down, right, rotated_front, down, rotated_left, front):
	if (len(move) == 1):
		rotated_back, rotated_right, rotated_down, rotated_front, rotated_left = down_cw(rotated_back, back, rotated_right, left, rotated_down, right, rotated_front, down, rotated_left, front)
	elif (len(move) == 2 and move[1] == '\''):
		rotated_back, rotated_right, rotated_down, rotated_front, rotated_left = down_ccw(rotated_back, back, rotated_right, left, rotated_down, right, rotated_front, down, rotated_left, front)
		print('ccw')
	elif (len(move) == 2 and move[1] == '2'):
		rotated_back, rotated_right, rotated_down, rotated_front, rotated_left = down_180(rotated_back, back, rotated_right, left, rotated_down, right, rotated_front, down, rotated_left, front)
		print('180')