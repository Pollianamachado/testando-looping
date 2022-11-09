
name = input("What's your name? ")

# TODO: Ask the user by name if they understand Python while loops
user= input(f"Hi, {name}. Do you understand Python while loops? (yes/no)? ")

# TODO: Write a while statement that checks if the user doesn't understand while loops
# TODO: Since the user doesn't understand while loops, let's explain them.
# TODO: Ask the user again, by name, if they understand while loops.
while user == "no":
    print("while loops repeat as long as a certain Boolean condition is met.")
    user= input(f"{name}. Now do you understand Python while loops? (yes/no)? ")  
# TODO: Outside the while loop, congratulate the user for understanding while loops
else:
    print(f"Congratulations, {name}!")
