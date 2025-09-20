# Pixel's Big Run Egg Calculator

# This is a super simple program that you can use to figure out how many eggs you need for each quota (bronze, silver and gold).
# The program also gives averages of the amount of eggs you will need in the next waves to reach a quota.

# Make sure to manually change the values below if they don't match the current Big Run quotas!
# I think they tend to stay at 85/110/135, but they might change at some point so we can use variables for now.
bronze = 85
silver = 110
gold = 135

import math

def identifyGoal(goal):  # Define function that lets the program find the quota name based on the value
    if goal == bronze:  # If the goal number matches the number for bronze, return "bronze"
        return "bronze"
    elif goal == silver:  # Functions same as above but for silver
        return "silver"
    else:  # If not bronze or silver, return "gold"
        return "gold"

def giveMessage(eggs, wave, goal):  # Define how to send messages to user
    if eggs >= goal:  # This part is self-explanatory
        print(f"Quota for {identifyGoal(goal)} reached!")  # Function is used inside print because we don't need to assign it a value
    elif eggs < goal and wave == 1:  # If you're on Wave 1 (2 waves to go), print total requirements and average eggs needed in Waves 2 and 3
        print(f"{goal-eggs} needed for {identifyGoal(goal)} ({(goal-eggs)/(3-wave)} avg for Waves 2+3)")
    else:  # If on Wave 2 or 3, just print the total requirement as average is useless
        print(f"{goal-eggs} needed for {identifyGoal(goal)}")

def msgs(eggs, wave):  # Make a function for all of the message-sending to save space
    if wave > 1:  # If on Wave 2 or 3, print the total eggs acquired
        print(f"Total so far: {eggs}")
    giveMessage(eggs, wave, bronze)  # Do messages for bronze, silver and gold quotas respectively
    giveMessage(eggs, wave, silver)
    giveMessage(eggs, wave, gold)

print(f"Average {math.ceil(bronze/3)} eggs each round needed for bronze")  # Print the average eggs for all three rounds
print(f"Average {math.ceil(silver/3)} eggs each round needed for silver")  # for each quota when the program is run
print(f"Average {math.ceil(gold/3)} eggs each round needed for gold")      # 'math.ceil' used so fractions don't print as x.3333333333...
print()

eggs = int(input("Eggs in Wave 1: "))  # Make 'eggs' into the number acquired in Round 1
msgs(eggs, 1)  # Do all wave 1 outputs
print()
eggs += int(input("Eggs in Wave 2: "))  # Add Round 2 count to eggs (no individual value is required to be saved)
msgs(eggs, 2)  # Do all wave 2 outputs
print()
eggs += int(input("Eggs in Wave 3: "))  # Add Round 3 count to eggs
msgs(eggs, 3)  # Do all wave 3 outputs
print()