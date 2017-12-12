progs = dict()
with open('file.txt') as file:
	for line in file.read().splitlines():
		data = line.split(' <-> ')
		progs[int(data[0])] = [int(x) for x in data[1].split(', ')]

groups = 0
while (len(progs) > 0):
	nullset = set([list(progs.keys())[0]])
	changed = True
	while (changed):
		changed = False
		oldlen = len(nullset)
		newset = set()
		for prog in nullset:
			newset.update(progs[prog])
		nullset.update(newset)
		changed = oldlen != len(nullset)
	for prog in nullset:
		progs.pop(prog)
	groups += 1

print(groups)
