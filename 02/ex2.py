rows = []
with open('file2.txt') as fp:
	line = fp.readline()
	while line:
		l = line.split('\t')
		rows.append([])
		for c in l:
			rows[-1].append(int(c))
		line = fp.readline()

s = 0
for row in rows:
	go_on = False
	for i in range(len(row)):
		if go_on:
			break
		for j in range(len(row)):
			if i != j and row[i] % row[j] == 0:
				s += int(row[i] / row[j])
				go_on = True
				break

print(s)
