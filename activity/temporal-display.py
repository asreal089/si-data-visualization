from pandas import read_csv
from matplotlib import pyplot as plt

data = read_csv('b3_stocks_1994_2020.csv')
filtered_data = data[data['ticker'] == 'IBOV11']
filtered_data_covid_impact = filtered_data[filtered_data['datetime'] >= '2019-01-01']
datetime = filtered_data_covid_impact['datetime']
close_price = filtered_data_covid_impact['close']

plt.figure(figsize=(10, 6))
plt.plot(datetime, close_price, label='Close price BRL')

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
