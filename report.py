class DailyReport:
    def __init__(self, config):
        pass

    def generate(self, dashboard, pos_manager, opportunities):
        print("\n--- Daily Trading Report ---")
        print("P/L:", dashboard.daily_pl)
        print("Opportunities Considered:", len(opportunities))
        print("--- End of Report ---")
