import unittest


class TestFails(unittest.TestCase):
    def setUp(self):
        pass

    def test_fail(self):
        self.assertEqual(1, 2)
        
    def test_pass(self):
        self.assertEqual(1, 1)
        
    def test_fail_second(self):
        self.assertTrue(False)

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()    