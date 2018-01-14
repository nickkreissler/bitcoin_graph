from exchanges.base import Exchange, FuturesExchange


class Poloniex(Exchange):

    TICKER_URL = 'https://poloniex.com/public?command=returnTicker'

    @classmethod
    def _current_price_extractor(cls, data,arg):
        try:
            return data.get(arg).get('last')
        except:
            print('error')
    @classmethod
    def _current_bid_extractor(cls, data):
        return data.get('USDT_BTC').get('highestBid')

    @classmethod
    def _current_ask_extractor(cls, data):
        return data.get('USDT_BTC').get('lowestAsk')
