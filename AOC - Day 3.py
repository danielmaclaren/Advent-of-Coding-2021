## Binary Diagnostic ##

f = open("binarydiagnostic.txt","r")
instruction = f.read().split("\n")

def binarydiagnostic():
    gamma_rate = []
    epsilon_rate = []

    for position in range(len(instruction[1])): 
        test = []

        for binary_value in instruction:
            test.append(binary_value[position])
        print(test)
        ones = test.count('1')
        zeroes = test.count('0') 

        if ones > zeroes:
            gamma_rate.append(1)
            epsilon_rate.append(0)
        elif zeroes > ones:
            gamma_rate.append(0)
            epsilon_rate.append(1)

    gamma_value = 0
    gamma_rate.reverse()
    for binary_position, bit_value in enumerate(gamma_rate):
        gamma_value += bit_value * (2**binary_position)

    epsilon_value = 0
    epsilon_rate.reverse()
    for binary_position, bit_value in enumerate(epsilon_rate):
        epsilon_value += bit_value * (2**binary_position)

    print('Gamma Binary Value: ', gamma_rate)
    print('Epsilon Binary Value: ', epsilon_rate)

    print('Gamma Value:', gamma_value)
    print('Epsilon Value:', epsilon_value)
    print('Power Consumption:', gamma_value*epsilon_value)


binarydiagnostic()
