from sklearn.datasets import make_blobs
from sklearn import preprocessing
from sklearn.cluster import SpectralClustering
from sklearn.metrics import normalized_mutual_info_score
from similarity import sim, pm, similarity_adjoint, similarity_swap
import matplotlib.pyplot as plt
import numpy as np

NB_DATA = 100
NB_CLUSTER = 3

## Create a dataframe
X, y = make_blobs(n_samples=NB_DATA, centers=NB_CLUSTER, n_features=2, random_state=3)
min_max_scaler = preprocessing.MinMaxScaler()
X = np.pi * min_max_scaler.fit_transform(X) # rescale data between between [-pi/2, pi/2]
plt.scatter(X[:,0], X[:,1], c=y)

## Compute distances with quantum kernel

dist = similarity_adjoint(2, 1, X, sim, pm)
plt.imshow(dist, interpolation="nearest", origin="upper", cmap="Blues")

# dist2 = similarity_swap(2, 1, X, sim, pm)
# plt.imshow(dist2, interpolation="nearest", origin="upper", cmap="Blues")

## Make clustering and display results and precision (NMI score)

adhoc_spectral = SpectralClustering(3, affinity="precomputed")
cluster_labels = adhoc_spectral.fit_predict(dist)
cluster_score = normalized_mutual_info_score(cluster_labels, y)
print(f"Clustering score: {cluster_score}")
plt.scatter(X[:,0], X[:,1], c=cluster_labels)