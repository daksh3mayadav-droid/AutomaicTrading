class Config:
    # All tunable parameters & thresholds centralized here
    def __init__(self):
        self.confidence_threshold = 75
        self.max_daily_loss = -0.01  # -1% daily
        self.max_drawdown = -0.03    # -3%
        self.max_pos_size = 0.20     # 20%
        self.market_open_time = "09:15"
        self.market_close_time = "15:25"
        self.symbols = ["INFY", "RELI", "TCS"]  # Demo only
        self.paper_trading = True
        # Add API keys, DB paths etc here as needed
