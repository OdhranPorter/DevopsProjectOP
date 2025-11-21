import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[logging.FileHandler("app.log"), logging.StreamHandler()]
)

def is_valid_age(age):
    logging.info(f"Validating age input: {age}")
    
    # Check if input is an integer
    if not isinstance(age, int):
        logging.warning(f"Invalid input type: {type(age)}. Expected int.")
        return False
    
    # Check for negative age
    if age < 0:
        logging.warning(f"Invalid age: {age}. Age cannot be negative.")
        return False
        
    # Check for age > 150
    if age > 150:
        logging.warning(f"Invalid age: {age}. Age cannot be greater than 150.")
        return False

    logging.info(f"Age {age} is valid.")
    return True