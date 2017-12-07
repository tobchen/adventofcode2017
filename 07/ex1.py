with open('file1.txt') as file:
	data = file.read().splitlines()

name_called = []
for line in data:
	if ' -> ' in line:
		children = line.split(' -> ')[1].split(', ')
		name_called.extend(children)

for line in data:
	date = line.split(' ')[0]
	if date not in name_called:
		print(date)
