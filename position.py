import oandapy


OANDA = oandapy.API(environment="practice",
                    access_token="6a2232c67ebbc14e2be2758babe64aad-ed6636b4118a89be18e0a9976cf69bfb")

ACCOUNT = 1813880

# Changes for different position types like market and limit order.
# also check if order has become a position.


class Position:

    def __init__(self, buyer, direction, instrument="EUR_USD"):
        self.instrument = instrument
        self.buyer = buyer
        self.direction = direction
        self.position_open = False

    def open_position(self):
        OANDA.create_order(account_id=ACCOUNT,
                           type='market',
                           instrument=self.instrument,
                           units=10,
                           side=self.direction,
                           )
        self.position_open = True

    def close_position(self):
        OANDA.close_position(account_id=ACCOUNT,
                             instrument=self.instrument
                             )
        self.position_open = False
