n = int(input().strip())
if n < 2 or n > 50:
    raise ValueError("Constraint breached! Value of n needs to be between 2 and 50.")

output = ["min(int, int)"]
for _ in range(2, n):
    output.insert(0, "min(int, ")
    output.append(')')
print(''.join(output))
