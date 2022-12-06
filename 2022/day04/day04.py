# Day 4

with open('day04_input.txt') as f:
	totalPart1 = 0
	totalPart2 = 0
	for line in f:
		elf1, elf2 = line[:-1].split(',')
		lowerBoundElf1, upperBoundElf1 = map(int, elf1.split('-'))
		lowerBoundElf2, upperBoundElf2 = map(int, elf2.split('-'))
		
		if lowerBoundElf1 <= lowerBoundElf2 and upperBoundElf1 >= upperBoundElf2:
			totalPart1 += 1
		elif lowerBoundElf2 <= lowerBoundElf1 and upperBoundElf2 >= upperBoundElf1:
			totalPart1 += 1
			
		if lowerBoundElf1 <= lowerBoundElf2 <= upperBoundElf1:
			totalPart2 += 1
		elif lowerBoundElf1 <= upperBoundElf2 <= upperBoundElf1:
			totalPart2 += 1
		elif lowerBoundElf2 <= lowerBoundElf1 <= upperBoundElf2:
			totalPart2 += 1 # intervall 2 contains intervall 1 whole
		
	print("Part 1:", totalPart1)
	print("Part 2:", totalPart2)