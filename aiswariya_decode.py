data = "Luna42Kai3.14True#Knight"

# 1. Extract "Luna" and convert to uppercase
name = data[0:4].upper()

# 2. Extract 42 and add 8
number = int(data[4:6]) + 8

# 3. Extract 3.14 and multiply by 2
pi_value = float(data[9:13]) * 2

# 4. Slice "Knight" using negative indexing and reverse it
title = data[-6:][::-1]

# Print results
print("Name:", name)
print("42 + 8 =", number)
print("3.14 * 2 =", round(pi_value, 2))
print("Reversed Title:", title)