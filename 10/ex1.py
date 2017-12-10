lengths = [int(x) for x in "46,41,212,83,1,255,157,65,139,52,39,254,2,86,0,204".split(',')]
numbers = [x for x in range(256)]
#lengths = [int(x) for x in "3,4,1,5".split(',')]
#numbers = [x for x in range(5)]
skip = pos = 0

for length in lengths:
	for i in range(int(length / 2)):
		numbers[(pos + i) % len(numbers)], numbers[(pos + length - i - 1) % len(numbers)] =\
		numbers[(pos + length - i - 1) % len(numbers)], numbers[(pos + i) % len(numbers)]
	pos += skip + length
	skip += 1

# print(numbers)
print(numbers[0] * numbers[1])