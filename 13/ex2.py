scanners = dict()
last = 0
with open('file.txt') as file:
	for line in file.read().splitlines():
		data = [int(x) for x in line.split(": ")]
		scanners[data[0]] = data[1]
		last = max(last, data[0])

delay = 0
cont = True
while cont:
	cont = False
	for key in scanners:
		if (delay + key) % ((scanners[key] - 1) * 2) == 0:
			cont = True
			break
	delay += 1

print(delay - 1)
