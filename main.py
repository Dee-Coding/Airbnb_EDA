import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Get the data file path
data_file = input("Enter the data file path: ")
# Read the Airbnb listings data into a Pandas DataFrame
df = pd.read_csv(data_file)

# Get some basic information about the data
df.info()

# Drop rows where availability_365 is 0
df = df[df['availability_365'] != 0]

# Subset the columns
new_df = df[['neighbourhood', 'room_type', 'availability_365', 'price']]
print(new_df.info())

# Statistical Analysis: T-test to compare mean prices in different neighborhoods
neighborhoods = new_df['neighbourhood'].unique()

for neighbourhood in neighborhoods:
    subset = new_df.loc[new_df['neighbourhood'] == neighbourhood, 'price']
    mean_price = subset.mean()
    print(f"Mean price in {neighbourhood}: {mean_price:.2f}")

# Explore the distribution of prices
plt.figure(figsize=(10, 6))
sns.histplot(data=new_df, x='price', bins=30, kde=True)
plt.xlabel('Price')
plt.ylabel('Frequency')
plt.title('Distribution of Prices')
plt.show()

# Scatter Plot of Price vs Availability
plt.figure(figsize=(10, 6))
sns.scatterplot(data=new_df, x='availability_365', y='price', alpha=0.5)
plt.xlabel('Availability (365 days)')
plt.ylabel('Price')
plt.title('Relationship between price and availability')
plt.show()

# Explore the distribution of prices by property type
sns.boxplot(x='room_type', y='price', data=new_df)
plt.xlabel('Property type')
plt.ylabel('Price')
plt.title('Distribution of prices by property type')
plt.show()