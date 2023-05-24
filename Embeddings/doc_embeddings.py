import openai
import pandas as pd
from Settings.settings import DOC_EMBEDDINGS_MODEL,QUERY_EMBEDDINGS_MODEL




# Document Embedding Functions


def get_embedding(text: str, model: str) :
    result = openai.Embedding.create(
      model=model,
      input=text
    )
    return result["data"][0]["embedding"]

def get_doc_embedding(text: str) :
    return get_embedding(text, DOC_EMBEDDINGS_MODEL)

def get_query_embedding(text: str) :
    return get_embedding(text, QUERY_EMBEDDINGS_MODEL)

def compute_doc_embeddings(df: pd.DataFrame) :
   
    return {
        idx: get_doc_embedding(r.content.replace("\n", " ")) for idx, r in df.iterrows()
    }
#token counter
