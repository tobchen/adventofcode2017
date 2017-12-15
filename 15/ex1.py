ga = 289
gb = 629

count = 0

for i in range(40000000):
	ga = (ga * 16807) % 2147483647
	gb = (gb * 48271) % 2147483647
	if ga & 65535 == gb & 65535:
		count += 1

print(count)
