# Day 6

with open('day06_input.txt') as f:
    LENGTH_UNIQUE_STRING = 14
    data = f.read()

    for i in range(LENGTH_UNIQUE_STRING,len(data)):
        if len(set(data[i-LENGTH_UNIQUE_STRING:i])) == LENGTH_UNIQUE_STRING:
            print(f"string{i, data[i-LENGTH_UNIQUE_STRING:i])
            break
    else:
        print("no string found")