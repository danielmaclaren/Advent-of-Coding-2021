## Binary Diagnostic ##

f = open("binarydiagnostic.txt","r")
instruction = f.read().split("\n")

def oxygen_rating():
    oxygen_rate = instruction.copy()
    for position in range(len(instruction[1])): 
        oxygen_test = []

        for binary_value in oxygen_rate:
            if binary_value == 'None':
                oxygen_test.append('')
                pass
            else:
                oxygen_test.append(binary_value[position])
        ones = oxygen_test.count('1')
        zeroes = oxygen_test.count('0') 

        if ones > zeroes or  ones == zeroes:
            for i, value in enumerate(oxygen_test):
                if value == '0':
                    oxygen_rate[i] = 'None'

        elif zeroes > ones:
            for i, value in enumerate(oxygen_test):
                if value == '1':
                    oxygen_rate[i] = 'None'

        final_check = [x for x in oxygen_rate if x != 'None']
        if len(final_check) == 1:
            oxygen_generator_rating = list(map(int,final_check[0]))
            oxygen_value = 0
            oxygen_generator_rating.reverse()
            for binary_position, bit_value in enumerate(oxygen_generator_rating):
                oxygen_value += bit_value * (2**binary_position)
            return oxygen_value

def carbon_rating():
    carbon_rate = instruction.copy()
    for position in range(len(instruction[1])): 
        carbon_test = []

        for binary_value in carbon_rate:
            if binary_value == 'None':
                carbon_test.append('')
                pass
            else:
                carbon_test.append(binary_value[position])
        ones = carbon_test.count('1')
        zeroes = carbon_test.count('0') 

        if ones > zeroes or ones == zeroes:
            for i, value in enumerate(carbon_test):
                if value == '1':
                    carbon_rate[i] = 'None'
        elif zeroes > ones:
            for i, value in enumerate(carbon_test):
                if value == '0':
                    carbon_rate[i] = 'None'

        final_check = [x for x in carbon_rate if x != 'None']
        if len(final_check) == 1:
            carbon_generator_rating = list(map(int,final_check[0]))
            carbon_value = 0
            carbon_generator_rating.reverse()
            for binary_position, bit_value in enumerate(carbon_generator_rating):
                carbon_value += bit_value * (2**binary_position)
            return carbon_value

def life_support():
    oxygen = oxygen_rating()
    carbon = carbon_rating()
    life_support_rating = carbon * oxygen
    print(life_support_rating)

oxygen_rating()
carbon_rating()
life_support()
