ga = 289
gb = 629

count = 0

for i in range(5000000):
	ga = (ga * 16807) % 2147483647
	while ga % 4 != 0: # Y YU DON HAVE DO-WHILE, PYTHON???
		ga = (ga * 16807) % 2147483647
	gb = (gb * 48271) % 2147483647
	while gb % 8 != 0:
		gb = (gb * 48271) % 2147483647
	if ga & 65535 == gb & 65535:
		count += 1

print(count)
