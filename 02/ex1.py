s = 0
with open('file.txt') as fp:
	line = fp.readline()
	while line:
		l = line.split('\t')
		mn = mx = int(l[0])
		for c in l:
			n = int(c)
			if n < mn:
				mn = n
			if n > mx:
				mx = n
		s += mx-mn
		line = fp.readline()

print(s)
