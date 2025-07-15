import os
import pyupbit
from dotenv import load_dotenv


def main():
    """
    업비트 API를 사용하여 비트코인의 현재가를 조회하고 출력합니다.
    """
    # .env 파일에서 환경 변수를 불러옵니다.
    load_dotenv()

    # 환경 변수에서 API 키를 읽어옵니다.
    access_key = os.getenv("UPBIT_ACCESS_KEY")
    secret_key = os.getenv("UPBIT_SECRET_KEY")

    # API 키가 있는지 확인합니다.
    if not access_key or not secret_key:
        print("오류: .env 파일에 UPBIT_ACCESS_KEY와 UPBIT_SECRET_KEY를 설정해주세요.")
        return

    try:
        # pyupbit 객체를 생성합니다. (API 키 인증)
        upbit = pyupbit.Upbit(access_key, secret_key)
        print("✅ 업비트 API 인증에 성공했습니다.")

        # KRW-BTC (비트코인)의 현재가를 조회합니다.
        ticker = "KRW-BTC"
        current_price = pyupbit.get_current_price(ticker)

        if current_price:
            # 보기 좋게 쉼표를 넣어서 출력합니다.
            print(f"📈 [{ticker}] 현재가: {current_price:,.0f} 원")
        else:
            print(f"오류: {ticker}의 가격을 조회할 수 없습니다.")
    except Exception as e:
        print(f"오류가 발생했습니다: {e}")


if __name__ == "__main__":
    main()
