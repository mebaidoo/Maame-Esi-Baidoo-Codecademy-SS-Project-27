import codecademylib3_seaborn
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("country_data.csv")
#Inspecting the data
print(data.head())
#Saving the life expectancy column to a variable
life_expectancy = data["Life Expectancy"]
#Finding the quartiles of life_expectancy
life_expectancy_quartiles = np.quantile(life_expectancy, [0.25, 0.5, 0.75])
print(life_expectancy_quartiles)
#Saving the gdp column to a variable
gdp = data["GDP"]
#Finding the median or 2-quantile of gdp
median_gdp = np.quantile(gdp, 0.5)
print(median_gdp)
#Selecting all the rows from data where GDP is less than or equal to median_gdp and higher than gdp to determine if a country's gdp affects the life expectancy of its people
low_gdp = data[data["GDP"] <= median_gdp]
high_gdp = data[data["GDP"] > median_gdp]
#Finding the quartiles of the life expectancy columns for both the low_gdp and high_gdp data
low_gdp_quartiles = np.quantile(low_gdp["Life Expectancy"], [0.25, 0.5, 0.75])
print(low_gdp_quartiles)
high_gdp_quartiles = np.quantile(high_gdp["Life Expectancy"], [0.25, 0.5, 0.75])
print(high_gdp_quartiles)
#Plotting histograms for the life expectancies column of both low_gdp and high gdp
plt.hist(high_gdp["Life Expectancy"], alpha = 0.5, label = "High GDP")
plt.hist(low_gdp["Life Expectancy"], alpha = 0.5, label = "Low GDP")
plt.legend()
plt.show()