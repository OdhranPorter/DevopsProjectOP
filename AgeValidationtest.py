import unittest
from AgeValidation import is_valid_age

class TestAgeValidation(unittest.TestCase):
    """Test cases for the is_valid_age function."""

    def test_valid_age(self):
        """Test a typical, valid age."""
        self.assertTrue(is_valid_age(31))

    def test_invalid_age_too_high(self):
        """Test that an age over 150 is rejected."""
        self.assertFalse(is_valid_age(151))

    def test_invalid_age_negative(self):
        """Test that a negative age is rejected."""
        self.assertFalse(is_valid_age(-5))


if __name__ == '__main__':
    unittest.main()

