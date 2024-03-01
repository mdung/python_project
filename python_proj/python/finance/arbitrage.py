import ccxt
import time

class ArbitrageBot:
    def __init__(self, exchange1, exchange2, symbol, threshold_percentage=1.0):
        self.exchange1 = getattr(ccxt, exchange1)()
        self.exchange2 = getattr(ccxt, exchange2)()
        self.symbol = symbol
        self.threshold_percentage = threshold_percentage / 100.0

    def get_price_difference(self):
        ticker1 = self.exchange1.fetch_ticker(self.symbol)
        ticker2 = self.exchange2.fetch_ticker(self.symbol)
        price1 = ticker1['ask']
        price2 = ticker2['bid']
        return price1 - price2

    def arbitrage_opportunity(self):
        price_difference = self.get_price_difference()
        threshold = self.threshold_percentage * min(self.exchange1.fetch_ticker(self.symbol)['ask'],
                                                    self.exchange2.fetch_ticker(self.symbol)['bid'])
        return price_difference > threshold

    def execute_arbitrage(self):
        if self.arbitrage_opportunity():
            print("Arbitrage opportunity found!")
            orderbook1 = self.exchange1.fetch_order_book(self.symbol)
            orderbook2 = self.exchange2.fetch_order_book(self.symbol)
            buy_price = orderbook2['bids'][0][0]
            sell_price = orderbook1['asks'][0][0]

            print(f"Buy {self.symbol} on {self.exchange2.name} at {buy_price}")
            print(f"Sell {self.symbol} on {self.exchange1.name} at {sell_price}")

            # Place buy and sell orders here (use exchange.create_order)

    def run(self):
        while True:
            try:
                self.execute_arbitrage()
            except ccxt.NetworkError as e:
                print(f"Network error: {e}")
            except ccxt.ExchangeError as e:
                print(f"Exchange error: {e}")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")

            # Set the interval for checking arbitrage opportunities
            time.sleep(60)

if __name__ == '__main__':
    # Replace 'exchange1' and 'exchange2' with your preferred exchanges (e.g., 'binance', 'kraken')
    # Replace 'BTC/USD' with your desired trading pair
    bot = ArbitrageBot(exchange1='exchange1', exchange2='exchange2', symbol='BTC/USD', threshold_percentage=1.0)
    bot.run()
