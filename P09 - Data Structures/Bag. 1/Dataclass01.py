# Belajar Named Tuple
from dataclasses import dataclass

@dataclass
class Stock:
    symbol: str
    current: float
    high: float
    low: float
    
    def __str__(self):
        return f"Stock(symbol={self.symbol}, current={self.current}, high={self.high}, low={self.low})"
   
class StockPortfolio:
    def __init__(self):
        self.stocks = []

    def add_stock(self, stock: Stock):
        self.stocks.append(stock)

    def calculate_portfolio_value(self):
        total_value = sum(stock.current for stock in self.stocks)
        return total_value
    
def main():
    # Menggunakan urutan (positions)
    # d1 = Stock("APPL", 123.52, 137.98, 53.15)
    # print("d1: ", d1)
    
    # # Dataclass isinya dapat diubah
    # d1.symbol = "HUAW"
    
    # # Akses menggunakan atribut
    # print("d1.symbol:   ", d1.symbol)
    # print("d1.current:  ", d1.current)
    # print("d1.high:     ", d1.high)
    # print("d1.low:      ", d1.low)
    
    # # Bisa tambah atribut seperti kelas biasa
    # d1.tambahan = 100.20
    # print("d1.tambahan: ", d1.tambahan)
    # # tetapi tidak tampil kalau di print keseluruhan
    # print("d1: ", d1)
    
    
    # # Perbandingan sudah built-in pada dataclass
    # d2 = Stock("HUAW", 123.52, 137.98, 53.15)
    # print("d2: ", d2)
    # if (d1 == d2):
    #     print("d1 == d2")
    # else:
    #     print("d1 != d2")
        
        
    # mencoba modifikasi memakai materi seblmna
    portfolio = StockPortfolio()

    stock1 = Stock("APPL", 123.52, 137.98, 53.15)
    stock2 = Stock("HUAW", 100.0, 110.0, 90.0)

    portfolio.add_stock(stock1)
    portfolio.add_stock(stock2)

    print("Stocks in Portfolio:")
    for stock in portfolio.stocks:
        print(stock)

    try:
        stock1.symbol = "GOOGL"
    except AttributeError as e:
        print(f"Error: {e}")

    custom_stock = {"symbol": "MSFT", "current": 150.0, "high": 160.0, "low": 140.0}
    portfolio.add_stock(Stock(**custom_stock))

    print("\nUpdated Stocks in Portfolio:")
    for stock in portfolio.stocks:
        print(stock)

    total_portfolio_value = portfolio.calculate_portfolio_value()
    print(f"\nTotal Portfolio: {total_portfolio_value}")
    
    
    
if __name__ == "__main__":
    main()