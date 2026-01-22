from sentence_transformers import CrossEncoder
import os

def new_rerank_model_baai() -> CrossEncoder:
    # r"C:\Users\fajar\.cache\huggingface\hub\models--BAAI--bge-reranker-base\snapshots\2cfc18c9415c912f9d8155881c133215df768a70",
    model = os.getenv("MODEL_PATH")
    device = os.getenv("DEVICE")
    model = CrossEncoder(
        model,
        local_files_only=True,
        device=device,
    )
    model.predict([("warmup", "warmup")])

    return model