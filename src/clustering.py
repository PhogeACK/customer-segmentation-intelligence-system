from sklearn.cluster import KMeans


# ---------------------------------
# Train KMeans model
# ---------------------------------
def train_kmeans(df_scaled, n_clusters=6):

    kmeans_model = KMeans(
        n_clusters=n_clusters,
        random_state=42,
        n_init=10
    )

    kmeans_model.fit(df_scaled)

    return kmeans_model


# ---------------------------------
# Predict customer cluster
# ---------------------------------
def predict_cluster(df_scaled, kmeans_model):

    cluster_prediction = kmeans_model.predict(df_scaled)

    return cluster_prediction