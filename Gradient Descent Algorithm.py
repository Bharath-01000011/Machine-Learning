# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 11:49:36 2021

@author: Bharath
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def param_init(y):
    m = 0.1
    c = y.mean()
    return (m,c)


def generate_prediction(m , c, x):
    prediction = []
    for i in x:
        pred = (m * i) + c
        prediction.append(pred)
    return prediction


def compute_cost(prediction , y):
    n = len(y)
    cost = np.sum((prediction - y) ** 2 / n)
    return cost


def gradient(prediction , y, x):
    n = len(y)
    Gm = 2/n * np.sum((prediction - y) * x)
    Gc = 2/n * np.sum((prediction - y))
    return Gm,Gc


def param_update(m_old , c_old , Gm_old , Gc_old , alpha):
    m_new = m_old - (alpha * Gm_old)
    c_new = c_old - (alpha * Gc_old)
    return m_new , c_new

def result(m ,c, x , y , cost , predictions , i):
    if i < max_iter-1:
        print("Gradient Descent has converged at the iteration {}****".format(i))
    else:
        print("Result after",max_iter," iteration is :*****")

    plt.figure(figsize=(14,7) , dpi=120)
    plt.scatter(x, y,color='red',label='data points')
    label = 'final regression line : m = {}  c = {}'.format(str(m) , str(c))
    plt.plot(x , predictions , color = 'green' , label =label)
    plt.xlabel('Flat Area')
    plt.ylabel('Sale Price')
    plt.title('Final Regression Line')
    plt.show


from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
sale_price = scaler.fit_transform(sample_data['sale_price'].values.reshape(-1,1))
flat_area = scaler.fit_transform(sample_data['flat_area'].values.reshape(-1,1))

max_iter = 1000
alpha = 0.01
cost_old = 0

m,c = param_init(sale_price)

for i in range(0 , max_iter):
    predictions = generate_prediction(m,c,flat_area)
    
    cost_new = compute_cost(predictions , sale_price)
    
    if abs(cost_new - cost_old) < 10**(-7):
        break
    
    Gm , Gc = gradient(predictions , sale_price , flat_area)
    
    m , c = param_update(m , c , Gm , Gc , alpha)
    
    
    if i%20 == 0:
        print("After iteration :",i," :m = ",m," c= ",c," Cost = ",cost_new)
    
    cost_old = cost_new
    
result (m , c , flat_area , sale_price , cost_new , predictions , i)
