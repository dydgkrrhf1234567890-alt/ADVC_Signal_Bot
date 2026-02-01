class AladdinShield:
    def __init__(self):
        self.stop_loss_pct = -0.03  # -3% 손실 시 무조건 손절 (방어)
        self.take_profit_pct = 0.05 # +5% 수익 시 익절 (수확)
        print(">>> [Aladdin Shield] Risk Management System Activated.")

    def check_risk(self, current_price, buy_price):
        """
        현재 가격과 매수 가격을 비교하여
        방패를 들어야 할지(매도), 기다려야 할지(홀딩) 판단합니다.
        """
        if buy_price == 0:
            return "WAIT"

        # 수익률 계산
        profit_rate = (current_price - buy_price) / buy_price

        # 1. 위험 감지: 손절매 (Stop Loss)
        if profit_rate <= self.stop_loss_pct:
            print(f"🚨 WARNING: 손실율 {profit_rate*100:.2f}% 도달! 알라딘 방패 발동! -> 전량 매도")
            return "SELL_STOP_LOSS"

        # 2. 이익 확정: 익절 (Take Profit)
        elif profit_rate >= self.take_profit_pct:
            print(f"💰 SUCCESS: 수익률 {profit_rate*100:.2f}% 달성! 황금 수확 시작! -> 전량 매도")
            return "SELL_TAKE_PROFIT"

        # 3. 안전 구간: 홀딩 (Hold)
        else:
            return "HOLD"
