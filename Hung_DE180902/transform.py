import pandas as pd
from IPython.display import display
# Read the CSV file into a DataFrame
df = pd.read_csv('Project ADY7.csv')

# Make changes to the DataFrame (e.g., add a new column)
df=df.drop('Unnamed: 0', axis=1)
df=df.T
df.columns=[2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022]
df.index=[0,1,2,3]

# Write the updated DataFrame to a new CSV file
df.to_csv('Project ADY7.csv', index=True)
