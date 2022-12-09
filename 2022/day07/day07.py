# Day 7

directionary = {}

with open('day07_input.txt') as f:
    current = directionary
    path = [directionary]
    ls = False
    for line in f:
        tokens = line[:-1].split(' ')
        if tokens[0] == '$':
            if tokens[1] == 'cd':
                if tokens[2] == '/':
                    current = directionary
                    path = []
                elif tokens[2] == '..':
                    current = path.pop()
                else:
                    path.append(current)
                    current = current[tokens[2]]
        else:
            if tokens[0] == 'dir':
                current[tokens[1]] = {}
            else:
                current[tokens[1]] = int(tokens[0])


dirsizes = []
def recursive_dir_size(directionary, dirsizes):
    size = 0
    for fileorsubdir in directionary.values():
        if type(fileorsubdir) == type(0):
            size += fileorsubdir
        else:
            size += recursive_dir_size(fileorsubdir, dirsizes)
    dirsizes.append(size)
    return size

dirsizes = []
total_size = recursive_dir_size(directionary, dirsizes)

print("Part 1:", sum([size for size in dirsizes if size <= 100000]))
print("Part 2:", min([size for size in dirsizes if size >= total_size - 40000000]))