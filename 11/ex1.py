import re

def calc_steps(x, y):
	if abs(x) >= abs(y):
		return abs(x)
	else:
		return abs(abs(y) - abs(x)) / 2 + abs(x)

with open('file.txt') as file:
	data = [x for x in file.read().split(',')]

# data = "ne,ne,s,s".split(',')

furthest = 0

x = y = 0
for step in data:
	if step == 'nw':
		x -= 1
		y -= 1
	elif step == 'n':
		y -= 2
	elif step == 'ne':
		x += 1
		y -= 1
	elif step == 'se':
		x += 1
		y += 1
	elif step == 's':
		y += 2
	elif step == 'sw':
		x -= 1
		y += 1

	furthest = max(furthest, calc_steps(x, y))

print(x, ",", y, ", steps:", calc_steps(x, y), ", furthest:", furthest)
