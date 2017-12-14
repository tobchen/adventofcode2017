# ripped right out of #10
def knot(key):
	lengths = [ord(x) for x in key] + [17, 31, 73, 47, 23]
	numbers = [x for x in range(256)]
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

	return final_hash

puzzle = "ffayrhll"
hb = {
	"0": "0000",
	"1": "0001",
	"2": "0010",
	"3": "0011",
	"4": "0100",
	"5": "0101",
	"6": "0110",
	"7": "0111",
	"8": "1000",
	"9": "1001",
	"a": "1010",
	"b": "1011",
	"c": "1100",
	"d": "1101",
	"e": "1110",
	"f": "1111"
}

used = 0
for i in range(128):
	h = knot(puzzle + "-" + str(i))
	line = ""
	for c in h:
		line += hb[c]
	print(line)
	for c in line:
		if c == '1':
			used += 1

print(used)