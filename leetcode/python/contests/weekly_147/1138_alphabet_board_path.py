import copy

class Solution:

    def __init__(self):
        self.board = board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]

    def calc_letter_loc(self, letter):
        diff = ord(letter) - 97
        return [diff // 5, diff % 5]

    def alphabetBoardPath(self, target: str) -> str:
        curr_loc = [0, 0]
        path_taken = ""
        for i in range(len(target)):
            curr_letter = target[i]
            target_loc = self.calc_letter_loc(curr_letter)
            while curr_loc != target_loc:
                if target_loc == [5, 0] and curr_loc[0] == 4 and curr_loc[1] != 0:
                    curr_loc[1] -= 1
                    path_taken += "L"
                else:
                    # Go up or down till in same row
                    if curr_loc[0] > target_loc[0]:
                        curr_loc[0] -= 1
                        path_taken += "U"
                    elif curr_loc[0] < target_loc[0]:
                        curr_loc[0] += 1
                        path_taken += "D"
                    else:
                        # In same row, go left or right till in same column
                        if curr_loc[1] > target_loc[1]:
                            curr_loc[1] -= 1
                            path_taken += "L"
                        else:
                            curr_loc[1] += 1
                            path_taken += "R"
            # We are in the right location.
            path_taken += "!"
        return path_taken

s = Solution()
print(s.alphabetBoardPath("zdz"))
