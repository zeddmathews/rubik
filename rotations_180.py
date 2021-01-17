def front_180(rotated_front, front, rotated_left, down, rotated_up, left, rotated_right, up, rotated_down, right):
	# front
	rotated_front[0][0] = front[2][2]
	rotated_front[0][1] = front[2][1]
	rotated_front[0][2] = front[2][0]

	rotated_front[1][2] = front[1][0]

	rotated_front[2][2] = front[0][0]
	rotated_front[2][1] = front[0][1]
	rotated_front[2][0] = front[0][2]

	rotated_front[1][0] = front[1][2]

	# left
	rotated_left[0][2] = right[2][0]
	rotated_left[1][2] = right[1][0]
	rotated_left[2][2] = right[0][0]

	# up
	rotated_up[2][0] = down[0][2]
	rotated_up[2][1] = down[0][1]
	rotated_up[2][2] = down[0][0]

	# right
	rotated_right[0][0] = left[2][2]
	rotated_right[1][0] = left[1][2]
	rotated_right[2][0] = left[0][2]

	# down
	rotated_down[0][0] = up[2][2]
	rotated_down[0][1] = up[2][1]
	rotated_down[0][2] = up[2][0]

	return rotated_front, rotated_left, rotated_up, rotated_right, rotated_down

def back_180(rotated_back, back, rotated_left, down, rotated_up, left, rotated_right, up, rotated_down, right):
	# back
	rotated_back[0][0] = back[2][2]
	rotated_back[0][1] = back[2][1]
	rotated_back[0][2] = back[2][0]

	rotated_back[1][2] = back[1][0]

	rotated_back[2][2] = back[0][0]
	rotated_back[2][1] = back[0][1]
	rotated_back[2][0] = back[0][2]

	rotated_back[1][0] = back[1][2]

	# right
	rotated_right[0][2] = left[2][0]
	rotated_right[1][2] = left[1][0]
	rotated_right[2][2] = left[0][0]

	# up
	rotated_up[0][2] = down[2][0]
	rotated_up[0][1] = down[2][1]
	rotated_up[0][0] = down[2][2]

	# left
	rotated_left[0][0] = right[2][2]
	rotated_left[1][0] = right[1][2]
	rotated_left[2][0] = right[0][2]

	# down
	rotated_down[2][2] = up[0][0]
	rotated_down[2][1] = up[0][1]
	rotated_down[2][0] = up[0][2]

	return rotated_back, rotated_left, rotated_up, rotated_right, rotated_down

def left_180(rotated_back, back, rotated_left, down, rotated_up, left, rotated_front, up, rotated_down, front):
	# left
	rotated_left[0][0] = left[2][2]
	rotated_left[0][1] = left[2][1]
	rotated_left[0][2] = left[2][0]

	rotated_left[1][2] = left[1][0]

	rotated_left[2][2] = left[0][0]
	rotated_left[2][1] = left[0][1]
	rotated_left[2][0] = left[0][2]

	rotated_left[1][0] = left[1][2]

	# up
	rotated_up[0][0] = down[0][0]
	rotated_up[1][0] = down[1][0]
	rotated_up[2][0] = down[2][0]

	# down
	rotated_down[2][0] = up[2][0]
	rotated_down[1][0] = up[1][0]
	rotated_down[0][0] = up[0][0]

	# back
	rotated_back[0][2] = front[2][0]
	rotated_back[1][2] = front[1][0]
	rotated_back[2][2] = front[0][0]

	# front
	rotated_front[0][0] = back[2][2]
	rotated_front[1][0] = back[1][2]
	rotated_front[2][0] = back[0][2]

	return rotated_back, rotated_left, rotated_up, rotated_front, rotated_down

def right_180(rotated_back, back, rotated_right, down, rotated_up, right, rotated_front, up, rotated_down, front):
	# right
	rotated_right[0][0] = right[2][2]
	rotated_right[0][1] = right[2][1]
	rotated_right[0][2] = right[2][0]

	rotated_right[1][2] = right[1][0]

	rotated_right[2][2] = right[0][0]
	rotated_right[2][1] = right[0][1]
	rotated_right[2][0] = right[0][2]

	rotated_right[1][0] = right[1][2]

	# up
	rotated_up[2][2] = down[2][2]
	rotated_up[1][2] = down[1][2]
	rotated_up[0][2] = down[0][2]

	# down
	rotated_down[2][2] = up[2][2]
	rotated_down[1][2] = up[1][2]
	rotated_down[0][2] = up[0][2]

	# back
	rotated_back[0][0] = front[2][2]
	rotated_back[1][0] = front[1][2]
	rotated_back[2][0] = front[0][2]

	# front
	rotated_front[2][2] = back[0][0]
	rotated_front[1][2] = back[1][0]
	rotated_front[0][2] = back[2][0]

	return rotated_back, rotated_right, rotated_up, rotated_front, rotated_down

def up_180(rotated_back, back, rotated_right, left, rotated_up, right, rotated_front, up, rotated_left, front):
	# up
	rotated_up[0][0] = up[2][2]
	rotated_up[0][1] = up[2][1]
	rotated_up[0][2] = up[2][0]

	rotated_up[1][2] = up[1][0]

	rotated_up[2][2] = up[0][0]
	rotated_up[2][1] = up[0][1]
	rotated_up[2][0] = up[0][2]

	rotated_up[1][0] = up[1][2]

	# front
	rotated_front[0][0] = back[0][0]
	rotated_front[0][1] = back[0][1]
	rotated_front[0][2] = back[0][2]

	# back
	rotated_back[0][0] = front[0][0]
	rotated_back[0][1] = front[0][1]
	rotated_back[0][2] = front[0][2]

	# left
	rotated_left[0][0] = right[0][0]
	rotated_left[0][1] = right[0][1]
	rotated_left[0][2] = right[0][2]

	# right
	rotated_right[0][0] = left[0][0]
	rotated_right[0][1] = left[0][1]
	rotated_right[0][2] = left[0][2]

	return rotated_back, rotated_right, rotated_up, rotated_front, rotated_left

def down_180(rotated_back, back, rotated_right, left, rotated_down, right, rotated_front, down, rotated_left, front):
	# down
	rotated_down[0][0] = down[2][2]
	rotated_down[0][1] = down[2][1]
	rotated_down[0][2] = down[2][0]

	rotated_down[1][2] = down[1][0]

	rotated_down[2][2] = down[0][0]
	rotated_down[2][1] = down[0][1]
	rotated_down[2][0] = down[0][2]

	rotated_down[1][0] = down[1][2]

	# front
	rotated_front[2][0] = back[2][0]
	rotated_front[2][1] = back[2][1]
	rotated_front[2][2] = back[2][2]

	# back
	rotated_back[2][0] = front[2][0]
	rotated_back[2][1] = front[2][1]
	rotated_back[2][2] = front[2][2]

	# left
	rotated_left[2][0] = right[2][0]
	rotated_left[2][1] = right[2][1]
	rotated_left[2][2] = right[2][2]

	# right
	rotated_right[2][0] = left[2][0]
	rotated_right[2][1] = left[2][1]
	rotated_right[2][2] = left[2][2]

	return rotated_back, rotated_right, rotated_down, rotated_front, rotated_left