import pandas as pd 
import numpy as np
uni = pd.read_csv("E:\\Bokey\\Excelr Data\\Python Codes\\all_py\\Clustering\\Universities.csv")
uni.describe()
uni.head()
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from sklearn.preprocessing import scale 
uni.data = uni.ix[:,1:]
uni.data.head(4)
uni_normal = scale(uni.data)
pca = PCA(n_components = 6)
pca_values = pca.fit_transform(uni_normal)
var = pca.explained_variance_ratio_
var
pca.components_[0]
var1 = np.cumsum(np.round(var,decimals = 4)*100)
var1

plt.plot(var1,color="red")

x = pca_values[:,0]
y = pca_values[:,1]
z = pca_values[:2:3]
plt.scatter(x,y,color=["red","blue"])

from mpl_toolkits.mplot3d import Axes3D
Axes3D.scatter(np.array(x),np.array(y),np.array(z),c=["green","blue","red"])
new_df = pd.DataFrame(pca_values[:,0:4])
from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters = 3)
kmeans.fit(new_df)
kmeans.labels_
