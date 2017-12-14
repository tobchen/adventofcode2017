data = []
# from previous result
with open('file.txt') as file:
	for line in file.read().splitlines():
		data.append([int(x) for x in line])

groups = 0

def fill(i, j):
	if not 0 <= i < 128 or not 0 <= j < 128 or data[i][j] == 0:
		return
	data[i][j] = 0
	fill(i-1, j)
	fill(i+1, j)
	fill(i, j-1)
	fill(i, j+1)

for y in range(128):
	for x in range(128):
		if data[y][x] == 1:
			groups += 1
			fill(y, x)

print(groups)
