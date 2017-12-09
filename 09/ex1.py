with open('file.txt') as file:
	stream = file.read()

# stream = '<{o"i!a,<{i<a>'

score = 0
group_depth = 0
in_garbage = False
in_escape = False
garbage = 0
for c in stream:
	if in_escape:
		in_escape = False
		continue

	if c == '!':
		in_escape = True
	elif c == '<' and not in_garbage:
		in_garbage = True
	elif c == '>' and in_garbage:
		in_garbage = False
	elif c == '{' and not in_garbage:
		group_depth += 1
	elif c == '}' and not in_garbage and group_depth > 0:
		score += group_depth
		group_depth -= 1
	elif in_garbage:
		garbage += 1

print(score, garbage)
