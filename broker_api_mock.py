import random

class BrokerAPIMock:
    def place_order(self, symbol, side, price, quantity):
        fill_price = price + random.uniform(-0.1, 0.1)
        return {
            "symbol": symbol,
            "side": side,
            "entry": price,
            "fill_price": fill_price,
            "quantity": quantity,
            "pnl": random.uniform(-5, 15)
        }
