import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
cars = pd.read_csv("E:\\Bokey\\Excelr Data\\Python Codes\\all_py\\Multilinear Regression\\cars.csv")
cars.head(40) 
cars.corr()

import seaborn as sns
sns.pairplot(cars)
cars.columns

import statsmodels.formula.api as smf         
ml1 = smf.ols('MPG~WT+VOL+SP+HP',data=cars).fit()
ml1.params
ml1.summary()
ml_v=smf.ols('MPG~VOL',data = cars).fit()  
ml_v.summary() 
ml_w=smf.ols('MPG~WT',data = cars).fit()  
ml_w.summary()
ml_wv=smf.ols('MPG~WT+VOL',data = cars).fit()  
ml_wv.summary() 

import statsmodels.api as sm
sm.graphics.influence_plot(ml1)
cars_new=cars.drop(cars.index[[76,70]],axis=0)
ml_new = smf.ols('MPG~WT+VOL+HP+SP',data = cars_new).fit()    
ml_new.params
ml_new.summary() 
print(ml_new.conf_int(0.01))

mpg_pred = ml_new.predict(cars_new[['WT','VOL','HP','SP']])
mpg_pred
cars_new.head()
rsq_hp = smf.ols('HP~WT+VOL+SP',data=cars_new).fit().rsquared  
vif_hp = 1/(1-rsq_hp) 

rsq_wt = smf.ols('WT~HP+VOL+SP',data=cars_new).fit().rsquared  
vif_wt = 1/(1-rsq_wt) 

rsq_vol = smf.ols('VOL~WT+SP+HP',data=cars_new).fit().rsquared  
vif_vol = 1/(1-rsq_vol) 

rsq_sp = smf.ols('SP~WT+VOL+HP',data=cars_new).fit().rsquared  
vif_sp = 1/(1-rsq_sp)

d1 = {'Variables':['Hp','WT','VOL','SP'],'VIF':[vif_hp,vif_wt,vif_vol,vif_sp]}
Vif_frame = pd.DataFrame(d1)  
Vif_frame

sm.graphics.plot_partregress_grid(ml_new)

final_ml= smf.ols('MPG~VOL+SP+HP',data = cars_new).fit()
final_ml.params
final_ml.summary()
mpg_pred = final_ml.predict(cars_new)

import statsmodels.api as sm
sm.graphics.plot_partregress_grid(final_ml)
plt.scatter(cars_new.MPG,mpg_pred,c="r");plt.xlabel("observed_values");plt.ylabel("fitted_values")
plt.scatter(mpg_pred,final_ml.resid_pearson,c="r"),plt.axhline(y=0,color='blue');plt.xlabel("fitted_values");plt.ylabel("residuals")
plt.hist(final_ml.resid_pearson) 

import pylab          
import scipy.stats as st
st.probplot(final_ml.resid_pearson, dist="norm", plot=pylab)

plt.scatter(mpg_pred,final_ml.resid_pearson,c="r"),plt.axhline(y=0,color='blue');plt.xlabel("fitted_values");plt.ylabel("residuals")

from sklearn.model_selection import train_test_split
cars_train,cars_test  = train_test_split(cars_new,test_size = 0.2) 

model_train = smf.ols("MPG~HP+SP+VOL",data=cars_train).fit()

train_pred = model_train.predict(cars_train)

train_resid  = train_pred - cars_train.MPG

train_rmse = np.sqrt(np.mean(train_resid*train_resid))

test_pred = model_train.predict(cars_test)

test_resid  = test_pred - cars_test.MPG

test_rmse = np.sqrt(np.mean(test_resid*test_resid))
