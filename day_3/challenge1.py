import sys
import math

def main():

    # Get input arguments.
    try:
        target_square = int(sys.argv[1])
    except IndexError:
        print("Usage: python challenge1.py <target_square>")
        exit(1)

    # Get the closest perfect odd square root (defines dimensions of the square)
    closest_perfect_square_root = math.ceil(math.sqrt(target_square))
    closest_perfect_square_root += 1 if closest_perfect_square_root % 2 == 0 else 0

    # Will always be on the outside of the square. Need to find out where.
    edge = int((closest_perfect_square_root ** 2 - target_square) / closest_perfect_square_root)
    
    # Edge of 0 means bottom, 1 means left, 2 means top, etc...
    distance_along_edge = closest_perfect_square_root ** 2 - target_square - edge * closest_perfect_square_root
    
    result = int(closest_perfect_square_root / 2) + int(closest_perfect_square_root / 2) - distance_along_edge

    print("The answer is: " + str(result))
    

if __name__ == "__main__":
    main()
