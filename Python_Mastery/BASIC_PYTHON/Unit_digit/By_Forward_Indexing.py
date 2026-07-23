# UNIT DIGIT [LAST DIGIT] USING FORWARD INDEXING 
# NOTE: Value in Original Input Variable (num) cannot be Change

# GET DEFAULT INPUT FROM THE USER
num = input("Enter the Number: ")

# Find the Length of the Input Number
print("Length of the Input Number: ",len(num))

# GET THE UNIT DIGIT (Last Digit) USING FORWARD INDEXING
Num = num[len(num)-1] # num[4-1] --> num[3] --> LAST DIGIT
print("Last Digit from Input Number: ",Num)

# print("Length of the Input Number after Last Digit: ",len(num))

# GET TENTH DIGIT USING FORWARD INDEXING
num = num[(len(num)-1) - 1] 
# num[(4-1) - 1] --> num[(3) - 1] --> num[2] --> TENTH DIGIT
print("Tenth Digit from Input Number: ",num)