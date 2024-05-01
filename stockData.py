import yfinance as yf

def get_current_price(stock):
    stock = yf.Ticker(stock)
    stock_info = stock.info
    real_time_price = stock_info.get('currentPrice')
    return real_time_price

def get_price_history(stock):
    stock = yf.Ticker(stock)
    stock_info = stock.history(start='2024-01-01', end='2024-01-07', interval='1m')
    return stock_info