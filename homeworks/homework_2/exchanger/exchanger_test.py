import unittest
from exchanger import Exchanger


class ExchangerTest(unittest.TestCase):
    rub_val = Exchanger(1234, 'RUB')
    usd_val = Exchanger(120, 'USD')
    usd_val2 = Exchanger(27.55, 'USD')
    eur_val = Exchanger(50, 'EUR')
    cad_val = Exchanger(12.34, 'CAD')
    raw_val = Exchanger(45.558)
    int_val = 48

    rub_plus_usd = rub_val + usd_val
    usd_plus_rub = usd_val + rub_val
    rub_plus_raw = rub_val + raw_val
    rub_plus_int = rub_val + int_val
    raw_plus_int = raw_val + int_val

    multiple_sum_rub = rub_val + usd_val + eur_val + cad_val
    multiple_sum_usd = usd_val + rub_val + eur_val + cad_val
    multiple_sum_eur = eur_val + usd_val + rub_val + cad_val
    multiple_sum_cad = cad_val + usd_val + eur_val + rub_val
    multiple_sum_usd2 = usd_val + rub_val + eur_val + cad_val + usd_val2

    def test_str(self):
        self.assertEqual((self.rub_val.__str__()), '1,234.00 RUB')
        self.assertEqual((self.usd_val.__str__()), '120.00 USD')
        self.assertEqual((self.raw_val.__str__()), '45.56 units')
        self.assertEqual(self.rub_plus_usd.__str__(), '9,131.67 RUB')
        self.assertEqual(self.usd_plus_rub.__str__(), '138.75 USD')
        self.assertEqual(self.rub_plus_raw.__str__(), '1,279.56 RUB')
        self.assertEqual(self.rub_plus_int.__str__(), '1,282.00 RUB')
        self.assertEqual(self.raw_plus_int.__str__(), '93.56 units')
        self.assertEqual(self.multiple_sum_rub.__str__(), '13,400.50 RUB')
        self.assertEqual(self.multiple_sum_usd.__str__(), '203.61 USD')
        self.assertEqual(self.multiple_sum_eur.__str__(), '183.02 EUR')
        self.assertEqual(self.multiple_sum_cad.__str__(), '272.01 CAD')
        self.assertEqual(self.multiple_sum_usd2.__str__(), '231.16 USD')


if __name__ == "__main__":
    unittest.main()
