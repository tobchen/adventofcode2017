with open('file.txt') as file:
	instructions = file.read().splitlines()

regs = dict()

last_freq = 0
last_recv = 0

def get_value(val):
	global regs
	try:
		return int(val)
	except ValueError:
		return regs.get(val, 0)

pos = 0
while 0 <= pos < len(instructions):
	ins = instructions[pos].split(' ')
	if ins[0] == 'snd':
		last_freq = get_value(ins[1])
	elif ins[0] == 'set':
		regs[ins[1]] = get_value(ins[2])
	elif ins[0] == 'add':
		regs[ins[1]] = regs.get(ins[1], 0) + get_value(ins[2])
	elif ins[0] == 'mul':
		regs[ins[1]] = regs.get(ins[1], 0) * get_value(ins[2])
	elif ins[0] == 'mod':
		regs[ins[1]] = regs.get(ins[1], 0) % get_value(ins[2])
	elif ins[0] == 'rcv':
		if get_value(ins[1]) != 0:
			last_recv = last_freq
			break
	elif ins[0] == 'jgz':
		if get_value(ins[1]) > 0:
			pos += get_value(ins[2])
			continue
	pos += 1

print(last_recv)
