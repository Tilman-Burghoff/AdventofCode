""" https://www.reddit.com/r/adventofcode/comments/z9i581/python_script_creator_tool/ """

import sys
import os

if __name__ == '__main__':
    sys.path.append('..')
    year = input('Enter year: ')
    # create folders for the days and the py files
    if not os.path.exists(year):
	    os.makedirs(year)
    with open(f"{year}/stars.txt", "w") as f:
        f.writelines([f"Day{i:02}: 0/2\n" for i in range(1,26)])

    for i in range(1, 26):
        if not os.path.exists(f"{year}/day{i:02}"):
            os.makedirs(f"{year}/day{i:02}")
			
            f = open(f"{year}/day{i:02}/day{i:02}.py", 'w')
            f. write(f"# Day {i}\n\nwith open('day{i:02}_input.txt') as f:\n    pass")
            f.close()
			
            f = open(f"{year}/day{i:02}//day{i:02}_input.txt", 'w')
            f.close()