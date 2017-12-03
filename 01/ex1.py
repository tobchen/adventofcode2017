c = "1212"

c_list = []
for l in c:
	c_list.append(int(l))

s = 0
for i in range(-1, len(c_list) - 1):
	if c_list[i] == c_list[i+1]:
		s += c_list[i]

print(s)