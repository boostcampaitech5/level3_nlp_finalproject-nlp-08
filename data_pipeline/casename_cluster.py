import os
import pickle

import matplotlib.pyplot as plt
import pandas as pd
from konlpy.tag import Kkma
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import pairwise_distances, silhouette_score


def save_data(data, file="tokenized_documents.pkl"):
    with open(os.path.join("./artifact", file), "wb") as f:
        pickle.dump(data, f)

def load_data(file="tokenized_documents.pkl"):
    with open(os.path.join("./artifact", file), "rb") as f:
        loaded_file = pickle.load(f)
    return loaded_file

def tokenize_documents(data):
    kkma = Kkma()
    tokenized_documents = [kkma.sentences(document) for document in data]
    return tokenized_documents

def get_sparse_embeddings(data):
    vectorizer = CountVectorizer()
    sparse_embeddings = vectorizer.fit_transform(data)
    return vectorizer, sparse_embeddings

def get_raw_data(data):
    raw_data = pd.read_csv(data)
    documents = raw_data.apply(lambda x: x["question"] + x["answer"], axis=1).tolist()
    return documents

def evaluate_clustering_results(cluster_assignments, embeddings, metric):
    silhouette_avg = silhouette_score(embeddings, cluster_assignments, metric=metric)
    print(f"Silhouette Score: {silhouette_avg}")

def get_cluster_indices(cluster_assignments, cluster_label):
    indices = [index for index, cluster in enumerate(cluster_assignments) if cluster == cluster_label]
    return indices

def predict_cluster(new_document, vectorizer, kmeans_model):
    new_embedding = vectorizer.transform([new_document])
    new_embedding = new_embedding[:, :kmeans_model.cluster_centers_.shape[1]]
    distance_to_centers = pairwise_distances(new_embedding, kmeans_model.cluster_centers_)
    predicted_cluster = distance_to_centers.argmin()
    distance_to_center = distance_to_centers.min()
    return predicted_cluster, distance_to_center

def find_optimal_k(distances):
    distortions = []
    k_values = range(2, 11)
    for k in k_values:
        kmeans = KMeans(n_clusters=k, random_state=42).fit(distances)
        distortions.append(kmeans.inertia_)
    
    plt.plot(k_values, distortions, marker='o')
    plt.xlabel('Number of Clusters (k)')
    plt.ylabel('Distortion')
    plt.title('Elbow Method')
    plt.show()

def plot_cluster_distribution(embeddings, cluster_assignments, k):
    plt.figure(figsize=(8, 6))
    colors = plt.cm.get_cmap('tab10', k)

    for cluster_label in range(k):
        indices = get_cluster_indices(cluster_assignments, cluster_label)
        cluster_embeddings = embeddings[indices]
        plt.scatter(cluster_embeddings[:, 0], cluster_embeddings[:, 1], color=colors(cluster_label),
                    label=f"Cluster {cluster_label}")

    plt.xlabel("Dimension 1")
    plt.ylabel("Dimension 2")
    plt.title("Data Point Distribution")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    # tokenized_documents = load_data("tokenized_documents.pkl")
    tokenized_documents = get_raw_data("./data/easy_law.csv")
    vectorizer, sparse_embeddings = get_sparse_embeddings(tokenized_documents)

    distances_cosine = pairwise_distances(sparse_embeddings, metric="cosine")
    distances_euclidean = pairwise_distances(sparse_embeddings, metric="euclidean")


    k = 10
    kmeans_cosine = KMeans(n_clusters=k, random_state=42).fit(distances_cosine)
    kmeans_euclidean = KMeans(n_clusters=k, random_state=42).fit(distances_euclidean)

    cluster_assignments_cosine = kmeans_cosine.labels_
    cluster_assignments_euclidean = kmeans_euclidean.labels_

    cluster_indices = {}
    for cluster_label in range(k):
        indices = get_cluster_indices(cluster_assignments_cosine, cluster_label)
        cluster_indices[cluster_label] = indices
        print(f"Cluster {cluster_label}: {len(indices)} data points")

    query_document = "성폭력으로 고소당했는데 어떻게 처벌받을까요?"

    pca = PCA(n_components=5)
    embeddings_pca = pca.fit_transform(sparse_embeddings.toarray())

    predicted_cluster, distance_to_center = predict_cluster(query_document, vectorizer, kmeans_cosine)
    print(f"Predicted cluster for the query document: {predicted_cluster, distance_to_center}")

    plot_cluster_distribution(embeddings_pca, cluster_assignments_cosine, k)