def main():

    # Parse problem input
    input_fp = "./input.txt"
    passphrases = []
    with open(input_fp, 'r') as input_file:
        for line in input_file:
            line = line.replace('\n', '')
            passphrases.append(line)

    valid_count = 0
    for passphrase in passphrases:
        words = passphrase.split(" ")
        unique_words = set()
        valid = True
        for word in words:
            if word in unique_words:
                valid = False
                break
            else:
                unique_words.add(word)
        valid_count += 1 if valid else 0
    
    print("The answer is: " + str(valid_count))



if __name__ == "__main__":
    main()
