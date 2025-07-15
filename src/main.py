from trader import UpbitTrader


def main():
    """
    UpbitTrader 클래스를 사용하여 내 잔고를 조회하고 출력합니다.
    """
    try:
        # UpbitTrader 객체를 생성합니다. (이 과정에서 API 인증이 일어남)
        trader = UpbitTrader()

        # 내 잔고 정보를 가져옵니다.
        my_balances = trader.get_my_balances()

        if my_balances:
            print("\n--- 💰 내 보유자산 ---")
            for balance in my_balances:
                currency = balance["currency"]
                amount = float(balance["balance"])

                # KRW(원화)와 암호화폐를 구분해서 출력
                if currency == "KRW":
                    print(f"💵 {currency}: {amount:,.0f} 원")
                else:
                    avg_price = float(balance["avg_buy_price"])
                    print(f"🪙 {currency}: {amount} (평균 매수가: {avg_price:,.0f} 원)")
            print("--------------------")
        else:
            print("조회된 잔고가 없습니다.")

        # --- 실제 주문 테스트 (주의!) ---
        # 아래 주석을 해제하면 실제 주문이 실행됩니다.
        # 업비트 최소 주문 금액은 5,000원입니다. 소액으로 충분히 테스트 후 사용하세요.

        # # [1] 시장가 매수 테스트 (예: 5,000원어치 비트코인 매수)
        # ticker_to_buy = "KRW-BTC"
        # budget_to_buy = 5000
        # buy_result = trader.buy_market_order(ticker_to_buy, budget_to_buy)
        # if buy_result:
        #     print("\n--- 매수 주문 결과 ---")
        #     print(buy_result)
        #     print("--------------------")

        # # [2] 시장가 매도 테스트 (예: 보유한 비트코인 전부 매도)
        # # 먼저 내가 가진 비트코인 잔고를 확인합니다.
        # btc_balance = trader.upbit.get_balance("BTC")
        # if btc_balance and btc_balance > 0:
        #     ticker_to_sell = "KRW-BTC"
        #     sell_result = trader.sell_market_order(ticker_to_sell, btc_balance)
        #     if sell_result:
        #         print("\n--- 매도 주문 결과 ---")
        #         print(sell_result)
        #         print("--------------------")
        # else:
        #     print("\n매도할 비트코인이 없습니다.")

    except ValueError as ve:
        # UpbitTrader 초기화 시 발생할 수 있는 API 키 오류
        print(f"오류: {ve}")
    except Exception as e:
        print(f"메인 로직 실행 중 오류가 발생했습니다: {e}")


if __name__ == "__main__":
    main()
