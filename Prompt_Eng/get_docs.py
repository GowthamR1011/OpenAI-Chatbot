from Embeddings import doc_embeddings as ebd
import numpy as np

def vector_similarity(x, y):
  return np.dot(np.array(x), np.array(y))

def order_document_sections_by_query_similarity(query: str, contexts) :
  query_embedding = ebd.get_query_embedding(query)
  
  document_similarities = sorted([
      (vector_similarity(query_embedding, doc_embedding), doc_index) for doc_index, doc_embedding in contexts.items()
  ], reverse=True)
  
  return document_similarities
