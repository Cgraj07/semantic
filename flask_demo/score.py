from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
def semantic_score(text1,text2):
    text=text1+text2
    text=text.lower().split(".")
    model = SentenceTransformer('bert-base-nli-mean-tokens')
    sentence_embeddings = model.encode(text)
    cos_sim=cosine_similarity([sentence_embeddings[0]],sentence_embeddings[1:])
    semantic=cos_sim.mean()
    return semantic

