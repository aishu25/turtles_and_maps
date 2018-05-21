import urllib
import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime

import mpld3

def image():
	url = "https://min-api.cryptocompare.com/data/histohour?fsym=XMR&tsym=EUR&limit=100"
	page = requests.get(url)
	data = page.json()['Data']
	df = pd.DataFrame(data)
	df['timestamp'] = [datetime.datetime.fromtimestamp(d) for d in df.time]
	print "timestamp : ", df['timestamp']
	print "df.close", df.close
	plt.plot(df.timestamp, df.close)
	plt.xticks(rotation=30)
	# plt.rcParams["figure.figsize"] = (20,3)
	fig = plt.gcf()
	fig.set_size_inches(18.5, 10.5, forward=True)
	plt.show()
	fig.savefig("graphy.png", dpi=None)
image()

















