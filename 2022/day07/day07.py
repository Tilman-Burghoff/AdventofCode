# Day 7

directionary = {}

testdata = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""

with open('day07_input.txt') as f:
    current = directionary
    path = [directionary]
    ls = False
    for line in f:#testdata.split('\n'):
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

print(total_size, dirsizes)