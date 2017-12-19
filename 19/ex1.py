with open('file.txt') as file:
	route = file.read().splitlines()

d = 0 # 0 down, 1 up, 2 left, 3 right

x, y = route[0].index('|'), 0

r = ""
r2 = 0

def walk():
	global d, x, y, r2
	if d == 0:
		y += 1
	elif d == 1:
		y -= 1
	elif d == 2:
		x -= 1
	elif d == 3:
		x += 1
	r2 += 1

while True:
	if route[y][x] == '+':
		if 0 <= d <= 1:
			if route[y][x-1] == '-':
				d = 2
			else:
				d = 3
		elif 2 <= d <= 3:
			if route[y-1][x] == '|':
				d = 1
			else:
				d = 0
		walk()
	elif route[y][x] == '-' or route[y][x] == '|':
		walk()
	elif route[y][x] == ' ':
		break
	else:
		r += route[y][x]
		walk()

print(r, r2)
