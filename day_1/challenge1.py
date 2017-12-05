import sys

def main():

    # Parse the capatcha
    try:
        capatcha = sys.argv[1].strip()
    except IndexError:
        print("Usage: challenge1.py <capatcha>")
        exit(1)

    capatcha_sum = 0
    for i in range(0, len(capatcha)):
        second_ptr = (i + 1) % len(capatcha)
        if capatcha[i] == capatcha[second_ptr]:
            capatcha_sum += int(capatcha[i])

    print("The answer is: " + str(capatcha_sum))

if __name__ == "__main__":
    main()