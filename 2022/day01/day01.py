# -*- coding: utf-8 -*-

with open('input.txt') as f:
    raw = f.read()

data = raw.split('\n\n')
sums = []
for block in data:
    sums.append(sum(map(int, block.split('\n'))))

sums.sort()

print(sums[-1])

print(sum(sums[-3:]))

print(max([sum(map(int, s.split('\n'))) for s in raw.split('\n\n')]))