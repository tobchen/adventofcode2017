lengths = [ord(x) for x in "46,41,212,83,1,255,157,65,139,52,39,254,2,86,0,204"] + [17, 31, 73, 47, 23]
numbers = [x for x in range(256)]
#lengths = [int(x) for x in "3,4,1,5".split(',')]
#numbers = [x for x in range(5)]
skip = pos = 0

for i in range(64):
	for length in lengths:
		for i in range(int(length / 2)):
			numbers[(pos + i) % len(numbers)], numbers[(pos + length - i - 1) % len(numbers)] =\
			numbers[(pos + length - i - 1) % len(numbers)], numbers[(pos + i) % len(numbers)]
		pos += skip + length
		skip += 1

	# Afraid of overflow without having it tested even once
	while pos >= 256:
		pos -= 256

final_hash = ''
for i in range(16):
	tmp = 0
	for j in range(16):
		tmp = tmp ^ numbers[i * 16 + j]
	tmp = str(hex(tmp)).split('x')[1]
	if len(tmp) < 2:
		tmp = '0' + tmp
	final_hash += tmp

print(final_hash)