import unittest
from src.trip import Trip

class TestTripInitialization(unittest.TestCase):
    def setUp(self):
        self.trip = Trip("Paris", 7)

    def test_trip(self):
        self.assertEqual(self.trip.destination, "Paris")
        self.assertEqual(self.trip.duration, 7)

    def test_not_empty(self):
        self.assertIsNotNone(self.trip.duration)
        self.assertIsNotNone(self.trip.duration)

    def test_calculate_cost(self):
        self.assertEqual(self.trip.calculate_cost(), 700)
        trip2 = Trip("Rome", 5)
        self.assertEqual(trip2.calculate_cost(), 500)

    def test_add_participant(self):
        self.trip.add_participant("John")
        self.assertIn("John", self.trip.participant_list)
        self.trip.add_participant("John", "Alice", "Bob")
        for p in ["John", "Alice", "Bob"]:
            self.assertIn(p, self.trip.participant_list)
        with self.assertRaises(ValueError):
            self.trip.add_participant("")

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()