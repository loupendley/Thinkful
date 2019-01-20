https://plot.ly/matplotlib/histograms/

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
filename = '/Users/lou/GITHubProjects/Thinkful/Datafiles/planecrashinfo_20181121001952_clean.csv'
# crashes = pd.read_csv(filename, quotechar='"')
crashes = pd.read_csv(filename)
crashes_df = crashes[['country_code', 'operator_code', 'ac_type', 'aboard_count', 'fatal_count', 'ground']]

# let's remove all the NaN's for the numeric data types
crashes_df = crashes_df.dropna(subset=['aboard_count'])
crashes_df = crashes_df.dropna(subset=['fatal_count'])  
crashes_df = crashes_df.dropna(subset=['ground'])

# let's strip off all leading and trailing spaces from the numeric data types
crashes_df = crashes_df[(crashes_df['aboard_count'].str.strip() != '?')] # remove unknown aboard_cont
crashes_df = crashes_df[(crashes_df['ground'].str.strip()       != '?')]       # remove unknown ground count
crashes_df = crashes_df[(crashes_df['fatal_count'].str.strip()  != '?')]  # remove unknown fatal_count

# let's convert all of these numeric data types to numerics
crashes_df['ground']       = pd.to_numeric(crashes_df['ground'])
crashes_df['aboard_count'] = pd.to_numeric(crashes_df['aboard_count'])
crashes_df['fatal_count']  = pd.to_numeric(crashes_df['fatal_count'])
print("there are now {} clean rows of data in crashes_df.".format(len(crashes_df)))
print(crashes_df.columns)

FATALITIES = 150
# we only want big crashes, more than n fatalties
crashes_big = crashes_df[(crashes_df['fatal_count']  > FATALITIES)]
crashes_df = crashes_big
print("We are working with {} airline crashes, rows of more than {} fatalities.".format(len(crashes_df), FATALITIES))

crashes_df_country = crashes_df[['country_code', 'aboard_count', 'fatal_count', 'ground']]
crashes_df_operator = crashes_df[['operator_code', 'aboard_count', 'fatal_count', 'ground']]
crashes_df_ac_type = crashes_df[['ac_type', 'aboard_count', 'fatal_count', 'ground']]
print("For df crashes_df_country, the columns are {}".format(crashes_df_country.columns))
print("For df crashes_df_country, the columns are {}".format(crashes_df_operator.columns))
print("For df crashes_df_country, the columns are {}".format(crashes_df_ac_type.columns))
crashes2 = crashes_df.sort_values('country_code',ascending=True)

plt.hist(crashes_df['aboard_count'])
plt.title("Crashes Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")
fig = plt.gcf()