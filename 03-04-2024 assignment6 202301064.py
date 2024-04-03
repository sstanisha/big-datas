import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


data = pd.read_csv('data.csv')  

plt.scatter(data['Experience'], data['Rank'], s=50, alpha=0.5)
plt.title('K means cluster')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()


k = 2  # Number of clusters
kmeans = KMeans(n_clusters=k)
kmeans.fit(data)

centers = kmeans.cluster_centers_
labels = kmeans.labels_

plt.scatter(data['X'], data['Y'], c=labels, s=50, cmap='viridis', alpha=0.5)
plt.scatter(centers[:, 0], centers[:, 1], c='pink', s=200, alpha=0.8)
plt.title('Clustered Data')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()

