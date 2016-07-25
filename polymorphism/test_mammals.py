import animals
import unittest

class TestDog(unittest.TestCase):
    def setUp(self):
        self.dog = animals.Dog()

    def tearDown(self):
        del self.dog

    def test_make_sound(self):
        self.assertEqual(self.dog.make_sound(), 'Bow!!!!')

if __name__ =='__main__':
    unittest.main()