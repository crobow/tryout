import oandapy


OANDA = oandapy.API(environment="practice",
                    access_token="6a2232c67ebbc14e2be2758babe64aad-ed6636b4118a89be18e0a9976cf69bfb")

ACCOUNT = 1813880


class History:

    def __init__(self, instrument, timeframe):
        self.history = OANDA.get_history(instrument=instrument, granularity=timeframe)

    def low_bid(self):
        """This is to this point completely not scalable and just works for M15 or similar..
        """

        low_bid = []

        for i in range(0, 500):
            low_bid.append(self.history['candles'][i]['lowBid'])

        return low_bid

    def refresh(self):
        # refresh history at every new run.
        # get new candle element and append to history list
        # delete first element of list
        pass
