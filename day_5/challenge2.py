def main():

    # Parse problem input
    input_fp = "./input.txt"
    instructions = []
    with open(input_fp, 'r') as input_file:
        for line in input_file:
            line = line.replace('\n', '')
            instructions.append(int(line))

    current_pos = 0
    steps = 0
    while True:
        steps += 1
        next_pos = current_pos + instructions[current_pos]
        instructions[current_pos] += 1 if instructions[current_pos] < 3 else -1
        current_pos = next_pos
        if current_pos >= len(instructions):
            break
    
    print("The answer is: " + str(steps))



if __name__ == "__main__":
    main()
