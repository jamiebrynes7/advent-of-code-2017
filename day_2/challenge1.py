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
        checksum += findMaxDifference(row)

    print("The answer is: " + str(checksum))


def findMaxDifference(row):
    largest = row[0]
    smallest = row[0]

    for digit in row:
        if digit > largest:
            largest = digit
        if digit < smallest:
            smallest = digit
    
    return largest - smallest


if __name__ == "__main__":
    main()
