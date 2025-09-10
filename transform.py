from config import CONFIG

def generate_embeddings(array:list):
    model = CONFIG.local_embed_model()
    vectors = model.encode(array)
    return vectors


sentances = [
    "hello"
]

print(generate_embeddings(sentances).shape)

