class RiskDashboard:
    def __init__(self, config):
        self.daily_pl = 0
        self.drawdown = 0
        self.max_daily_loss = config.max_daily_loss
        self.max_drawdown = config.max_drawdown
        self.history = []

    def update(self, trade):
        self.daily_pl += trade.get('pnl', 0)
        self.history.append(trade)

    def trading_allowed(self):
        return (self.daily_pl > self.max_daily_loss) and (self.drawdown > self.max_drawdown)

    def risk_breached(self):
        return (self.daily_pl <= self.max_daily_loss) or (self.drawdown <= self.max_drawdown)

    def generate_report(self):
        print("Risk report triggered!")
