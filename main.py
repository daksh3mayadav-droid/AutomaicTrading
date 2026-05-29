from config import Config
from market_data import MarketDataScanner
from opportunity import OpportunityDetector
from risk import RiskAssessor
from execution import TradeExecutor
from position import PositionManager
from risk_dashboard import RiskDashboard
from learn import LearningEngine
from report import DailyReport


def main():
    config = Config()
    dashboard = RiskDashboard(config)
    scanner = MarketDataScanner(config)
    detector = OpportunityDetector(config)
    assessor = RiskAssessor(config)
    executor = TradeExecutor(config)
    pos_manager = PositionManager(config)
    learner = LearningEngine(config)
    reporter = DailyReport(config)

    session_active = True
    while session_active and dashboard.trading_allowed():
        market_snapshot = scanner.scan_market()
        opportunities = detector.detect(market_snapshot)
        for opp in opportunities:
            if dashboard.risk_breached():
                session_active = False
                print("Trading halted due to risk breach.")
                dashboard.generate_report()
                break

            if assessor.assess(opp):
                trade = executor.execute(opp)
                dashboard.update(trade)
                pos_manager.manage(trade, market_snapshot, dashboard)
            else:
                continue

        if scanner.market_closed():
            session_active = False
            break

    learner.analyze_trades(dashboard.history)
    reporter.generate(dashboard, pos_manager, opportunities)

if __name__ == "__main__":
    main()
