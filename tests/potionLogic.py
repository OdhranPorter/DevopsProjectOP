def use_health_potion(current_health, max_health):

    potion_value = 20
    potential_health = current_health + potion_value

    return min(potential_health, max_health)
