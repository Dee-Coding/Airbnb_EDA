# Airbnb Exploratory Data Analysis (EDA)

This repository contains Python code to perform an exploratory data analysis (EDA) on Airbnb listings data. 
The analysis focuses on factors such as price, availability, location, and property type to identify trends and patterns in the demand for Airbnb listings in a city.

## Getting Started

1. **Data:** Download the Airbnb listings data for your city from [the provided link](http://insideairbnb.com/get-the-data/). Make sure to have the necessary data files, including listings, reviews, and related datasets.

2. **Setup:** Ensure you have Python installed on your system. You can also set up a virtual environment if desired.

3. **Dependencies:** Install the required Python libraries by running the following command:
    pip install pandas numpy matplotlib seaborn

5. **Running the Code:** Save the code provided in a `.py` file and run it using a Python interpreter. You will be prompted to enter the data file path.

## Code Overview

1. **Data Loading:** The code loads the Airbnb listings data from the specified file path using Pandas.

2. **Data Preprocessing:** Rows with availability_365 equal to 0 are dropped. A subset of relevant columns (neighbourhood, room_type, availability_365, price) is created.

3. **Statistical Analysis:** The code calculates and prints the mean prices for different neighborhoods using a loop.

4. **Data Visualization:** The distribution of prices and the relationship between price and availability are visualized using histograms and scatter plots.

5. **Price by Property Type:** A box plot is created to explore the distribution of prices by property type.

## Results

The EDA provides insights into the Airbnb listings data, revealing patterns in prices, availability, and property types. The code generates visualizations that help in understanding the distribution of prices and their relationship with availability and property types.

