from pinecone import Pinecone, ServerlessSpec
import dotenv
from pathlib import Path
from config import Config

dotenv.load_dotenv(Path(__file__).parent / ".env")

conf = Config()

pc = Pinecone(api_key=conf.db_api_key)
