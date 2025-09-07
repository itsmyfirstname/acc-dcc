import os


class Config:
    @property
    def db_api_key(self) -> str:
        return os.environ["PINECONE_API_KEY"]

    @property
    def index_name(self) -> str:
        return os.getenv("VECTOR_DB_INDEX") or "acc-dcc"
