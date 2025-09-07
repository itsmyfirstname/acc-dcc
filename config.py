import os

class Config:
    @property
    def db_api_key(self) -> str:
        return os.environ["PINECONE_API_KEY"]