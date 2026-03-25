import unittest
from pesel_validator import PeselValidator

class TestPeselValidator(unittest.TestCase):
    def setUp(self):
        self.pesel = PeselValidator(12345678910)

    def test_pesel_format(self):
        self.assertTrue(self.pesel.validate_format())

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()