## Dive! ##

f = open("divedata.txt","r")
instruction = f.read().split("\n")

def dive():
    horizontal = 0
    depth = 0
    aim = 0

    for x in instruction:
        x = x.split(' ')
        if x[0] == 'forward':
            horizontal += int(x[1])
            depth += aim * int(x[1])
        elif x[0] == 'down':
            aim += int(x[1])
        elif x[0] == 'up':
            aim -= int(x[1])

    print('Final Horizontal: ', horizontal)
    print('Final Depth: ', depth)
    print('Final Position: ', depth*horizontal)

dive()