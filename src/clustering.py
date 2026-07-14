from sklearn.cluster import KMeans


def train_kmeans(df_scaled, n_clusters=6):

    # ---------------------------------
    # Initialize KMeans
    # ---------------------------------
    kmeans_model = KMeans(
        n_clusters=n_clusters,
        random_state=42,
        n_init=10
    )

    # ---------------------------------
    # Train model and assign clusters
    # ---------------------------------
    cluster_labels = kmeans_model.fit_predict(df_scaled)

    return kmeans_model, cluster_labels


def predict_cluster(df_scaled, kmeans_model):

    cluster_prediction = kmeans_model.predict(df_scaled)

    return cluster_prediction