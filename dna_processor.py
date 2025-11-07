# this file is dna_processor.py

__author__ = 'Savani Ravikumar'

import dna_operations as ops

def main() -> None:
    """
    Main function to run the DNA Processor program.
    """
    print("Welcome to the DNA Processor")
    cleaned_sequence = get_cleaned_sequence()
    error_rate = ops.calculate_error_rate(cleaned_sequence)
    print(f"Error rate: {error_rate:.1f}%")
    run_menu(cleaned_sequence)

def get_cleaned_sequence() -> str:
    """
    Get a DNA sequence from the user and clean it.
    """
    dna_sequence = input("Enter a DNA sequence: ").upper()
    return ops.clean_sequence(dna_sequence)

def run_menu(cleaned_sequence: str) -> None:
    """
    Display the main menu and handle user choices.
    """
    while True:
        display_sequence(cleaned_sequence)
        choice = display_menu()
        if choice == '1':
            ops.display_complement(cleaned_sequence)
        elif choice == '2':
            error_rate = ops.calculate_error_rate(cleaned_sequence)
            print(f"Error rate: {error_rate:.1f}%")
        elif choice == '3':
            ops.transcribe_sequence(cleaned_sequence)
        elif choice == '4':
            cleaned_sequence = ops.transcribe_section(cleaned_sequence)
        elif choice == '5':
            cleaned_sequence = ops.splice_sequence(cleaned_sequence)
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

def display_sequence(sequence: str) -> None:
    """
    Display the working sequence.
    """
    print(f"Working sequence: {sequence}")

def display_menu() -> str:
    """
    Display the main menu and get user choice.
    """
    print("\nMenu:")
    print("1. Display the sequence with its complement")
    print("2. Display the error rate")
    print("3. Transcribe the entire sequence")
    print("4. Transcribe a section of the sequence")
    print("5. Splice another sequence onto the end")
    print("6. Quit")
    return input("Select an option: ")

if __name__ == "__main__":
    main()
