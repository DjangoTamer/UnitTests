from unittest import TestCase, main
from calculator import calculator as calc

class CalculatorTest(TestCase):
    def test_plus(self):
        self.assertEqual(calc('1+2'), 3)

    def test_minus(self):
        self.assertEqual(calc('4-2'), 2)

    def test_multi(self):
        self.assertEqual(calc('5*6'), 30)

    def test_div(self):
        self.assertEqual(calc('8/2'), 4)

    def test_no_signs(self):
        with self.assertRaises(ValueError) as e:
            calc('ababa')
        self.assertEqual('Выражение должно содержать хотя бы один знак +-*/', e.exception.args[0])




if __name__ == '__main__':
    main()