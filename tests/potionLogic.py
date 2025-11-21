import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[logging.FileHandler("app.log"), logging.StreamHandler()]
)

def use_health_potion(current_health, max_health):
    logging.info(f"Using potion: current_health={current_health}, max_health={max_health}")

    potion_value = 20
    potential_health = current_health + potion_value
    
    # Calculate final health (capped at max_health)
    final_health = min(potential_health, max_health)

    # Log specific outcomes
    if potential_health > max_health:
        logging.info(f"Healing would exceed max health. Capped at {max_health}.")
    else:
        logging.info(f"Healed for full potion value ({potion_value}).")

    logging.info(f"Final health: {final_health}")
    return final_health