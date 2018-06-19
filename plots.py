"""Simple plots a graph for the Ask prices for the last available candles.
Time frame defaults to 15 Minutes"""


# Still need to know how to make a candlestick plot.


import argparse
import oandapy
import matplotlib.pyplot as plt


parser = argparse.ArgumentParser()
parser.add_argument("--time_frame", default="M15", type=str,
                    help="Specify the time frame for the plot as command line option.")
args = parser.parse_args()

time_frame = args.time_frame


oanda = oandapy.API(environment="practice",
                    access_token="6a2232c67ebbc14e2be2758babe64aad-ed6636b4118a89be18e0a9976cf69bfb")
history = oanda.get_history(instrument="EUR_USD", granularity=time_frame)


# get to know what this stuff means
# lowAsk, highAsk, closeBid, openBid, openBid, closeAsk, openAsk


lowAsk = []
highAsk = []
openAsk = []
closeAsk = []
x = []


for i in range(0, 500):
    lowAsk.append(history['candles'][i]['lowAsk'])
    highAsk.append(history['candles'][i]['highAsk'])
    openAsk.append(history['candles'][i]['openAsk'])
    closeAsk.append(history['candles'][i]['closeAsk'])
    x.append(i)

plt.ylabel("Price")
plt.title("Time Frame {}".format(time_frame))
plt.plot(x, lowAsk)
plt.plot(x, highAsk)
plt.plot(x, closeAsk)
plt.plot(x, openAsk)

plt.show()
