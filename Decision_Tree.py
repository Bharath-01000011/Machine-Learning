import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("C:\\Users\\Bharath\\Desktop\\Code\\iris.csv")
data.head()
data['Species'].unique()
data.Species.value_counts()
colnames = list(data.columns)
predictors = colnames[:4]
target = colnames[4]

import numpy as np

data['is_train'] = np.random.uniform(0, 1, len(data))<= 0.75
data['is_train']
train,test = data[data['is_train'] == True],data[data['is_train']==False]

from sklearn.model_selection import train_test_split
train,test = train_test_split(data,test_size = 0.2)

from sklearn.tree import  DecisionTreeClassifier
help(DecisionTreeClassifier)

model = DecisionTreeClassifier(criterion = 'entropy')
model.fit(train[predictors],train[target])

preds = model.predict(test[predictors])
pd.Series(preds).value_counts()
pd.crosstab(test[target],preds)

np.mean(train.Species == model.predict(train[predictors]))

np.mean(preds==test.Species) 

train_emails_matrix
email_train.type
test_emails_matrix
email_test.type


model.fit(train_emails_matrix,email_train.type)

preds = model.predict(test_emails_matrix)
pd.Series(preds).value_counts()
pd.crosstab(test[target],preds)

np.mean(email_train.type == model.predict(train_emails_matrix))

np.mean(preds==email_test.type)
