import unittest
from src.zadanie2 import validate_email

class TestValidateEmail(unittest.TestCase):
    def test_zla_domena(self):
        self.assertFalse(validate_email("email@email"))

    def test_bez_malpy(self):
        self.assertFalse(validate_email("emailwp.pl"))

    def test_dobry(self):
        self.assertTrue(validate_email("wp.pl@wp.pl"))
        self.assertTrue(validate_email("wp.pl@interia.pl"))

    def test_brak_domeny(self):
        self.assertFalse(validate_email("email@"))

    def tearDown(self):
        pass

if __name__ == "__main__":
        unittest.main()
