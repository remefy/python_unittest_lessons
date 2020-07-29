from unittest import TestCase
from functions.plus import plus


class PlusFunctionTestCase(TestCase):
    def test_1_plus_1_return_2(self):
        self.assertEqual(2, plus(1, 1))

    def test_5_plus_5_return_10(self):
        self.assertEqual(10, plus(5, 5))

    def test_1555_plus_1445_return_3000(self):
        self.assertEqual(3000, plus(1555, 1445))

    def test_100_plus_100_return_200(self):
        self.assertEqual(200, plus(100, 100))
