"""
  This library is provided without warranty under the MIT license
  Created by Dustin Tinney <dustin@testdouble.com>
"""

from .exchange_service import ExchangeService


class ExchangeServiceDownError(Exception):
    pass


class ForexDataClient:
    def get_rate(self, *, to_currency, from_currency):
        try:
            rate = self._exchange_rate(to_currency, from_currency)
            return {to_currency: rate}
        except Exception:
            raise ExchangeServiceDownError('Exchange Service is offline.')

    def convert(self, *, to_currency, from_currency, amount):
        try:
            total = amount * self._exchange_rate(to_currency, from_currency)
            return {to_currency: total}
        except Exception:
            raise ExchangeServiceDownError('Exchange Service is offline.')

    def _exchange_rate(self, to_currency, from_currency):
        if to_currency == from_currency:
            return 1
        return ExchangeService.get_rate(to_currency, from_currency)
