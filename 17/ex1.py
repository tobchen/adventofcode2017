b = [0]
pos = 0

for i in range(1, 2018):
	pos = (pos + 367) % len(b)
	b.insert(pos + 1, i)
	pos += 1

print(b[(pos + 1) % len(b)])