# Day 2

def rps_winner(me, opponent):
	"""
	0 rock, 1 paper, 2 scissors.
	return 1 if win, 0 if draw, -1 if lost.
	solve (opponent + x mod 3) = me for smallest x
	"""
	return (me - opponent + 1) % 3 - 1
	
	
getindex = {'A': 0, 'B': 1, 'C': 2, 'X': 0, 'Y': 1, 'Z': 2}
points = {'X': 1, 'Y': 2, 'Z': 3}

# proof that rps_winner works	
for i in range(3):
	print([rps_winner(i, j) for j in range(3)])
	
with open('day02_input.txt') as f:
	totalPart1 = 0
	totalPart2 = 0
	for line in f:
		opponent, me = line[:-1].split(' ')
		totalPart1 += 3 + 3 * rps_winner(getindex[me], getindex[opponent]) + points[me]
		totalPart2 += {'X' : 0, 'Y' : 3, 'Z' : 6}[me]
		totalPart2 += [[3, 1, 2], [1, 2, 3], [2, 3, 1]][getindex[opponent]][getindex[me]]
		
	print("part 1:", totalPart1)
	print("part 2:", totalPart2)