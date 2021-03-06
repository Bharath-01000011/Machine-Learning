# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 11:51:41 2021

@author: Bharath
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data = pd.read_csv('Transformed_Housing_Data2.csv')
data.head()
data['mean_sales'] = data['Sale_Price'].mean()
data['mean_sales'].head()
plt.figure(dpi=100)
k = range(0,len(data))
plt.scatter(k,data['Sale_Price'].sort_values(),color='green',label='Actual Sale Price')
plt.plot(k,data['mean_sales'].sort_values(),color='red',label='Mean_sales')
plt.xlabel('Fitted_points (Ascending)')
plt.ylabel('Sale Price')
plt.title('Overall Mean')
plt.legend
grades_mean = data.pivot_table(values = 'Sale_Price', columns ='Overall Grade', aggfunc=np.mean)
grades_mean
data['grade_mean'] = 0
for i in grades_mean.columns:
    data['grade_mean'][data['Overall Grade'] == i] = grades_mean[i][0]
data['grade_mean'].head()
mean_difference = data['mean_sales'] - data['Sale_Price']
grade_mean_difference = data['grade_mean'] - data['Sale_Price']
k = range(0, len(data))
l = [0 for i in range(len(data))]
plt.figure (figsize = (15,6), dpi = 100)
plt.subplot(1,2,1)
plt.scatter(k, mean_difference, color = 'red', label= 'Residuals', s=2)
plt.plot(k , l,color ='green', label='meaan Regression',linewidth=3)
plt.xlabel('Fitted points')
plt.ylabel('Residuals')
plt.title('Residuals with respect to Gradewise Mean')

plt.subplot(1,2,2)
plt.scatter(k, grade_mean_difference, color = 'red', label='Residuals', s=2)
plt.plot(k, l, color='green', label='mean Regression', linewidth = 3)
plt.xlabel('Fitted Points')
plt.ylabel('Residuals')
plt.legend()
plt.title('Residuals with respect to Gradewise Mean')
plt.legend()

cost = sum(mean_difference)/len(data)
print(round(cost,7))
y = data['Sale_Price']
y_hat1 = data['mean_sales']
y_hat2 = data['grade_mean']
n = len(data)

len(y) , len(y_hat1) , len(y_hat2), n
cost_mean = sum(abs(y_hat1 - y))/n
cost_mean
cost_grade_mean = sum(abs(y_hat2 - y))/n
cost_grade_mean
from sklearn.metrics import mean_absolute_error
cost_grade_mean = mean_absolute_error(y_hat2,y)
cost_grade_mean

from sklearn.metrics import mean_squared_error
cost_mean - mean_squared_error(y_hat1,y) ** 0.5
cost_grade_mean = mean_squared_error(y_hat2,y) ** 0.5
cost_mean , cost_grade_mean
y = data['Sale_Price']
y_bar = data['mean_sales']
y_hat = data['grade_mean']
n = len(data)
len(y) , len(y_bar) , len(y_hat)

mse_mean = mean_squared_error(y_hat,y)
mse_mean