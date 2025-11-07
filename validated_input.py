"""
4.3CR User Input Functions
"""

__author__ = "Ravikumar Savani"

def input_int(prompt: str, low: int, high: int) -> int:
    """
    Continuously prompt the user to enter an integer within a specified range.

    This function will repeatedly prompt the user to input an integer value 
    between 'low' and 'high' (inclusive) until a valid value is provided.
    """
    while True:
        try:
            value = int(input(f"{prompt} ({low}-{high}): "))
            if low <= value <= high:
                return value
            else:
                print("Value out of range.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def input_float(prompt: str, low: float, high: float) -> float:
    """
    Continuously prompt the user to enter a float within a specified range.

    This function will repeatedly prompt the user to input a float value 
    between 'low' and 'high' (inclusive) until a valid value is provided.
    """
    while True:
        try:
            value = float(input(f"{prompt} ({low}-{high}): "))
            if low <= value <= high:
                return value
            else:
                print("Value out of range.")
        except ValueError:
            print("Invalid input. Please enter a valid float.")

def input_bool(prompt: str) -> bool:
    """
    Continuously prompt the user to enter a boolean value based on yes/no responses.

    This function will repeatedly prompt the user to input a response until a valid 
    boolean value is provided.
    """
    true_responses = ['y', 'yes', 'true']
    false_responses = ['n', 'no', 'false']
    
    while True:
        response = input(f"{prompt} (yes/no): ").strip().lower()
        if response in true_responses:
            return True
        elif response in false_responses:
            return False
        else:
            print("Invalid input. Please enter yes or no.")

if __name__ == "__main__":
    # Test input_int
    print("Welcome to User Input Functions..")
    stars = input_int("Enter the number of stars", 1, 10)
    print(f"You entered: {stars}")

    # Test input_float
    volume = input_float("Enter the volume", 0.0, 1.0)
    print(f"You entered: {volume}")

    # Test input_bool
    again = input_bool("Would you like to continue?")
    print(f"You entered: {again}")
