import pandas as pd
import matplotlib.pylab as plt 
Univ = pd.read_csv("E:\\Bokey\\Excelr Data\\Python Codes\\all_py\\Clustering\\Universities.csv")

def norm_func(i):
    x = (i-i.mean())/(i.std())
    return (x)

df_norm = norm_func(Univ.iloc[:,1:])

from scipy.cluster.hierarchy import linkage 

import scipy.cluster.hierarchy as sch 

type(df_norm)

help(linkage)
z = linkage(df_norm, method="complete",metric="euclidean")

plt.figure(figsize=(15, 5));plt.title('Hierarchical Clustering Dendrogram');plt.xlabel('Index');plt.ylabel('Distance')
sch.dendrogram(
    z,
    leaf_rotation=0., 
    leaf_font_size=8.,
)
plt.show()

help(linkage)

from	sklearn.cluster	import	AgglomerativeClustering 
h_complete	=	AgglomerativeClustering(n_clusters=3,	linkage='complete',affinity = "euclidean").fit(df_norm) 


cluster_labels=pd.Series(h_complete.labels_)

Univ['clust']=cluster_labels 
Univ = Univ.iloc[:,[7,0,1,2,3,4,5,6]]
Univ.head()

Univ.iloc[:,2:].groupby(Univ.clust).median()

Univ.to_csv("University.csv",encoding="utf-8")
