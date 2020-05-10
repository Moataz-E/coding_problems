import os
import math

def rotate_right(m):
    """Rotates a matrix 90-degrees to the right."""
    return list(list(x)[::-1] for x in zip(*m))

def generateThreeByThree():
    """Returns a list containing all the 3x3 magic squares."""
    mss = []
    # We know that non-corners and non-center will have these numbers, we use
    # this information to create a seed
    seed = [[1,1,3], [3,7,7], [7,9,9]]
    # We know that the center element has to be 5
    seed[1][1] = 5
    # Generate first seed with knowledge that all squares must have 2, 8, 4,
    # and 6 in corners.
    seed[0][0] = 8
    seed[0][2] = 6
    seed[2][0] = 4
    seed[2][2] = 2
    # Perform rotation and flip operations to generate magic squares from seed
    for i in range(1,5):
        seed = rotate_right(seed)
        mss.append(seed)
        seed_copy = seed[:]
        seed_copy[0], seed_copy[2] = seed_copy[2], seed_copy[0]
        mss.append(seed_copy)
    return mss

def diffSquares(s1, s2):
    """Find difference between squares."""
    return sum([abs(x[i] - y[i]) for x,y in zip(s1, s2) for i in range(len(x))])

def formingMagicSquare(s):
    magic_squares = generateThreeByThree()
    min_cost = math.inf
    for i, ms in enumerate(magic_squares):
        cost = diffSquares(s, ms)
        if cost < min_cost: min_cost = cost
    return min_cost

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = []
    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))
    result = formingMagicSquare(s)
    fptr.write(str(result) + '\n')
    fptr.close()
