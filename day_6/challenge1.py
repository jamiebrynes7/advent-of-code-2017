def main():

    # Parse problem input
    input_fp = "./input.txt"
    banks = []
    with open(input_fp, 'r') as input_file:
        for bank in input_file.read().split('\t'):
            banks.append(int(bank))

    unique_generations = set()
    unique_generations.add(serializeBanks(banks))

    redistribution_count = 0
    while True:
        redistribution_count += 1
        redistributeMemory(banks)
        serialized_banks = serializeBanks(banks)
        if serialized_banks in unique_generations:
            break
        unique_generations.add(serialized_banks)
    
    print("The answer is: " + str(redistribution_count))



def serializeBanks(banks):
    serialization = ""
    for bank in banks:
        serialization += str(bank) + "."
    
    return serialization

def redistributeMemory(banks):

    # Setup    
    redis_mem = max(banks)
    index = banks.index(redis_mem)
    banks[index] = 0

    index = (index + 1) % len(banks)

    for i in range(redis_mem):
        banks[index] += 1
        index = (index + 1) % len(banks)

if __name__ == "__main__":
    main()
