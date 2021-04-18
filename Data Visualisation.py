# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 11:47:39 2021

@author: Bharath
"""

import pandas as pd
import numpy as np
import matplotlib as plt
data.dtypes
data.head(10)
data['Sale Price'].mean()
data['Sale Price'].min()
data['Sale Price'].max()
data['Sale Price'].quantile(.25)
data['Sale Price'].quantile(.75)
data['Condition of the House'].unique()
import numpy as np
np.std(data['Sale Price'])
np.std(data['Sale Price'],ddof=1)
import matplotlib.pyplot as plt
plt.plot(data['Sale Price'],color='orange')
plt.plot(data['Sale Price'],color='Red')
plt.xlabel("Record Number")
plt.ylabel('Sale Price')
plt.title("Housing Graph")
plt.show
plt.plot(data['Sale Price'],marker='o',markerfacecolor='Blue',color='red',markersize=8,linewidth=5,linestyle='dashed')
data.groupby('Condition of the House')['ID'].count()
values = [30,2702,14031,5679,172]
labels = ['Bad','Excellent','Fair','Good','Okay']
#Pie Chart
plt.pie(values,labels=labels)
#Bar Chart
plt.bar(labels,values,color= 'blue')
plt.bar(labels,values,color='red')
plt.xlabel('Condition of the House')
plt.ylabel('Count of the House')
plt.title('Housing Graph')
plt.show()
#Scatter Plot
plt.scatter(x = data['Flat Area (in Sqft)'] ,y = data['Sale Price'] , color = 'Red')
plt.xlabel('Area')
plt.ylabel('Sale Price')
plt.title('Housing Graph')
plt.show()

plt.scatter(x = data['No of Bathrooms'] ,y = data['Sale Price'] , color = 'Red')
plt.xlabel('No of Bathrooms')
plt.ylabel('Sale Price')
plt.title('Housing Graph')
plt.show()

#Histogram
plt.hist(data['Age of House (in Years)'],bins = 10)

#Boxplot
plt.boxplot(data['Age of House (in Years)']