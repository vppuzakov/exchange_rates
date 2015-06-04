__author__ = 'Vladimir I. Puzakov'

from decimal import Decimal

class Course:
    """
    Exchange rate for some currency

    :type source: str
    :type source: str
    :type source: Decimal

    """
    def __init__(self, source, target, price):
        """
        Initialize with setting source and target currency, and price for exchange
        :param source: source currency
        :param target: target currency
        :param price: exchange rate

        :type source: str
        :type target: str
        :type price: Decimal

        :return: instance
        """

        self.source = source
        self.target = target
        self.price = price

