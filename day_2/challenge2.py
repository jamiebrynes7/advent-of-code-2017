def main():

    # Parse problem input
    input_fp = "./input.txt"
    spreadsheet = []
    with open(input_fp, 'r') as input_file:
        for line in input_file:
            line.replace('\n', ' ')
            spreadsheet.append([int(x) for x in line.split('\t')])

    checksum = 0
    for row in spreadsheet:
        checksum += findEvenDivision(row)

    print("The answer is: " + str(checksum))


def findEvenDivision(row):
    for first_value in row:
        for second_value in row:
            if first_value == second_value:
                continue
            if first_value % second_value == 0:
                return (first_value / second_value)

if __name__ == "__main__":
    main()
