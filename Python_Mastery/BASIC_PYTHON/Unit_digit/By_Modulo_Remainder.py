# UNIT DIGIT [LAST DIGIT] USING MODULO REMAINDER (%)
# NOTE: Value in Original Input Variable (num) cannot be Change

# GET INTEGER INPUT FROM THE USER
num = int(input("Enter the Input Number: "))

# Find the Length of the Input Number 
# ERROR: TypeError - int has no len()
# print("Length of the Input Number: ",len(num))

# Find the UNIT DIGIT [LAST DIGIT] using MODULO REMAINDER
Num = num%10
print("Last Digit from Input Number: ",Num)

# Find the TENTH DIGIT using FLOOR DIVISION & MODULO REMAINDER 
num = num // 10
print("By Floor Division (Tenth): ",num)
Num_1 = num%10
print("Tenth Digit from Input Number: ",Num_1)

# Find the HUNDREDTH DIGIT using FLOOR DIVISION & MODULO REMAINDER
num = num // 10
print("By Floor Division (Hundredth): ",num)
Num_2 = num%10
print("Hundredth Digit from Input Number: ",Num_2)

# Find the THOUSANDTH DIGIT using FLOOR DIVISION & MODULO REMAINDER
num = num // 10
print("By Floor Division (Thousandth): ",num)
Num_3 = num%10
print("Thousandth Digit from Input Number: ",Num_3)