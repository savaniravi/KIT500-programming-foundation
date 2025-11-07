"""
4.1PP Selection and Repetition
"""

__author__ = "Ravi Savani"

import timeit

def show_heading(heading: str): 
    """
    Display the given heading, with underline.
    """
    heading = heading.upper()   # Convert heading into uppercase
    print(heading)              # display heading
    print("~" * len(heading))   # display underline (~)  
    print()                     # print a blank line

def one_attempt(word: str) -> bool:
    """
    Tests the user's ability to type the given word, providing feedback on
    the attempt. Returns True if they typed it correctly, False otherwise.
    """
    attempt = input(f"Type the word: {word}\nEnter word: ")
    if attempt == word:   # check user typed the word correctly
        print("Correct")
        return True
    else:                # user did not type the word correctly
        print("Incorrect")
        return False

def practice_typing(word: str, required: int) -> int:
    """
    Tests the user's typing ability by having them type the given word
    correctly, including capitalisation, required times before finishing.
    Returns the total number of attempts.
    """
    attempts = 0 # Total number of attempts made by the user
    correct = 0  # Number of times the user has typed the word correctly

    while correct < required:
        attempts += 1
        if one_attempt(word):
            correct += 1

    return attempts

def main():
    WORD = "python" # the practice word
    REPEATS = int(input("Enter number for practice repeat: ")) # number of required correct repeats
    start_time = timeit.default_timer() # start time of practice
    attempted = practice_typing(WORD, REPEATS)
    end_time = timeit.default_timer() # end time of practice

    # Report on the user's performance
    print(f"Total Attempts: {attempted}")
    print(f"Your Accuracy: {100 * REPEATS / attempted:.0f}%")
    print(f"Total time taken: {end_time - start_time:.1f} s")
    print()
    show_heading("New word every day!")

if __name__ == "__main__":
    main()
