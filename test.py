def categorize_age(age):
    """
    Categorizes an age into 'Child', 'Teenager', or 'Adult'.
    Raises an error for negative ages.
    """
    if age < 0:
        raise ValueError("Age cannot be negative.")
    elif age < 13:
        return "Child"
    elif age < 18:
        return "Teenager"
    else:
        return "Adult"
