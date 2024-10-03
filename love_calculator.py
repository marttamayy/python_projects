import time
import sys

# You are going to write a function called calculate_love_score() that tests the compatibility between two names.  
# To work out the love score between two people: 
# 1. Take both people's names and check for the number of times the letters in the word TRUE occurs.   

name1 = input("What's the first name?: ")
name2 = input("What's the second name?: ")

first_name1 = name1.split()[0]
first_name2 = name2.split()[0]

# Simulate a loading animation (dots appearing one by one)


print(f"Calculating love score for {first_name1} and {first_name2}")

for _ in range(3):
    time.sleep(0.5)  # Pauses for 0.5 seconds
    print(".", end="")
    sys.stdout.flush()  # Forces the print output to update immediately

# Move to the next line after loading animation
print("\n")


def calculate_love_score(name1, name2):

    concat_name = (name1 + name2).lower()
    # Define the words we are checking for
    word_true = "true"
    word_love = "love"

    # Initialize counters
    counter_true = 0
    counter_love = 0

    # Count occurrences of letters from "TRUE" in the combined names
    for letter in word_true:
        counter_true += concat_name.count(letter)

    # Count occurrences of letters from "LOVE" in the combined names
    for letter in word_love:
        counter_love += concat_name.count(letter)

    # Combine the counts to form a two-digit love score
    love_score = int(f"{counter_true}{counter_love}")

    print("Love score = ", love_score)

# Print the final love score

calculate_love_score(name1, name2)

# 3. Then combine these numbers to make a 2 digit number and print it out. 
# e.g.
# name1 = "Angela Yu" name2 = "Jack Bauer"
# T occurs 0 times 
# R occurs 1 time 
# U occurs 2 times 
# E occurs 2 times 
# Total = 5 
# L occurs 1 time 
# O occurs 0 times 
# V occurs 0 times 
# E occurs 2 times 
# Total = 3 

# Love Score = 53


# Example Input 

# How to test your code and see your output?

# Udemy coding exercises do not have a console, so you cannot use the input() function. You will need to call your function with hard-coded values like so:

# # Call your function with hard coded values
print("Fun fact! The love score for Kanye West and Kim Kardashian:")
calculate_love_score("Kanye West", "Kim Kardashian")