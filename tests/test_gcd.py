from unittest import TestCase
from functions.gcd import gcd


class GCDFunctionTestCase(TestCase):
    def test_gcd_33_and_27_return_3(self):
        self.assertEqual(3, gcd(33, 27))

    def test_gcd_99_and_45_return_9(self):
        self.assertEqual(9, gcd(99, 45))

    def test_gcd_97_and_23_return_1(self):
        self.assertEqual(1, gcd(97, 23))

    def test_gcd_10_and_100_return_10(self):
        self.assertEqual(10, gcd(10, 100))
