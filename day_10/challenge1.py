def main():
    
    data = None
    with open('./input.txt', 'r') as input_file:
        data = input_file.read().replace('\n','').split(',')

    knot_hash = [x for x in range(256)]
    position = 0
    skip_size = 0

    for step in data:
        step = int(step)
        twistData(knot_hash, position, step)
        position += step + skip_size
        skip_size += 1
    
    print(knot_hash[0] * knot_hash[1])

def twistData(knot_hash, position, step):  
    start = position % len(knot_hash)
    end = (start + step) % len(knot_hash)
    sublist = knot_hash[start:end] if end >= start else knot_hash[start:] + knot_hash[:end]
    reversed_sublist = [x for x in reversed(sublist)]
    for index in range(len(reversed_sublist)):
        knot_hash_index = (start + index) % len(knot_hash)
        knot_hash[knot_hash_index] = reversed_sublist[index]

if __name__ == "__main__":
    main()