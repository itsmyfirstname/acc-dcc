import os
from sentence_transformers import SentenceTransformer


class Config:
    @property
    def db_api_key(self) -> str:
        return os.environ["PINECONE_API_KEY"]

    @property
    def index_name(self) -> str:
        return os.getenv("VECTOR_DB_INDEX") or "acc-dcc"
    @property
    def embedding_model_name(self) -> str:
        return "all-mpnet-base-v2"

    def local_embed_model(self, model_name: str | None = None):
        model = model_name or self.embedding_model_name
        return SentenceTransformer(model)

CONFIG = Config()
