# UNIT DIGIT [LAST DIGIT] USING NEGATIVE INDEXING 
# NOTE: Value in Original Input Variable (num) cannot be Change

# GET DEFAULT INPUT FROM THE USER
num = input("Enter the Input Number: ")

# Find the Length of the Input Number
print("Length of the Input Number: ",len(num))

# Find the UNIT DIGIT (Last Digit) using NEGATIVE INDEXING
Num = num[-1] # Index -1 == Index 3
print("Last Digit from Input Number: ",Num)

# print("Length of the Input Number after Last Digit: ",len(num))

# Find the TENTH DIGIT using NEGATIVE INDEXING
Num_1 = num[-2] # Index -2 == Index 2
print("Tenth Digit from Input Number: ",Num_1)

# print("Length of the Input Number after Tenth Digit: ",len(num))

# Find the HUNDREDTH DIGIT using NEGATIVE INDEXING
Num_2 = num[-3] # Index -3 == Index 1
print("Hundredth Digit from Input Number: ",Num_2)