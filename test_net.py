import yfinance as yf
import requests

def test():
    print("正在尝试连接 Yahoo Finance (带伪装头)...")
    USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    
    try:
        session = requests.Session()
        session.headers.update({'User-Agent': USER_AGENT})
        
        ticker = yf.Ticker("AAPL", session=session)
        info = ticker.info
        if "longName" in info:
            print(f"OK - Company: {info['longName']}")
        else:
            print("OK - But no data found.")
    except Exception as e:
        print(f"Fail: {str(e)}")

if __name__ == "__main__":
    test()
