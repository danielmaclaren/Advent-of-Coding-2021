### Sonar Sweep ###
### This took way too long, decided to combine every 3 items in the list and then use that to create a new list, using the previous code to check ###

f = open("sonarsweep.txt","r")
instruction = f.read().split("\n")

#instruction = [199,200,208,210,200,207,240,269,260,263]

def depthmeasure(instruction):
    count_increase = 0
    count_decrease = 0
    window = []

    for i in range(len(instruction)-2):
        window_item = int(instruction[i]) + int(instruction[i+1]) + int(instruction[i+2])
        window.append(window_item)
 
    for i, combined_depth in enumerate(window):
        if i == len(window)-1:
            print('Count Increase: ', count_increase)
            print('Count Decrease: ', count_decrease)

        else: 
            if int(combined_depth) < int(window[i+1]):
                count_increase += 1    
            elif int(combined_depth) > int(window[i+1]):
                count_decrease += 1


depthmeasure(instruction)