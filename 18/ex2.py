with open('file.txt') as file:
	instructions = file.read().splitlines()

regs0 = {"p": 0}
regs1 = {"p": 1}

def get_value0(val):
	global regs0
	try:
		return int(val)
	except ValueError:
		return regs0.get(val, 0)

def get_value1(val):
	global regs1
	try:
		return int(val)
	except ValueError:
		return regs1.get(val, 0)

count = 0

qu0 = list()
qu1 = list()
pos0 = 0
pos1 = 0
while True:
	dead0 = True
	while 0 <= pos0 < len(instructions):
		ins = instructions[pos0].split(' ')
		if ins[0] == 'snd':
			qu1.insert(0, get_value0(ins[1]))
		elif ins[0] == 'set':
			regs0[ins[1]] = get_value0(ins[2])
		elif ins[0] == 'add':
			regs0[ins[1]] = regs0.get(ins[1], 0) + get_value0(ins[2])
		elif ins[0] == 'mul':
			regs0[ins[1]] = regs0.get(ins[1], 0) * get_value0(ins[2])
		elif ins[0] == 'mod':
			regs0[ins[1]] = regs0.get(ins[1], 0) % get_value0(ins[2])
		elif ins[0] == 'rcv':
			if len(qu0) > 0:
				regs0[ins[1]] = qu0.pop()
			else:
				break
		elif ins[0] == 'jgz':
			if get_value0(ins[1]) > 0:
				pos0 += get_value0(ins[2])
				dead0 = False
				continue
		pos0 += 1
		dead0 = False

	dead1 = True
	while 0 <= pos1 < len(instructions):
		ins = instructions[pos1].split(' ')
		if ins[0] == 'snd':
			count += 1
			qu0.insert(0, get_value1(ins[1]))
		elif ins[0] == 'set':
			regs1[ins[1]] = get_value1(ins[2])
		elif ins[0] == 'add':
			regs1[ins[1]] = regs1.get(ins[1], 0) + get_value1(ins[2])
		elif ins[0] == 'mul':
			regs1[ins[1]] = regs1.get(ins[1], 0) * get_value1(ins[2])
		elif ins[0] == 'mod':
			regs1[ins[1]] = regs1.get(ins[1], 0) % get_value1(ins[2])
		elif ins[0] == 'rcv':
			if len(qu1) > 0:
				regs1[ins[1]] = qu1.pop()
			else:
				break
		elif ins[0] == 'jgz':
			if get_value1(ins[1]) > 0:
				pos1 += get_value1(ins[2])
				dead1 = False
				continue
		pos1 += 1
		dead1 = False

	if dead0 and dead1:
		break

print(count)
