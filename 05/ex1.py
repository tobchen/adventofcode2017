with open('file1.txt') as file:
	jumps, head, count = [int(x) for x in file.read().splitlines()], 0, 0

while 0 <= head < len(jumps):
	jumps[head], head, count = jumps[head] + 1, head + jumps[head], count + 1

print(count)
