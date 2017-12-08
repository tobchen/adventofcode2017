import re

def equalto(a, b):
	return a == b

def greaterthan(a, b):
	return a > b

def lesserthan(a, b):
	return a < b

def greq(a, b):
	return a >= b

def leeq(a, b):
	return a <= b

def unequalto(a, b):
	return a != b

def increase(a, b):
	return a + b

def decrease(a, b):
	return a - b

conditions = {"==": equalto, ">": greaterthan, "<": lesserthan, ">=": greq, "<=": leeq, "!=": unequalto}
operations = {"inc": increase, "dec": decrease}
registers = dict()

with open('file.txt') as file:
	data = file.read().splitlines()

atmax = 0
for line in data:
	m = re.search('([a-z]+) (.+) (-?[0-9]+) if ([a-z]+) (.+) (-?[0-9]+)', line)
	if conditions[m.group(5)](registers.get(m.group(4), 0), int(m.group(6))):
		registers[m.group(1)] = operations[m.group(2)](registers.get(m.group(1), 0), int(m.group(3)))

	if len(registers) > 0:
		cmax = max(registers.values())
		if cmax > atmax:
			atmax = cmax

print("Current max:", max(registers.values()))
print("All-time max:", atmax)
