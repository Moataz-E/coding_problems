import sys

starting_candies, t = input().strip().split(' ')
starting_candies, t = [int(starting_candies), int(t)]
c = list(map(int, input().strip().split(' ')))

if starting_candies < 5 or starting_candies > 100:
    raise ValueError("Constraint for n breached! Should be 5 <= n <= 100.")
if t < 1 or t > 100:
    raise ValueError("Constrain for t breached! Should be 1 <= t <= 100.")

candies_added = 0
candies_in_bowl = starting_candies
for i in range(t-1):
    if candies_in_bowl < c[i]:
        raise ValueError("Attempting to take more candies than what is in the bowl.")
    if c[i] < 1 or c[i] > starting_candies:
        raise ValueError("Can't add more more than starting candies amount to bowl.")
    candies_in_bowl -= c[i]
    if candies_in_bowl < 5:
        candies_to_add = starting_candies - candies_in_bowl
        candies_in_bowl += candies_to_add
        candies_added += candies_to_add
print(candies_added)
