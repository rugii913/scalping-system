import os
import pyupbit
from dotenv import load_dotenv


class UpbitTrader:
    """업비트 API를 사용하여 거래 관련 기능을 수행하는 클래스"""

    def __init__(self):
        """
        클래스 초기화 시 .env 파일에서 API 키를 로드하고
        Upbit 객체를 생성하여 인증합니다.
        """
        load_dotenv()
        access_key = os.getenv("UPBIT_ACCESS_KEY")
        secret_key = os.getenv("UPBIT_SECRET_KEY")

        if not access_key or not secret_key:
            raise ValueError(
                "API 키가 .env 파일에 설정되지 않았습니다. UPBIT_ACCESS_KEY와 UPBIT_SECRET_KEY를 확인해주세요."
            )

        self.upbit = pyupbit.Upbit(access_key, secret_key)
        print("✅ UpbitTrader 초기화 및 API 인증 성공")

    def get_my_balances(self):
        """
        보유 중인 모든 자산의 잔고를 조회합니다.
        :return: 잔고 정보 리스트 (list of dictionaries) 또는 오류 발생 시 None
        """
        try:
            # get_balances()는 보유한 모든 화폐의 정보를 리스트 형태로 반환합니다.
            # 예: [{'currency': 'KRW', 'balance': '1000000.0', 'locked': '0.0', 'avg_buy_price': '0', 'avg_buy_price_modified': True, 'unit_currency': 'KRW'}, ...]
            return self.upbit.get_balances()
        except Exception as e:
            print(f"❌ 잔고 조회 중 오류 발생: {e}")
            return None

    def buy_market_order(self, ticker, budget):
        """
        시장가 매수 주문을 요청합니다.
        :param ticker: 마켓 티커 (예: "KRW-BTC")
        :param budget: 매수할 총액 (KRW)
        :return: 주문 결과 딕셔너리 또는 오류 발생 시 None
        """
        try:
            print(f"▶️ 시장가 매수 주문 시도: {ticker} / {budget:,.0f}원")
            # upbit.buy_market_order는 주문 성공 시 주문 정보를 담은 딕셔너리를 반환합니다.
            return self.upbit.buy_market_order(ticker, budget)
        except Exception as e:
            print(f"❌ 시장가 매수 주문 중 오류 발생: {e}")
            return None

    def sell_market_order(self, ticker, volume):
        """
        시장가 매도 주문을 요청합니다.
        :param ticker: 마켓 티커 (예: "KRW-BTC")
        :param volume: 매도할 수량
        :return: 주문 결과 딕셔너리 또는 오류 발생 시 None
        """
        try:
            print(f"◀️ 시장가 매도 주문 시도: {ticker} / {volume}개")
            # upbit.sell_market_order는 주문 성공 시 주문 정보를 담은 딕셔너리를 반환합니다.
            return self.upbit.sell_market_order(ticker, volume)
        except Exception as e:
            print(f"❌ 시장가 매도 주문 중 오류 발생: {e}")
            return None
