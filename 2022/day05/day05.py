# Day 5

with open('day05_input.txt') as f:
	data = f.read()

stacksUnparsed, procedure = data.split("\n\n")

# parse stacks
stacksUnparsed = stacksUnparsed.split(" 1")[0]
no_of_stacks = 9
stacks = [[] for _ in range(no_of_stacks)]
for i in range(len(stacksUnparsed)//4):
	item = stacksUnparsed[4*i:4*(i+1)]
	if item not in ("    ", "   \n"):
		stacks[i%no_of_stacks].insert(0, item[1])

		
		
		

for command in procedure.split('\n')[:-1]:
	count, fro, to = [int(command.split(' ')[i]) for i in [1,3,5]]
	"""# part 1:
	for i in range(count):
		stacks[to - 1].append(stacks[fro - 1].pop())
	"""
	stacks[to - 1].extend(stacks[fro - 1][-count:])
	del stacks[fro - 1][-count:]

print("".join([stack.pop() for stack in stacks]))
