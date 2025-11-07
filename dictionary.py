"""
5.2PP Word Collection

The functions main() and avg_length() contain code sourced from the notes on MyLO.

"""
__author__ = "Ravi Savani"

def add_word(word_list: list[str], word: str) -> bool:
    """
    Adds a word to the dictionary.

    Checks if the word is empty before adding it.

    Returns:
        bool: True if the word was added, False otherwise.
    """
    if word == "":
        print("Please provide a non-empty word!")
        return False
    elif word not in word_list:
        word_list.append(word)
        return True
    else:
        print("The word is already in the dictionary.")
        return False


def display_words(word_list: list[str]):
    """
    Displays the words in the list with proper formatting.
    """
    output = ", ".join(word_list)
    print(output)


def calculate_avg_length(word_list: list[str]) -> float:
    """
    Calculates the average length of words in the list.

    Returns:
        float: The average length of the words in the list.
    """
    if not word_list:
        return 0.0

    total_length = sum(len(word) for word in word_list)
    return total_length / len(word_list)


def main():
    """
    Manages the mini dictionary program.
    """
    word_list: list[str] = []  # Collection of words, initialized as empty
    choice: int = 0  # User's menu selection, initialized as empty

    print("Mini Dictionary")

    while choice != 4:
        print()
        print("1. Add a word")
        print("2. Display entries")
        print("3. Display average word length")
        print("4. Quit")
        print()

        try:
            choice = int(input("Please select one of the above options: "))
            print()
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
            continue

        match choice:
            case 1:
                print("You have selected to add a new word.")
                print()
                while True:
                    new_word = input("Please type the new word: ").strip()
                    if add_word(word_list, new_word):
                        break

            case 2:
                print("You have selected to display the entries.")
                print()
                display_words(word_list)

            case 3:
                print("You have selected to display average word length.")
                print()
                avg_length = calculate_avg_length(word_list)
                print(f"Average word length: {avg_length:.2f}")

            case 4:
                print("Exiting the program...")
                break

            case _:
                print("You have made an invalid choice. Please try again.")

if __name__ == "__main__":
    main()
