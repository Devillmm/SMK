## Swapping Two Numbers without Temporary Variable

# Get Inputs from the User
a = int(input("Enter a Value: "))
b = int(input("Enter b Value: "))

# Before Swapping
print("Before Swapping")
print("a = ",a,"b = ",b)

print()

# After Swapping
print("After Swapping")
a,b = b,a
print("a = ",a,"b = ",b)