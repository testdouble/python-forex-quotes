import random
import time


class ExchangeService:
    @staticmethod
    def valid_currency(currency):
        return ['USD', 'JPY'].includes(currency)

    @staticmethod
    def get_rate(to_currency, from_currency):
        # Note: This is set to mimic a 3rd party api that is making an external request
        if random.randrange(20) == 1:
            raise RuntimeError("We're going down")

        time.sleep(random.randrange(3))
        return random.uniform(1.45, 1.5)
