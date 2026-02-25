import unittest
from src.person import Person


class TestPerson(unittest.TestCase):
    def setUp(self):
        #Ten kod jest wykonywany przed każdym testem
        self.person = Person("Jan", "Kowalski", 30)

    def test_get_full_name(self):
        #Sprawdzamy, czy metoda get_full_name zwraca poprawną wartość
        self.assertEqual(self.person.get_full_name(), "Jan Kowalski")

    def test_is_adult_true(self):
        #Sprawdzamy, czy metoda is_adult zwraca True dla osoby pełnoletniej
        self.assertTrue(self.person.is_adult())

    def test_is_adult_false(self):
        #Sprawdzamy, czy metoda is_adult zwraca False dla osoby niepełnoletniej
        young_person = Person("Anna", "Nowak",15)
        self.assertFalse(young_person.is_adult())

    def test_is_adult_no_age(self):
        #Sprawdzamy, czy metoda is_adult zgłasza wyjątek, gdy age nie jest ustawiony
        person_no_age = Person("Piotr","Wiśniewski")
        with self.assertRaises(ValueError):
            person_no_age.is_adult()

    def test_celebrate_birthday(self):
        #Sprawdzamy, czy metoda celebrate_birthday zwiększa wiek o 1
        old_age = self.person.age
        new_age = self.person.celebrate_birthday()
        self.assertEqual(new_age, old_age + 1)
        self.assertEqual(self.person.age, old_age + 1)

    def tearDown(self):
        #Ten kod jest wykonywany po każdym teście
        pass


if __name__ == "__main__":
    unittest.main()