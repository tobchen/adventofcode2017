banks = [int(x) for x in "0	5	10	0	11	14	13	4	11	8	8	7	1	4	12	11".split('\t')]
states = []

while banks not in states:
	states.append(list(banks))
	value = max(banks)
	index = banks.index(value)
	banks[index] = 0
	while value > 0:
		index = index + 1
		if index >= len(banks):
			index = 0
		banks[index] += 1
		value -= 1

print(len(states) - states.index(banks))
