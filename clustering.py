from sklearn.cluster import KMeans
from sklearn.metrics.pairwise import cosine_similarity
from scipy.spatial.distance import cdist


import pandas as pd

data_vectors = pd.read_csv('../../PycharmProjects/mutation_signatures/output/count_syntetic2.csv', index_col=0).values.T

# Obliczanie macierzy podobieństwa cosinusowego
cosine_sim_matrix = cosine_similarity(data_vectors)

# Przekształcenie podobieństwa na odległość
cosine_dist_matrix = 1 - cosine_sim_matrix

# Klastrowanie
kmeans = KMeans(n_clusters=5, random_state=0)
clusters = kmeans.fit_predict(cosine_dist_matrix)

# Wyniki
print(clusters)
