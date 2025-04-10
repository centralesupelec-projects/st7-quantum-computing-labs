from sklearn import preprocessing
from sklearn.datasets import make_blobs
from sklearn.cluster import SpectralClustering
from sklearn.metrics import normalized_mutual_info_score
from similarity import similarity_matrix
import matplotlib.pyplot as plt
import numpy as np

# Step 4 - QML Clustering

NB_DATA = 100
NB_CLUSTER = 5
NB_FEATURES = 2

# Create a dataframe
def create_dataframe():
    X, y = make_blobs(n_samples=NB_DATA, centers=NB_CLUSTER, n_features=NB_FEATURES, random_state=3)
    min_max_scaler = preprocessing.MinMaxScaler()
    X = np.pi * min_max_scaler.fit_transform(X) # rescale data between between [-pi/2, pi/2]
    return X, y

def clustering(X, y, method):
    dist = similarity_matrix(2, 1, X, circ_type=method)
    adhoc_spectral = SpectralClustering(3, affinity="precomputed")
    cluster_labels = adhoc_spectral.fit_predict(dist)
    cluster_score = normalized_mutual_info_score(cluster_labels, y)
    return dist, cluster_labels, cluster_score

def display_results(X, y1, y2, y3, dist1, dist2):
    ax1 = plt.subplot(2, 3, 1)
    ax1.set_title("Initial Dataset")
    plt.scatter(X[:,0], X[:,1], c=y1)
    ax2 = plt.subplot(2, 3, 2)
    ax2.set_title("Clustered dataset with adjoint")
    plt.scatter(X[:,0], X[:,1], c=y2)
    ax3 = plt.subplot(2, 3, 3)
    ax3.set_title("Clustered dataset with swap")
    plt.scatter(X[:,0], X[:,1], c=y3)
    ax4 = plt.subplot(2, 3, 4)
    ax4.set_title("Similarity Matrix with adjoint")
    plt.imshow(dist1, interpolation="nearest", origin="upper", cmap="Blues")
    ax5 = plt.subplot(2, 3, 5)
    ax5.set_title("Similarity Matrix with swap")
    plt.imshow(dist2, interpolation="nearest", origin="upper", cmap="Blues")
    plt.show()

if __name__ == "__main__":
    print("--- Creating dataframe ---")
    X, y = create_dataframe()

    # Adjoint method
    print("--- Similarity and clustering with adjoint ---")
    dist_adjoint, cluster_labels_adjoint, cluster_score_adjoint = clustering(X, y, "adjoint")

    # Swap test method
    print("--- Similarity and clustering with swap ---")
    dist_swap, cluster_labels_swap, cluster_score_swap = clustering(X, y, "swap")

    # Make clustering and display results and precision (NMI score)
    print("--- Clustering scores ---")
    print(f"Clustering score with adjoint: {cluster_score_adjoint}")
    print(f"Clustering score with swap: {cluster_score_swap}")
    print("--- Displaying result of clustering ---")
    display_results(X, y, cluster_labels_adjoint, cluster_labels_swap, dist_adjoint, dist_swap)