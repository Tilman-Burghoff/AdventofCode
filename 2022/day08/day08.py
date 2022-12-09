# Day 8

with open('day08_input.txt') as f:
    data = f.readlines()

#data = ["30373\n", "25512\n", "65332\n", "33549\n", "35390\n"]

height = len(data)
width = len(data[0]) - 1

tree_visible = [[False]*width for _ in range(height)]

top = [-1] * height
bottom = [-1] * height
left = [-1] * width
right = [-1] * width

for i in range(height):
    for j in range(width):
        topleft = int(data[i][j])
        topright = int(data[i][-2-j])
        bottomleft = int(data[-1-i][j])

        if  topleft > top[j]:
            tree_visible[i][j] = True
            top[j] = topleft
        if bottomleft > bottom[j]:
            tree_visible[-1-i][j] = True
            bottom[j] = bottomleft
        if topleft > left[i]:
            tree_visible[i][j] = True
            left[i] = topleft
        if topright > right[i]:
            tree_visible[i][-1-j] = True
            right[i] = topright

print(sum([sum(row) for row in tree_visible]))