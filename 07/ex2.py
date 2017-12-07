with open('file1.txt') as file:
	data = file.read().splitlines()

def bt(root):
	for i in range(len(data)):
		if data[i].startswith(root):
			index = i
			break

	children = []
	if ' -> ' in data[i]:
		for child in data[i].split(' -> ')[1].split(', '):
			children.append(bt(child))

	name = data[i].split(' ')[0]
	weight = int(data[i].split('(')[1].split(')')[0])

	return {"name": name, "weight": weight, "children": children}

def weight(tr):
	w = tr["weight"]
	wc = []
	for child in tr["children"]:
		wc.append(weight(child))
	if len(wc) > 0 and min(wc) != max(wc):
		print(wc)
		for c in tr["children"]:
			print(c["name"])
	for wcc in wc:
		w += wcc
	return w

tree = bt("vgzejbd") # Known from previous gold star
weight(tree)
