import unittest
from potionLogic import use_health_potion

class TestHealthPotion(unittest.TestCase):

    def test_normal_heal(self):
        # Player is at 50/100 HP. After a 20 HP potion, they should be at 70.
        new_health = use_health_potion(current_health=50, max_health=100)
        self.assertEqual(new_health, 70)


    def test_heal_at_full_health(self):
        """Test that using a potion at full health does nothing."""
        # Player is at 100/100 HP. After a potion, they should still be at 100.
        new_health = use_health_potion(current_health=100, max_health=100)
        self.assertEqual(new_health, 100)


if __name__ == '__main__':
    unittest.main()
