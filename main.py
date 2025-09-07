from pinecone import Pinecone
import dotenv
from pathlib import Path
from config import Config
import os
from pypdf import PdfReader
import uuid

dotenv.load_dotenv(Path(__file__).parent / ".env")

conf = Config()

pc = Pinecone(api_key=conf.db_api_key)
pdf_dir = Path(__file__).parent / "pdf"
pdf_files = [pdf_dir / f for f in os.listdir(pdf_dir) if f.endswith(".pdf")]
all_records = []


if not pc.has_index(conf.index_name):
    pc.create_index_for_model(
        name=conf.index_name,
        cloud="aws",
        region="us-east-1",
        embed={"model": "llama-text-embed-v2", "field_map": {"text": "chunk_text"}},
    )


def extract_text_from_pdf(pdf_path):
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text


def chunk_text(text, chunk_size=1000, overlap=200):
    chunks = []
    start = 0
    while start < len(text):
        end = min(start + chunk_size, len(text))
        chunks.append(text[start:end])
        start += chunk_size - overlap
    return chunks


for pdf_file in pdf_files:
    text = extract_text_from_pdf(pdf_file)
    chunks = chunk_text(text)
    for i, chunk in enumerate(chunks):
        record = {"_id": str(uuid.uuid4()), "chunk_text": chunk}
        all_records.append(record)

# Upsert to Pinecone
index = pc.Index(conf.index_name)
index.upsert_records("inital-studies", all_records)
