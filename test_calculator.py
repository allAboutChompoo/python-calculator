import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(-67, -76), -143)
        self.assertEqual(self.calc.add(-55, 76), 21)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(-43, -88), 45)
        self.assertEqual(self.calc.subtract(99999, -458), 100457)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(-2, -3), 6)
        self.assertEqual(self.calc.multiply(-68, 3), -204)

    def test_divide(self): 
        self.assertEqual(self.calc.divide(-10, 3), -3)
        self.assertEqual(self.calc.divide(-10000, -50), 200)
        
    def test_modula(self): 
        self.assertEqual(self.calc.modulo(-10, 3), 2)
        self.assertEqual(self.calc.modulo(6789, 3), 0)
        
    # Add the following test methods to the TestCalculator class:

if __name__ == '__main__':
    unittest.main()