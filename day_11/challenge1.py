def main():

    steps = []
    with open('./input.txt', 'r') as f:
        steps = f.read().replace("\n", "").split(",")
    
    location = [0,0,0]
    for step in steps:
        if step == "n":
            incrementLocation(location, [0, 1, -1])
        elif step == "ne":
            incrementLocation(location, [-1, 1, 0])
        elif step == "se":
            incrementLocation(location, [-1, 0, 1])
        elif step == "s":
            incrementLocation(location, [0, -1, 1])
        elif step == "sw":
            incrementLocation(location, [1, -1, 0])
        elif step == "nw":
            incrementLocation(location, [1, 0, -1])
        else:
            print("Unrecognized instruction: ")
            print(step)
    
    print(getDistance(location))

def incrementLocation(location, change):
    for i in range(len(change)):
        location[i] += change[i]

def getDistance(location):
    return max([abs(coord) for coord in location])



if __name__ == "__main__":
    main()