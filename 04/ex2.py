rows = []
with open('file2.txt') as fp:
	lines = fp.readlines()
	for line in lines:
		spl = line[0:-1].split(' ')
		row = []
		for word in spl:
			row.append(''.join(sorted([c for c in word])))
		rows.append(row)

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
