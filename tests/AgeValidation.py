import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG) 

def is_adult(age):
    if not isinstance(age, int) or age < 0:
        logger.error(f"Invalid age input provided: {age}. Must be a non-negative integer.")
        raise ValueError("Age must be a non-negative integer.")

    if age >= 18:
        logger.info(f"Age {age} successfully validated as an adult.")
        return True
    else:
        logger.warning(f"Age {age} is below the adult threshold of 18.")
        return False