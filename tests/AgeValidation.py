# validators.py
# This file contains a function to validate a user's age input.

def is_valid_age(age_input):
    """
    Validates an age input based on specific rules.

    Rules:
    - Must be an integer (not a letter, float, or other type).
    - Must not be negative.
    - Must not be greater than 150.

    Returns True if the age is valid, False otherwise.
    """
    # Rule 1: Check if the input is an integer.
    # This immediately rejects letters, strings, floats, etc.
    if not isinstance(age_input, int):
        return False

    # Rule 2: Check if the age is within the valid range (0-150).
    # This also handles the negative age case.
    if 0 <= age_input <= 150:
        return True
    else:
        # This will catch negative numbers and ages over 150.
        return False

