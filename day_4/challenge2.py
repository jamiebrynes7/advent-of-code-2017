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
        for word in words:
            valid = True
            word_token = serializeWord(word)
            if word_token in unique_words:
                valid = False
                break
            else:
                unique_words.add(word_token)
        
        valid_count += 1 if valid else 0
    
    print("The answer is: " + str(valid_count))

def serializeWord(word):

    letter_to_count = dict()
    for letter in word:
        if letter in letter_to_count:
            letter_to_count[letter] += 1
        else:
            letter_to_count[letter] = 1
    
    word_token = ""
    for key in sorted(letter_to_count.keys()):
        word_token += key + str(letter_to_count[key])
    
    return word_token


if __name__ == "__main__":
    main()
