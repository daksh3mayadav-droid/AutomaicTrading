from nsetools import Nse
import time

class MarketDataScanner:
    def __init__(self, config):
        self.config = config
        self.nse = Nse()

    def scan_market(self):
        snapshot = []
        for symbol in self.config.symbols:
            try:
                data = self.nse.get_quote(symbol)
                price = float(data['lastPrice'].replace(',', ''))
                volume = data.get('quantityTraded', 0)
                # Real RSI/MACD can be added here using prices, or mock for demo
                snapshot.append({
                    "symbol": symbol,
                    "price": price,
                    "volume": volume,
                    "rsi": 50,
                    "macd": 0,
                    "vwap_pos": "n/a",
                    "news_sentiment": "neutral"
                })
            except Exception as ex:
                print(f"Error fetching {symbol}: {ex}")
        return snapshot

    def market_closed(self):
        return False
