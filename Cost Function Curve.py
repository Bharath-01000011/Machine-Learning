# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 11:39:38 2021

@author: Bharath
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


data = pd.read_csv('Transformed_Housing_Data2.csv')

sale_price = data['Sale_Price'].head(30)
flat_area = data['Flat Area (in Sqft)'].head(30)
sample_data = pd.DataFrame({'sale_price' : sale_price, 'flat_area' : flat_area})
sample_data


plt.figure(dpi=150)
plt.scatter(sample_data.flat_area , sample_data.sale_price, color='red')
plt.xlabel('Flat Area')
plt.ylabel('Sale Price')
plt.legend()
plt.show


sample_data['mean_sale_price'] = sample_data.sale_price.mean()
plt.figure(dpi=150)
plt.scatter(sample_data.flat_area , sample_data.sale_price , color='green')
plt.plot(sample_data.flat_area , sample_data.mean_sale_price , color='yellow' , label='Mean Sale Price')
plt.xlabel('Flat Area')
plt.ylabel('Mean Sale Price')
plt.legend()
plt.show


c = 0
m = 0
line = []
from sklearn.metrics import mean_squared_error as mse

for i in range(len(sample_data)):
    line.append((sample_data.flat_area[i] * m) + c )

plt.figure(dpi = 150)
plt.scatter(sample_data.flat_area , sample_data.sale_price , color = 'red')
plt.plot(sample_data.flat_area , line , label = 'm=0.0   c=0')
plt.xlabel('Flat Area')
plt.ylabel('Sale Price')
MSE = mse(sample_data.sale_price , line)
plt.title('Slope '+str(m)+' with MSE '+str(MSE))
plt.show


c = 0
m = 50
line = []
from sklearn.metrics import mean_squared_error as mse

for i in range(len(sample_data)):
    line.append((sample_data.flat_area[i] * m) + c )

plt.figure(dpi = 150)
plt.scatter(sample_data.flat_area , sample_data.sale_price , color = 'red')
plt.plot(sample_data.flat_area , line , label = 'm=50   c=0')
plt.xlabel('Flat Area')
plt.ylabel('Sale Price')
MSE = mse(sample_data.sale_price , line)
plt.title('Slope '+str(m)+' with MSE '+str(MSE))
plt.show

def slope_error(slope , intercept ,sample_data):
    sale = []
    for i in range(len(sample_data.flat_area)):
        tmp = sample_data.flat_area[i] * slope + intercept
        sale.append(tmp)
    MSE = mse(sample_data.sale_price , sale)
    return (MSE)

slope = [i/10 for i in range(0,5000)]
Cost = []
for i in slope:
    cost = slope_error(slope=i , intercept=0 , sample_data = sample_data)
    Cost.append(cost)

cost_table = pd.DataFrame({ 'slope' : slope , 'Cost' : Cost})
cost_table.tail()

plt.plot(cost_table.slope , cost_table.Cost , label = 'Cost Function Curve')
plt.xlabel('Value of the slope')
plt.ylabel("Cost")
plt.legend()
plt.show


def int_error(slope , intercept ,sample_data):
    sale = []
    for i in range(len(sample_data.flat_area)):
        tmp = sample_data.flat_area[i] * slope + intercept
        sale.append(tmp)
    MSE = mse(sample_data.sale_price , sale)
    return (MSE)

intercept = [i for i in range(5000,50000)]
Cost = []
for i in intercept:
    cost = int_error(slope= 234 , intercept= i , sample_data = sample_data)
    Cost.append(cost)

int_table = pd.DataFrame({ 'intercept' : intercept , 'Cost' : Cost})
int_table.tail()


plt.plot(int_table.intercept , int_table.Cost , label = 'Cost Function Curve')
plt.xlabel('Value of the intercept')
plt.ylabel("Cost")
plt.legend()
plt.show