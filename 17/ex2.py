no = 0
pos = 0

for i in range(1, 50000001):
	pos = ((pos + 367) % i) + 1
	if pos == 1:
		no = i

print(no)