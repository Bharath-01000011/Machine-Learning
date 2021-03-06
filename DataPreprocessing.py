# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 10:30:10 2021

@author: Bharath
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
data.describe()
data['Sale Price'].describe()
import seaborn as sns
sns.boxplot(x=data['Sale Price'])
q1 = data['Sale Price'].quantile(0.25)
q3 = data['Sale Price'].quantile(0.75)
iqr = q3 - q1
lower_quartile = q1 - (1.5 * iqr)
upper_quartile = q3 + (1.5 * iqr)
(lower_quartile , upper_quartile)
def limit_changer(value):
    if value > upper_quartile :
        return upper_quartile
    if value < lower_quartile:
        return lower_quartile
    else:
        return value

data['Sale Price'] = data['Sale Price'].apply(limit_changer)
data['Sale Price'].head(10)
data.dropna(inplace=True , axis =0 , subset = ['Sale Price'])
plt.hist(data['Sale Price'] , bins = 10 , color = 'red')
numerical_variables = ['No of Bathrooms' , 'Flat Area (in Sqft)' , 'Lot Area (in Sqft)' , 'Area of the House from Basement (in Sqft)' , 'Latitude' , 'Longitude' , 'Living Area after Renovation (in Sqft)']
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values = np.nan , strategy = 'median')
data[numerical_variables] = imputer.fit_transform(data[numerical_variables])
column = data['Zipcode'].values.reshape(-1,1)
column.shape
imputer = SimpleImputer (missing_values = np.nan , strategy = 'most_frequent')
data['Zipcode'] = imputer.fit_transform(column)
data['Zipcode'] = data['Zipcode'].astype(object)
mapping = {'None' : '0',
            'Once' : '1',
            'Twice' : '2',
            'Thrice' : '3',
            'Four' : '4'}
data['No of Times Visited'] = data['No of Times Visited'].map(mapping)
data['Ever Renovated'] = np.where(data['Renovated Year'] == 0, 'No', 'Yes')
data['Purchase Year'] = pd.DatetimeIndex(data['Date House was Sold']).year
data['Years Since Renovation'] = np.where(data['Ever Renovated'] == 'Yes', abs(data['Purchase Year'] - data['Renovated Year']),0)
data.drop(columns =['Purchase Year' , 'Date House was Sold' , 'Renovated Year'], inplace=True)
data['Condition of the House'].value_counts()
data.groupby('Condition of the House', )['Sale Price'].mean().plot(kind='bar')
data.groupby('Condition of the House', )['Sale Price'].mean().sort_values().plot(kind='bar')
from statsmodels.formula.api import ols
import statsmodels.api as sm
data = data.rename(columns = {'Sale Price' : 'Sale_Price'})
data = data.rename(columns = {'Condition of the House' : 'Condition_of_the_House'})
data = data.rename(columns = {'Ever Renovated' : 'Ever_Renovated'})
data = data.rename(columns = {'Waterfront View' : 'Waterfront_View'})
model = ols('Sale_Price ~ Condition_of_the_House' , data = data).fit()
anova_table = sm.stats.anova_lm(model , typ=2)
print(anova_table)
model = ols('Sale_Price ~ Waterfront_View ' , data = data).fit()
anova_table = sm.stats.anova_lm(model , typ = 2)
anova_table
model = ols('Sale_Price ~ Ever_Renovated' , data = data).fit()
anova_table = sm.stats.anova_lm(model , typ = 2)
anova_table
data = pd.get_dummies(data , columns = ['Condition_of_the_House'] , drop_first = True)
data.head(10)
data = pd.get_dummies(data , columns = ['Waterfront_View'] , drop_first = True)
data.head(10)
y = data.iloc[:,0]
x = data.iloc[:,1:31]
from sklearn.model_selection import train_test_split
x_train , x_test , y_train , y_test = train_test_split (x,y,test_size=0.3)
from sklearn import preprocessing
scale = preprocessing.StandardScaler()
x_train = scale.fit_transform(x_train)
x_test = scale.fit_transform(x_test)