def main():
    
    pipe_mapping = dict()
    with open('./input.txt', 'r') as f:
        for line in f:
            data = line.replace("\r\n","").replace(" ","").split("<->")
            pipe_mapping[data[0]] = data[1].split(",")
        
    explored = set()
    to_explore = []

    to_explore += pipe_mapping["0"]
    explored.add("0")

    while len(to_explore) > 0:
        target = to_explore.pop(0)
        explored.add(target)
        for pipe in pipe_mapping[target]:
            if pipe not in explored:
                to_explore.append(pipe)

    print(len(explored))


if __name__ == "__main__":
    main()