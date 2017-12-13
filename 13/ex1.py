scanners = dict()
last = 0
with open('file.txt') as file:
	for line in file.read().splitlines():
		data = [int(x) for x in line.split(": ")]
		scanners[data[0]] = [data[1], 0, +1]
		last = max(last, data[0])

severity = 0
pos = -1
while pos <= last:
	pos += 1
	if pos in scanners and scanners[pos][1] == 0:
		severity += pos * scanners[pos][0]
	for key in scanners:
		scanners[key][1] += scanners[key][2]
		if scanners[key][1] == 0:
			scanners[key][2] = +1
		if scanners[key][1] == scanners[key][0] - 1:
			scanners[key][2] = -1

print(severity)
