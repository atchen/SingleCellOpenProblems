from .....tools.decorators import metric


@metric(
    metric_name="Batch ASW",
    maximize=True,
    image="openproblems-python-batch-integration",  # only if required
)
def silhouette_batch(adata):
    from scIB.metrics import silhouette_batch

    _, sil = silhouette_batch(
        adata, batch_key="batch", group_key="labels", embed="X_emb"
    )
    return sil["silhouette_score"].mean()
