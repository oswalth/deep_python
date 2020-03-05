import unittest
from lister import Lister


class ListerTest(unittest.TestCase):
    a = Lister([1, 2, 3, 4])
    b = Lister([0, 2, 4, 6, 8])
    c = [2, 2, 2, 100.5]
    d = [-1, -2, -3, -4]

    smaller_sum = a + b
    greater_sum = b + a
    smaller_sub = a - b
    greater_sub = b - a
    normal_sum = a + c
    normal_sub = a - c

    eq = a == Lister([5, 2, 3])
    ne = a != Lister([1, 2, 3, 4, 0])
    lt = a < Lister([1, 2, 3, 5])
    le = a <= Lister([1, 2, 3, 4, 0])
    gt = a > Lister([5, 5])
    ge = a >= [9, 0, 1, 0, -1]

    def test_sum(self):
        self.assertEqual((self.a + self.b).__str__(),
                         'Magic list - {}'.format([1, 4, 7, 10, 8]))
        self.assertEqual((self.b + self.a).__str__(),
                         'Magic list - {}'.format([1, 4, 7, 10, 8]))
        self.assertEqual((self.a + self.c).__str__(),
                         'Magic list - {}'.format([3, 4, 5, 104.5]))
        self.assertEqual((self.a + self.d).__str__(),
                         'Magic list - {}'.format([0, 0, 0, 0]))

    def test_sub(self):
        self.assertEqual((self.a - self.b).__str__(),
                         'Magic list - {}'.format([1, 0, -1, -2, -8]))
        self.assertEqual((self.b - self.a).__str__(),
                         'Magic list - {}'.format([-1, 0, 1, 2, 8]))
        self.assertEqual((self.a - self.c).__str__(),
                         'Magic list - {}'.format([-1, 0, 1, -96.5]))
        self.assertEqual((self.a - self.d).__str__(),
                         'Magic list - {}'.format([2, 4, 6, 8]))

    def test_equality(self):
        self.assertEqual(self.a == Lister([5, 2, 3]), True)
        self.assertEqual(self.a != Lister([1, 2, 3, 4, 0]), False)
        self.assertEqual(self.a < Lister([1, 2, 3, 5]), True)
        self.assertEqual(self.a <= Lister([1, 2, 3, 5, -1]), True)
        self.assertEqual(self.a > Lister([5, 5]), False)
        self.assertEqual(self.a >= Lister([9, 0, 1, 0, -1]), True)


if __name__ == "__main__":
    unittest.main()
