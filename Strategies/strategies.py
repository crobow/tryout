import numpy as np

from position import Position


# Rename this file to moving_average.py since it already is a strategy.

def direction_moving_average(short_rate, long_rate):
    ma_short = np.mean(short_rate)
    ma_long = np.mean(long_rate)

    if ma_short > ma_long:
        return "buy"
    else:
        return "sell"


def moving_average(direction, instrument):
    return Position(buyer="ma", direction=direction, instrument="EUR_USD")
