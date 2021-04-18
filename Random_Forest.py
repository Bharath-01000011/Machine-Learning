import pandas as pd
import numpy as np
Diabetes = pd.read_csv("C:\\Users\\Bharath\\Desktop\\Code\\Diabetes_RF.csv")
Diabetes.head()
Diabetes.columns
colnames = list(Diabetes.columns)
predictors = colnames[:8]
predictors
target = colnames[8]
target
X = Diabetes[predictors]
Y = Diabetes[target]    

from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier(n_jobs=3,oob_score=True,n_estimators=15,criterion="entropy")
np.shape(Diabetes) 
rf.fit(X,Y)
rf.estimators_ 
rf.classes_
rf.n_classes_
rf.n_features_
rf.n_outputs_
rf.oob_score_ 
rf.predict(X)

Diabetes['rf_pred'] = rf.predict(X)
cols = ['rf_pred',' Class variable']
Diabetes[cols].head()
Diabetes[" Class variable"]

from sklearn.metrics import confusion_matrix
confusion_matrix(Diabetes[' Class variable'],Diabetes['rf_pred'])
pd.crosstab(Diabetes[' Class variable'],Diabetes['rf_pred'])
print("Accuracy",(497+268)/(497+268+0+3)*100)
Diabetes["rf_pred"]
iris = pd.read_csv("E:\\Bokey\\Excelr Data\\Python Codes\\all_py\\KNN\\iris.csv")
iX=iris[["Sepal.Length","Sepal.Width","Petal.Length","Petal.Width"]]
iy=iris[["Species"]]

from sklearn.ensemble import RandomForestClassifier
rfiris = RandomForestClassifier(n_jobs=4,oob_score=True,n_estimators=100,criterion="entropy")
rfiris.fit(iX,iy)
iris["rf_pred"] = rfiris.predict(iX)

from sklearn.metrics import confusion_matrix
confusion_matrix(iris["Species"],iris["rf_pred"])
salary_train = pd.read_csv("D:\\ML\\Python\\Python-ML\\Random Forests\\SalaryData_Train.csv")
salary_test = pd.read_csv("D:\\ML\\Python\\Python-ML\\Random Forests\\SalaryData_Test.csv")
colnames = salary_train.columns
len(colnames[0:13])
trainX = salary_train[colnames[0:13]]
trainY = salary_train[colnames[13]]
rfsalary = RandomForestClassifier(n_jobs=2,oob_score=True,n_estimators=15,criterion="entropy")
rfsalary.fit(trainX,trainY) 
string_columns=["workclass","education","maritalstatus","occupation","relationship","race","sex","native"]
from sklearn import preprocessing
for i in string_columns:
    number = preprocessing.LabelEncoder()
    trainX[i] = number.fit_transform(trainX[i])

rfsalary.fit(trainX,trainY)
trainX["rf_pred"] = rfsalary.predict(trainX)
confusion_matrix(trainY,trainX["rf_pred"])
print ("Accuracy",(22321+6954)/(22321+332+554+6954))

testX = salary_test[colnames[0:13]]
testY = salary_test[colnames[13]]

for i in string_columns:
    number = preprocessing.LabelEncoder()
    testX[i] = number.fit_transform(testX[i])
testX["rf_pred"] = rfsalary.predict(testX)
confusion_matrix(testY,testX["rf_pred"])
print ("Accuracy",(10359+2283)/(10359+1001+1417+2283))







