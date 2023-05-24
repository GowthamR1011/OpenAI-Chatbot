import pandas as pd

def load_embeddings(fname,seperator='\t'):
    
  df = pd.read_csv(fname,sep=seperator, header=0)
  max_dim = max([int(c) for c in df.columns if c != "title" and c != "header"])
  return {
          (r.title, r.header): [r[str(i)] for i in range(max_dim + 1)] for _, r in df.iterrows()
  }