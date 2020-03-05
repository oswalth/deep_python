import requests


class Exchanger():
    def __init__(self, quantity, currency=None):
        self.quantity = quantity
        self.load_rate()
        if currency not in self.currency_lib.keys() and currency:
            raise ValueError
        self.currency = currency

    @classmethod
    def load_rate(cls):
        """
        Loads exchange rate of
        """
        if hasattr(cls, 'currency_lib'):
            return
        response = requests.get('https://api.exchangeratesapi.io/2020-03-04')
        cls.currency_lib = response.json()['rates']
        base_currency = response.json()['base']
        cls.currency_lib[base_currency] = 1

    def __add__(self, other):
        """
        __add__ magic method overload to add currencies
        Standart currency - EUR. Used as intermidiate to provie calculations
        input: self - object pointer; other - object/value to add
        output: sum of values' quantity presented in self object's currency.
        """
        if hasattr(other, 'currency'):
            output_code = self.currency or other.currency or None
        else:
            output_code = self.currency or None
        if isinstance(other, (int, float)):
            return self.init_sum_object(self.quantity + other, output_code)
        elif other.currency != self.currency and other.currency and self.currency:
            self_standartized = self.quantity / \
                self.currency_lib[self.currency]
            other_standartized = other.quantity / \
                (self.currency_lib.get(other.currency) or 1)
            output_quantity = (
                self_standartized + other_standartized) * self.currency_lib[self.currency]
            return self.init_sum_object(output_quantity, output_code)
        return self.init_sum_object(
            self.quantity + other.quantity, output_code)

    def init_sum_object(self, quantity, currency=None):
        return Exchanger(quantity, currency=currency)

    def __str__(self):
        return '{:,.2f} {}'.format(self.quantity, self.currency or 'units')
