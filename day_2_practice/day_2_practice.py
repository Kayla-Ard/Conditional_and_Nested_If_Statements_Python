# Using user input and conditional statement to assign a letter grade to a score
grade = int(input("Enter the score you earned "))
if grade >= 90:
    print("You got an A!")
elif grade >= 80:
    print("You got a B!")
elif grade >= 70:
    print("You got a C!")
elif grade >= 60:
    print("You got a D!")
else:
    print("You got an F!")
    
# Using user input and conditional statement 
sugar = input("Enter yes if you want sugar, no if you do not want sugar ")
milk = input("Enter yes if you want milk, no if you do not want milk ")

if sugar == "yes" and milk == "yes":
    print("Try a latte")
elif sugar == "no" and milk == "yes":
    print("Try something that isn't sweet")
elif sugar == "yes" and milk == "no":
    print("Try a frap")
else:
    print("Order a black coffee")
    
# Nested if statements
age = 21
if age >= 18:
    if age >= 21:
        print("you can drive, vote  and drink")
    else:
        print("you can drive and vote")
else:
    print("you're to young to drive or vote")
    
# Nested if statements
genre = "Action"
author = "Susie Joe"

if genre == "Action":
    if author == "Susie Joe":
        print("Saving the world")
    elif author == "John Doe":
        print("Killing the bad guy")
elif genre == "Rom Com":
    if author == "Harry":
        print("They love each other")
    elif author == "Larry":
        print("fairytale")
    else:
        print("They don't love each other")
else:
    print("These people have bad taste")
    
# Shorthand conditional example 1
x = 5
y = 10
if x > y:
    print("x is greater")
else: 
    print("y is greater")
# This is the same thing
print("x is greater") if x > y else print("y is greater")

# Shorthand conditional example 2
weather = "sunny"
if weather == "sunny":
    activity = "beach"
else:
    activity = "video games"
print(activity)
#This is the same thing
activity = "beach" if weather == "sunny" else "video games"
print(activity)

# Another example of shorthand
energy_level = 4.5
time_available = 60
short_on_time = time_available < 45.0 #this is a boolean value so it will return true or false
print(short_on_time)

workout = "intense cardio" if energy_level > 4.0 and not short_on_time else "light yoga"
print(workout)

# Pass (placeholder so we do not get an error for empty code - write pass then fill in later)
