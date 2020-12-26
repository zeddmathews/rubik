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

def rubik(av):
	av.pop(0) #remove rubik.py from list
	valid_rotations(av)
	print(f'sum\'ing')

if (__name__ == '__main__'):
	limit_argv(av)
	rubik(av)