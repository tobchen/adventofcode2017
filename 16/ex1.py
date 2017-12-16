progs = [chr(97 + i) for i in range(16)]

def spin(s):
	global progs
	progs = progs[-s:] + progs[:16 - s]

def swap1(ab):
	global progs
	progs[ab[0]], progs[ab[1]] = progs[ab[1]], progs[ab[0]]

def swap2(ab):
	global progs
	a = progs.index(ab[0])
	b = progs.index(ab[1])
	progs[a], progs[b] = progs[b], progs[a]

dance = []
with open('file.txt') as file:
	for step in file.read().split(','):
		if step[0] == 's':
			dance.append([spin, int(step[1:])])
		elif step[0] == 'x':
			ab = step[1:].split('/')
			dance.append([swap1, (int(ab[0]), int(ab[1]))])
		elif step[0] == 'p':
			ab = step[1:].split('/')
			dance.append([swap2, (ab[0], ab[1])])

for step in dance:
	step[0](step[1])

result = ""
for p in progs:
	result += p
print(result)
