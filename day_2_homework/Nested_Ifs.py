# Nested Decisions: The Adventure Game - Task 1: Code Correction 
# Incorrect Code Below 

# place = input("Choose a place: forest or cave? ")

# if place = "forest":
#     action = input("climb a tree or cross a river?")
#     if action = "climb a tree":
#         print("You found a bird's nest!")
#     else action = "cross a river":
#         print("You found a boat!")
# elif place = "cave":
#     print("You find a hidden treasure!")
    
# Corrected Code Below

place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river? ")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
elif place == "cave":
    print("You found a hidden treasure!")
    


# Nested Decisions: The Adventure Game - Task 2: Setting the Scene

place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river? ")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
elif place == "cave":
    action = input("light a torch or proceed in the dark? ")
    if action == "light a torch":
        print("You're on fire!")
    elif action == "proceed in the dark":
        print("You can't see!")

        
        
# Nested Decisions: The Adventure Game - Task 3: Default Path
place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river? ")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
    else:
        pass
elif place == "cave":
    action = input("light a torch or proceed in the dark? ")
    if action == "light a torch":
        print("You're on fire!")
    elif action == "proceed in the dark":
        print("You can't see!")
    else:
        pass
else:
    pass



# Quick Decisions: The Event Planner - Task 1: Code Correction
# Incorrect Code Below 

# attendees = input("Enter number of attendees: ")
# venue = "large hall" if attendees > 100 else "conference room"
# print(venue)

# Corrected Code Below (Needed to add int function)

attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"
print(venue)



# Quick Decisions: The Event Planner - Task 2: Venue Selection

attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"
audio_system = "massive speakers" if attendees > 100 else "mini speakers"
projector = "big screen" if attendees > 100 else "no projector needed"
print(venue, audio_system, projector)



# Quick Decisions: The Event Planner - Task 3: Catering Choices

attendees = int(input("Enter number of attendees: "))
food_preference = input("Would you like vegetarian food? Yes or No? ")
venue = "large hall" if attendees > 100 else "conference room"
audio_system = "massive speakers" if attendees > 100 else "mini speakers"
projector = "120 inch projector" if attendees > 100 else "50 inch projector"
food = "you can bring on the meat" if attendees > 100 else "we must have vegetarian options"
print(f"The event will be held in a {venue} and include {audio_system} to produce the music. The dance floor will be live streamed on a {projector} and for the meals {food}!")