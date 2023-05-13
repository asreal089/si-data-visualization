from pandas import read_csv
from matplotlib import axes, pyplot as plt

data = read_csv('b3_stocks_1994_2020.csv')
filtered_data = data[data['ticker'] == 'IBOV11']
filtered_data_covid_impact = filtered_data[filtered_data['datetime'] >= '2019-01-01']
datetime_covid_impact = filtered_data_covid_impact['datetime']
close_price_covid_impact = filtered_data_covid_impact['close']
volume_covid_impact = filtered_data_covid_impact['volume']

datetime_historical_data = filtered_data['datetime']
close_price_historical_data = filtered_data['close']

plt.figure(figsize=(10, 6))
plt.plot(datetime_covid_impact, close_price_covid_impact, label='Close price BRL')

# Customizing the chart
plt.xlabel('Date')
plt.ylabel('Price')
plt.title('IBOV11')
plt.xticks(rotation=45, ha='right')
plt.yticks(rotation=45, ha='right')
plt.subplots_adjust(bottom=0.15)
plt.legend()

# Displaying the chart
plt.tight_layout()
plt.show()

plt.savefig('ibov11-covid-impact.png');


plt.figure(figsize=(10, 6))
axes = plt.gca()
axes.xaxis.set_major_locator(plt.MaxNLocator(nbins=11))
plt.plot(datetime_historical_data, close_price_historical_data, label='Close price BRL')
plt.xlabel('Date')
plt.ylabel('Price in BRL')
plt.title('IBOV11 historical data');
plt.xticks(rotation=45, ha='right');

plt.show()
plt.savefig('ibov11-historical-data.png');

plt.figure(figsize=(10, 6))
plt.bar(datetime_covid_impact, volume_covid_impact, label='Volume')
plt.xlabel('Date')
plt.ylabel('Volume')
plt.title('IBOV11 volume');
plt.xticks(rotation=45, ha='right');
plt.show()

