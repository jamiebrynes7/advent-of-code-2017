import functools

def main():
    
    data = None
    with open('./input.txt', 'r') as input_file:
        data = input_file.read().replace('\n','')

    knot_hash = [x for x in range(256)]
    position = 0
    skip_size = 0
    lengths = [ord(character) for character in data] + [17, 31, 73, 47, 23]
    for i in range(64):
        for step in lengths:
            step = int(step)
            twistData(knot_hash, position, step)
            position += step + skip_size
            skip_size += 1

    dense_hash = sparseToDenseHash(knot_hash)
    hex_string = denseHashToHex(dense_hash)

    print(hex_string)


def twistData(knot_hash, position, step):
    start = position % len(knot_hash)
    end = (start + step) % len(knot_hash)
    sublist = knot_hash[start:end] if end >= start else knot_hash[start:] + knot_hash[:end]
    reversed_sublist = [x for x in reversed(sublist)]
    for index in range(len(reversed_sublist)):
        knot_hash_index = (start + index) % len(knot_hash)
        knot_hash[knot_hash_index] = reversed_sublist[index]

def sparseToDenseHash(knot_hash):

    dense_hash = []
    blocks = []
    for i in range(16):
        block = knot_hash[i*16:(i+1)*16]
        blocks = blocks + block
        dense_hash.append(functools.reduce(lambda x, y: x ^ y, block))
    return dense_hash

def denseHashToHex(dense_hash):
    hex_string = ""

    for number in dense_hash:
        hex_string += '%02x'%number

    return hex_string

if __name__ == "__main__":
    main()