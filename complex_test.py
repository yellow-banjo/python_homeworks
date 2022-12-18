import unittest
from ComplexValue import Complex


class ComplexValueTest(unittest.TestCase):
    def test_equal(self):
        self.assertEqual(Complex(5, 3), 5 + 3j)

    def test_conjugate(self):
        self.assertEqual(Complex(5, 3).conjugate(), (5 + 3j).conjugate())

    def test_abs(self):
        self.assertEqual(abs(Complex(3, 4)), abs(3 + 4j))

    def test_add(self):
        self.assertEqual(Complex(5, 3) + Complex(6, -9), 5 + 3j + 6 - 9j)
        self.assertEqual(Complex(5, 3) + 5, 5 + 3j + 5)

    def test_radd(self):
        self.assertEqual(5 + 3j + Complex(6, -9), 5 + 3j + 6 - 9j)
        self.assertEqual(5 + Complex(5, 3), 5 + 3j + 5)

    def test_sub(self):
        self.assertEqual(Complex(5, 3) - Complex(6, -9), 5 + 3j - 6 + 9j)
        self.assertEqual(Complex(5, 3) - 15, 5 + 3j - 15)

    def test_rsub(self):
        self.assertEqual(5 + 3j - Complex(6, -9), 5 + 3j - 6 + 9j)
        self.assertEqual(13 - Complex(5, 3), 13 - (5 + 3j))

    def test_mul(self):
        self.assertEqual(Complex(3, 4) * Complex(-6, 12), (3 + 4j) * (-6 + 12j))
        self.assertEqual(Complex(-5, 3) * (- 6), (-5 + 3j) * (- 6))

    def test_rmul(self):
        self.assertEqual((3 + 4j) * Complex(-6, 12), (3 + 4j) * (-6 + 12j))
        self.assertEqual((- 6) * Complex(-5, 3), (-5 + 3j) * (- 6))

    def test_truediv(self):
        self.assertEqual(Complex(5, 3) / Complex(0, 7), (5 + 3j) / 7j)
        self.assertEqual(Complex(15, 31) / 12, (15 + 31j) / 12)

    def test_rtruediv(self):
        self.assertEqual((5 + 3j) / Complex(-5, 7), (5 + 3j) / (-5 + 7j))
        self.assertEqual(-6 / Complex(15, 31), -6 / (15 + 31j))

    def test_pow(self):
        self.assertEqual((Complex(1, 2) + (-3 + 4j)) ** Complex(-5, 6), ((1 + 2j) + (-3 + 4j)) ** (-5 + 6j))
        self.assertEqual(Complex(3, 5) ** (-1), (3 + 5j) ** (-1))
        self.assertEqual(Complex(3, 5) ** 3, (3 + 5j) ** 3)

    def test_str(self):
        self.assertEqual(str(Complex(1, 2)), str(1 + 2j))
        self.assertEqual(str(Complex(0, 2)), str(2j))


if __name__ == '__main__':
    unittest.main()
