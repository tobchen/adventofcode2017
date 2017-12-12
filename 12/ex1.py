progs = dict()
with open('file.txt') as file:
	for line in file.read().splitlines():
		data = line.split(' <-> ')
		progs[int(data[0])] = [int(x) for x in data[1].split(', ')]

nullset = set([0])
changed = True
while (changed):
	changed = False
	oldlen = len(nullset)
	newset = set()
	for prog in nullset:
		newset.update(progs[prog])
	nullset.update(newset)
	changed = oldlen != len(nullset)

print(len(nullset))
