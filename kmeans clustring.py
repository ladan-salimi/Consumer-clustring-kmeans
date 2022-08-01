import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans

df = pd.read_excel (r'C:\Users\ladan\Desktop\clustring\input2018.xlsx')
#Selecting the feature: consumption value and country
x = df.iloc[:,1:2]
#Apply K-means Clustering
kmeans = KMeans(2)
kmeans.fit(x)
#Clustering Results:prediction of clusters for each country
identified_clusters = kmeans.fit_predict(x)
#creates a copy of an existing list
data_with_clusters = df.copy()
#adding "Clusters" columns to the end of original dataset to put the number of clusters related to each country on it
data_with_clusters['Clusters'] = identified_clusters
plt.scatter(data_with_clusters['country'],data_with_clusters['value'],c=data_with_clusters['Clusters'],cmap='rainbow')
