import pandas as pd
from .doc_embeddings import compute_doc_embeddings
from Settings.settings import tokenizer



def count_tokens(text):
    return len(tokenizer.encode(text))

def create_ebd(src_filepath,dest_filepath):    
    df = pd.read_csv(src_filepath,sep='|', header=0)
    df = df.set_index(["title","header"])
    #print(df.columns)
    print(f"{len(df)} rows in the data.")
    df['tokens'] = [count_tokens(x) for x in df['content']]
    print(df.head())



    context_embeddings = compute_doc_embeddings(df)
    columns = [x for x in range(len(list(context_embeddings.values())[0]))]
    columns.insert(0,"header")
    columns.insert(0,"title")
    #columns[-1]

    context_df = pd.DataFrame(columns = columns)

    for (title,header),value in context_embeddings.items():
        new_row = [x for x in value]
        new_row.insert(0,header)
        new_row.insert(0,title)
        context_df.loc[len(context_df)] = new_row

    print(context_df.head())


    context_df.to_csv(dest_filepath,sep="\t",index = False)
    print(f"Embeddings created and stored at: \n {dest_filepath}")