# Day 9
import numpy as np

def move_segment(head_pos, tail_pos):
    difference = head_pos - tail_pos
    if not np.max(np.abs(head_pos - tail_pos)) <= 1:
        tail_pos += np.sign(difference)
    
LENGHT_OF_ROPE = 10
rope = [np.array([0,0]) for _ in range(LENGHT_OF_ROPE)]

visited = set()
visited.add((0,0))

direction_to_arr = {'U': np.array([1,0]), 'D': np.array([-1,0]), 
    'R': np.array([0,1]), 'L': np.array([0,-1])}

with open('day09_input.txt') as f:
    for line in f:
        direction, count = line.split()

        for _ in range(int(count)):
            rope[0] += direction_to_arr[direction]
            prev_seg = rope[0]
            for segment in rope[1:]:
                move_segment(prev_seg, segment)
                prev_seg = segment
            visited.add(tuple(rope[-1]))

print(len(visited))
