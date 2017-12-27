def main():
    
    pipe_mapping = dict()
    with open('./input.txt', 'r') as f:
        for line in f:
            data = line.replace("\r\n","").replace(" ","").split("<->")
            pipe_mapping[data[0]] = data[1].split(",")
        
    explored = set()
    groups = 0
    for pipe in pipe_mapping.keys():
        if pipe not in explored:
            groups += 1
            exploreGroup(pipe, pipe_mapping, explored)

    print("The number of groups is: " + str(groups))

def exploreGroup(start, mappings, explored):
    to_explore = []
    to_explore += mappings[start]

    while len(to_explore) > 0:
        target = to_explore.pop(0)
        explored.add(target)
        for pipe in mappings[target]:
            if pipe not in explored:
                to_explore.append(pipe)

if __name__ == "__main__":
    main()