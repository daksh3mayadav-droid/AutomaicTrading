from broker_api_mock import BrokerAPIMock

class TradeExecutor:
    def __init__(self, config):
        if config.paper_trading:
            self.broker = BrokerAPIMock()
        else:
            pass

    def execute(self, opportunity):
        trade = self.broker.place_order(
            symbol=opportunity["symbol"],
            side="BUY",
            price=opportunity["entry"],
            quantity=10
        )
        return trade
