import os
import bisect

def climbingLeaderboard(scores, alice):
    """Find alice's progressing leaderboard rank.

    Insert 'a' into a list if alice's score falls in that location.
    """
    scores = sorted(set(scores))
    ranks = []
    scores_len = len(scores)
    for a in alice:
        r = bisect.bisect_right(scores, a)
        ranks.append(scores_len - r + 1)
    return ranks

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    scores_count = int(input())
    scores = list(map(int, input().rstrip().split()))
    alice_count = int(input())
    alice = list(map(int, input().rstrip().split()))
    result = climbingLeaderboard(scores, alice)
    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')
    fptr.close()
