import random

class MarketDataScanner:
    def __init__(self, config):
        self.config = config

    def scan_market(self):
        # Demo: Mock market snapshot for each symbol
        snapshot = []
        for symbol in self.config.symbols:
            data = {
                "symbol": symbol,
                "price": round(1000 + random.random() * 500, 2),
                "volume": random.randint(100000, 500000),
                "rsi": random.randint(10, 90),
                "macd": random.gauss(0, 1),
                "vwap_pos": random.choice(["above", "below"]),
                "news_sentiment": random.choice(["positive", "neutral", "negative"])
            }
            snapshot.append(data)
        return snapshot

    def market_closed(self):
        return False
