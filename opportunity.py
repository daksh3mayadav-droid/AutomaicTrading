class OpportunityDetector:
    def __init__(self, config):
        self.threshold = config.confidence_threshold

    def detect(self, market_snapshot):
        setups = []
        for d in market_snapshot:
            conf = 60
            setup = None
            if d['rsi'] < 30 and d['macd'] > 0:
                setup = "VWAP Rebound"
                conf += 25
            elif d['rsi'] > 70:
                setup = "Overbought-Pullback"
                conf += 15
            else:
                setup = "None"
            if conf >= self.threshold:
                setups.append({
                    "symbol": d['symbol'],
                    "setup": setup,
                    "confidence": conf,
                    "entry": d['price'],
                    "stop": d['price'] * 0.99,
                    "target": d['price'] * 1.01,
                })
        return setups
