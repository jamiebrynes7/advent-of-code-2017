import re 
def main():
    stream = None
    with open('./input.txt', 'r') as input_file:
        stream = input_file.read()

    stack = []
    groups = 0
    score = 0
    garbage = False
    i = 0
    while i < len(stream):
        c = stream[i]
        if c == "!":
            i+= 1
        elif garbage:
            if c == ">":
                garbage = False
        elif c == "{":
            score += 1
            stack.append(score)
        elif c == "<":
            garbage = True
        elif c == "}":
            score -= 1
            groups += stack.pop()
        i += 1

    print(groups)

if __name__ == "__main__":
    main()