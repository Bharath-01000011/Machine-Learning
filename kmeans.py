import pandas as pd
import matplotlib.pylab as plt
from sklearn.cluster	import	KMeans
from scipy.spatial.distance import cdist 
import numpy as np

X = np.random.uniform(0,1,1000)
Y = np.random.uniform(0,1,1000)
df_xy =pd.DataFrame(columns=["X","Y"])
df_xy.X = X
df_xy.Y = Y
df_xy.plot(x="X",y = "Y",kind="scatter")
model1 = KMeans(n_clusters=5).fit(df_xy)
model1.labels_
model1.cluster_centers_
df_xy.plot(x="X",y = "Y",c=model1.labels_,kind="scatter",s=10,cmap=plt.cm.coolwarm)

Univ = pd.read_csv("E:\\Bokey\\Excelr Data\\Python Codes\\all_py\\Clustering\\Universities.csv")
def norm_func(i):
    x = (i-i.min())	/	(i.max()	-	i.min())
    return (x)

df_norm = norm_func(Univ.iloc[:,1:])


df_norm.head(10) 

k = list(range(2,15))
k
TWSS = [] 
for i in k:
    kmeans = KMeans(n_clusters = i)
    kmeans.fit(df_norm)
    WSS = [] 
    for j in range(i):
        WSS.append(sum(cdist(df_norm.iloc[kmeans.labels_==j,:],kmeans.cluster_centers_[j].reshape(1,df_norm.shape[1]),"euclidean")))
    TWSS.append(sum(WSS))

plt.plot(k,TWSS, 'ro-');plt.xlabel("No_of_Clusters");plt.ylabel("total_within_SS");plt.xticks(k)

model=KMeans(n_clusters=5) 
model.fit(df_norm)

model.labels_ 
md=pd.Series(model.labels_) 
Univ['clust']=md
df_norm.head()

Univ = Univ.iloc[:,[7,0,1,2,3,4,5,6]]

Univ.iloc[:,1:7].groupby(Univ.clust).mean()

Univ.to_csv("Univsersity.csv")
