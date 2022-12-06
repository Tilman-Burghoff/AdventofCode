# Day 3

def get_priotity(item):
	return ord(item) - 96 if item.islower() else ord(item) - 38

print(get_priotity('A'))
	
with open('day03_input.txt') as f:
	"""
	totalPart1 = 0
	for line in f:
		line = line[:-1]
		compartment1, compartment2 = set(line[:len(line)//2]), set(line[len(line)//2:])
		commonItem, = compartment1.intersection(compartment2)
		totalPart1 += get_priotity(commonItem)
	print("Part 1:", totalPart1)
	"""
	
	totalPart2 = 0
	fileIter = iter(f)
	for line in fileIter:
		elf1, elf2, elf3 = set(line[:-1]), set(next(fileIter)[:-1]), set(next(fileIter)[:-1])
		print(elf1.intersection(elf2).intersection(elf3))
		badge, = elf1.intersection(elf2).intersection(elf3)
		totalPart2 += get_priotity(badge)
	print("Part 2:", totalPart2)