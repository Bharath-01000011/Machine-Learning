import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.holtwinters import SimpleExpSmoothing 
from statsmodels.tsa.holtwinters import Holt 
from statsmodels.tsa.holtwinters import ExponentialSmoothing 
import statsmodels.graphics.tsaplots as tsa_plots
import statsmodels.tsa.statespace as tm_models
from datetime import datetime,time

Amtrak = pd.read_csv("E:\\Bokey\\Excelr Data\\Python_Classes\\Forecasting_Python\\Amtrak.csv")

Amtrak.rename(columns={"Ridership ('000)":"Ridership"},inplace=True)   

Amtrak.index = pd.to_datetime(Amtrak.Month,format="%b-%y")

Amtrak.Ridership.plot() 

Amtrak["Date"] = pd.to_datetime(Amtrak.Month,format="%b-%y")


Amtrak["month"] = Amtrak.Date.dt.strftime("%b") 
Amtrak["year"] = Amtrak.Date.dt.strftime("%Y")

heatmap_y_month = pd.pivot_table(data=Amtrak,values="Ridership",index="year",columns="month",aggfunc="mean",fill_value=0)
sns.heatmap(heatmap_y_month,annot=True,fmt="g")

sns.boxplot(x="month",y="Ridership",data=Amtrak)
sns.boxplot(x="year",y="Ridership",data=Amtrak)

sns.lineplot(x="year",y="Ridership",hue="month",data=Amtrak)

Amtrak.Ridership.plot(label="org")
for i in range(2,24,6):
    Amtrak["Ridership"].rolling(i).mean().plot(label=str(i))
plt.legend(loc=3)
    
decompose_ts_add = seasonal_decompose(Amtrak.Ridership,model="additive")
decompose_ts_add.plot()
decompose_ts_mul = seasonal_decompose(Amtrak.Ridership,model="multiplicative")
decompose_ts_mul.plot()

tsa_plots.plot_acf(Amtrak.Ridership,lags=10)
tsa_plots.plot_pacf(Amtrak.Ridership)

Train = Amtrak.head(133)
Test = Amtrak.tail(12)

def MAPE(pred,org):
    temp = np.abs((pred-org))*100/org
    return np.mean(temp)

ses_model = SimpleExpSmoothing(Train["Ridership"]).fit()
pred_ses = ses_model.predict(start = Test.index[0],end = Test.index[-1])
MAPE(pred_ses,Test.Ridership) 

hw_model = Holt(Train["Ridership"]).fit()
pred_hw = hw_model.predict(start = Test.index[0],end = Test.index[-1])
MAPE(pred_hw,Test.Ridership) 

hwe_model_add_add = ExponentialSmoothing(Train["Ridership"],seasonal="add",trend="add",seasonal_periods=12,damped=True).fit()
pred_hwe_add_add = hwe_model_add_add.predict(start = Test.index[0],end = Test.index[-1])
MAPE(pred_hwe_add_add,Test.Ridership) 

hwe_model_mul_add = ExponentialSmoothing(Train["Ridership"],seasonal="mul",trend="add",seasonal_periods=12).fit()
pred_hwe_mul_add = hwe_model_mul_add.predict(start = Test.index[0],end = Test.index[-1])
MAPE(pred_hwe_mul_add,Test.Ridership) 

from pyramid.arima import auto_arima
auto_arima_model = auto_arima(Train["Ridership"],start_p=0,
                              start_q=0,max_p=10,max_q=10,
                              m=12,start_P=0,seasonal=True,
                              d=1,D=1,trace=True,error_action="ignore",
                              suppress_warnings= True,
                              stepwise=False)
                
            
auto_arima_model.summary()
auto_arima_model.predict_in_sample( )

pred_test = pd.Series(auto_arima_model.predict(n_periods=12))

pred_test.index = Test.index
MAPE(pred_test,Test.Ridership) 


combinations_l = list(product(range(1,7),range(2),range(1,7)))
combinations_u = list(product(range(1,7),range(2),range(1,7)))
m =12 

results_sarima = []
best_aic = float("inf")

for i in combinations_l:
    for j in combinations_u:
        try:
            model_sarima = sm.tsa.statespace.SARIMAX(Train["Ridership"],
                                                     order = i,seasonal_order = j+(m,)).fit(disp=-1)
        except:
            continue
        aic = model_sarima.aic
        if aic < best_aic:
            best_model = model_sarima
            best_aic = aic
            best_l = i
            best_u = j
        results_sarima.append([i,j,model_sarima.aic])


result_sarima_table = pd.DataFrame(results_sarima)
result_sarima_table.columns = ["paramaters_l","parameters_j","aic"]
result_sarima_table = result_sarima_table.sort_values(by="aic",ascending=True).reset_index(drop=True)

best_fit_model = sm.tsa.statespace.SARIMAX(Train["Ridership"],
                                                     order = (1,1,1),seasonal_order = (1,1,1,12)).fit(disp=-1)
best_fit_model.summary()
best_fit_model.aic 
srma_pred = best_fit_model.predict(start = Test.index[0],end = Test.index[-1])
Amtrak["srma_pred"] = srma_pred

plt.plot(Train.index, Train["Ridership"], label='Train',color="black")
plt.plot(Test.index, Test["Ridership"], label='Test',color="blue")
plt.plot(pred_ses.index, pred_ses, label='SimpleExponential',color="green")
plt.plot(pred_hw.index, pred_hw, label='Holts_winter',color="red")
plt.plot(pred_hwe_add_add.index,pred_hwe_add_add,label="HoltsWinterExponential_1",color="brown")
plt.plot(pred_hwe_mul_add.index,pred_hwe_mul_add,label="HoltsWinterExponential_2",color="yellow")
plt.plot(pred_hwe_mul_add.index,pred_hwe_mul_add,label="Auto_Arima",color="grey")
plt.plot(pred_hwe_mul_add.index,srma_pred,label="Auto_Sarima",color="purple")
plt.legend(loc='best')

model_mapes = pd.DataFrame(columns=["model_name","mape"])
model_mapes["model_name"] = ["]