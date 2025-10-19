
import unittest
from test import categorize_age

class TestCategorizeAge(unittest.TestCase):
    """Test cases for the categorize_age function."""

    def test_child_category(self):
        """Test the path for the 'Child' category."""
        self.assertEqual(categorize_age(10), "Child")
        self.assertEqual(categorize_age(0), "Child")

    def test_teenager_category(self):
        """Test the path for the 'Teenager' category."""
        self.assertEqual(categorize_age(15), "Teenager")
        self.assertEqual(categorize_age(13), "Teenager") 

    def test_adult_category(self):
        """Test the path for the 'Adult' category."""
        self.assertEqual(categorize_age(25), "Adult")
        self.assertEqual(categorize_age(18), "Adult") 

    def test_negative_age_error(self):
        """Test that a negative age raises a ValueError."""
        with self.assertRaises(ValueError):
            categorize_age(-5)


if __name__ == '__main__':
    unittest.main()
