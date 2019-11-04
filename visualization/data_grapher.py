import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('dataset/london_crime_by_lsoa.csv')

# tables for crime frequency by caegories
crime_frequency_by_major = df['major_category'].value_counts()
crime_frequency_by_minor = df['minor_category'].value_counts()

# crime_frequency_by_major.plot(kind='bar')
# plt.show()
# crime_frequency_by_minor.plot(kind='bar')
# plt.show()

# tables for crime frequency by borough
crime_frequency_by_borough = df['borough'].value_counts()

# crime_frequency_by_borough.plot(kind='bar')
# plt.show()

# tables for crime frequeny by month
crime_frequency_by_month = df['month'].value_counts()
crime_frequency_by_month = crime_frequency_by_month.sort_index()

# crime_frequency_by_month.plot(kind='bar')
# plt.show()

# tables for crime frequenc by year
crime_frequency_by_year = df['year'].value_counts()
crime_frequency_by_year = crime_frequency_by_year.sort_index()

# convert to data frame
crime_frequency_by_year_df = pd.DataFrame({'year':crime_frequency_by_year.index, 'crime frequency':crime_frequency_by_year.values})

# crime_frequency_by_year_df.plot(kind='scatter', x='year', y='crime frequency')
# plt.show()

# rates of crimes for a certain borough
df1 = df[['borough', 'minor_category']].groupby(['borough', 'minor_category']).minor_category.agg('count')

# df1[214:246].plot(kind='bar')
# plt.show()
