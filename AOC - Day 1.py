### Sonar Sweep ###

f = open("sonarsweep.txt","r")
instruction = f.read().split("\n")
print(instruction)

def depthmeasure(instruction):
    count_increase = 0
    count_decrease = 0

    
    for i, depth in enumerate(instruction): 
        if i == len(instruction)-1:
            print('Count Increase: ', count_increase)
            print('Count Decrease: ', count_decrease)

        else: 
            if int(depth) < int(instruction[i+1]):
                count_increase += 1    
            elif int(depth) > int(instruction[i+1]):
                count_decrease += 1


depthmeasure(instruction)