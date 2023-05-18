from pandas import read_csv
from matplotlib import axes, pyplot as plt

data = read_csv('covid-vaccination-vs-death_ratio.csv')
filtered_data_brazil = data[data['iso_code'] == 'BRA']
filtered_data_brazil_date = filtered_data_brazil['date']
filtered_data_brazil_new_death = filtered_data_brazil['New_deaths']

plt.figure(figsize=(10, 6))
plt.plot(filtered_data_brazil_date, filtered_data_brazil_new_death, label='new Covid-19 deaths in Brazil')

# Customizing the chart
plt.xlabel('Date')
plt.ylabel('Deaths')
plt.title('Covid-19 deaths in Brazil')
plt.xticks(rotation=45, ha='right')
plt.yticks(rotation=45, ha='right')
plt.subplots_adjust(bottom=0.15)
plt.legend()
axes = plt.gca()
axes.xaxis.set_major_locator(plt.MaxNLocator(nbins=11))

# Displaying the chart
plt.tight_layout()
plt.show()
