# Decisions at the Crossroad - Task 1: Code Correction
# Incorrect Code Below

# number = input("Enter a number: ")

# if number > 0:
#     print("The number is positive.")
# elif number = 0:
#     print("The number is zero.")
# else number < 0:
#     print("The number is negative.")

# Corrected Code Below

number = int(input("Enter a number: ")) # Needed int function 

if number > 0:
    print("The number is positive.")
elif number == 0:                       # Needed ==
    print("The number is zero.")
else:                                   # else doesn't need number assigned to anything 
    print("The number is negative.")
    
    

# The Greatest Showdown - Task 1: Identify the Greatest

num_1 = int(input("Enter a number "))
num_2 = int(input("Enter a number different than your first number "))
num_3 = int(input("Enter a number different than your first two numbers "))
if num_1 > num_2 and num_1 > num_3:
    print(f"The largest number is {num_1}!")
elif num_2 > num_1 and num_2 > num_3:
    print(f"The largest number is {num_2}!")
else:
    print(f"The largest number is {num_3}!")



# The Greatest Showdown - Task 2: Identify the Smallest

num_1 = int(input("Enter a number "))
num_2 = int(input("Enter a number different than your first number "))
num_3 = int(input("Enter a number different than your first two numbers "))

if num_1 > num_2 and num_1 > num_3:
    print(f"The largest number is {num_1}!")
elif num_2 > num_1 and num_2 > num_3:
    print(f"The largest number is {num_2}!")
else:
    print(f"The largest number is {num_3}!")

if num_1 < num_2 and num_1 < num_3:
    print(f"The smallest number is {num_1}!")
elif num_2 < num_1 and num_2 < num_3:
    print(f"The smallest number is {num_2}!")
else:
    print(f"The smallest number is {num_3}!")