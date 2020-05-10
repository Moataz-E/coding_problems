import sys


def possible_moves(seq):
    """Returns set of indices that can be removed from sequence."""
    if len(seq) < 3:
        return []

    moves = []
    for i in range(1, len(seq) - 1):
        if seq[i-1] == 0 and seq[i+1] == 0:
            moves.append(i)
    return moves


def find_optimal_move(seq, moves):
    """Finds optimal move that will maximize reduction of available moves to opponent.

    Returns:
        None if there are no moves, otherwise returns the move that will reduce the opponent's
        possible move set the most.
    """
    # first element is move (index), and second element is resultant move reduction.
    optimal_move = (None, sys.maxsize)
    for move in moves:
        removed = seq.pop(move)
        new_moves = possible_moves(seq[min(0, move-2):min(len(seq)-1, move+2)])
        if len(new_moves) < optimal_move[1]:
            optimal_move = (move, len(new_moves))
        seq.insert(move, removed)
        if len(new_moves) == 0:
            break
    return optimal_move[0]


g = int(input().strip())
for a0 in range(g):
    n = int(input().strip())
    sequence = list(map(int, input().strip().split(' ')))

    alice_playing = True
    possible_move = True if len(possible_moves(sequence)) > 0 else False
    while possible_move:
        moves = possible_moves(sequence)
        optimal = find_optimal_move(sequence, moves)
        if optimal:
            sequence.pop(optimal)
            alice_playing = not alice_playing
        else:
            possible_move = False
    print("Bob") if alice_playing else print("Alice")
