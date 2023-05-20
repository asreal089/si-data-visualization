from pandas import read_csv
from matplotlib import axes, pyplot as plt

import plotly.express as px

data = read_csv('covid-vaccination-vs-death_ratio.csv')
filtered_data_brazil = data[data['iso_code'] == 'BRA']
filtered_data_brazil_date = filtered_data_brazil['date']
filtered_data_brazil_new_death = filtered_data_brazil['New_deaths']
filtered_data_brazil_vacination = filtered_data_brazil['ratio']

plt.figure(figsize=(10, 6))
plt.plot(filtered_data_brazil_date, filtered_data_brazil_new_death, label='new Covid-19 deaths in Brazil', color='red')

# Customizing the chart
plt.xlabel('Date')
plt.ylabel('Deaths')
plt.title('Covid-19 deaths in Brazil')
plt.xticks(rotation=45, ha='right')
plt.yticks(rotation=45, ha='right')
plt.subplots_adjust(bottom=0.15)
plt.legend()

ax2 = plt.twinx()
color = 'tab:blue'
ax2.set_ylabel('Vaccination ratio in population', color=color)
ax2.bar(filtered_data_brazil_date, filtered_data_brazil_vacination, color=color, alpha=0.3)
ax2.tick_params(axis='y', labelcolor=color)
axes = plt.gca()
axes.xaxis.set_major_locator(plt.MaxNLocator(nbins=11))

# Displaying the chart
plt.tight_layout()
plt.show()

#geo scatter chart

# Consoling the data
consolidated_data_iso_and_deaths = data[['iso_code','New_deaths', 'country']]

consolidated_data = consolidated_data_iso_and_deaths.groupby(['iso_code', 'country'],as_index=False).sum()


fig = px.scatter_geo(consolidated_data, locations="iso_code", color="country", hover_name="country", size="New_deaths", projection="natural earth")
fig.show()