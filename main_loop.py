import time

from history import History
from Strategies.strategies import moving_average, direction_moving_average


def wait_for_new_candle():
    """This waits for the new candle.
    It is not as easy as just sleeping for a certain amount of time!!
    """

    time.sleep(15)


# Initialize all Strategies.
M15 = History(instrument="EUR_USD", timeframe="M15")
H1 = History(instrument="EUR_USD", timeframe="M1")

ma = moving_average(direction=direction_moving_average(
    short_rate=M15, long_rate=H1), instrument="EUR_USD")


while True:

    wait_for_new_candle()
    
    M15.refresh()
    H1.refresh()

    if not ma.position_open:
        ma.open_position()
    else:
        if direction_moving_average(short_rate="M1", long_rate="H1") \
                is not ma.direction:
            ma.close_position()
