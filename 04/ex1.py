rows = []
with open('file1.txt') as fp:
	line = fp.readline()
	while line:
		rows.append(line[0:-1].split(' '))
		line = fp.readline()

c = 0
for row in rows:
	same = False
	for i in range(len(row)):
		for j in range(len(row)):
			if i != j and row[i] == row[j]:
				same = True
				break
		if same:
			break
	if not same:
		c += 1

print(c)
