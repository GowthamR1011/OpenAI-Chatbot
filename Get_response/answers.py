
import openai
from Settings.settings import COMPLETIONS_API_PARAMS
from Prompt_Eng.prompt_builder import construct_prompt

def answer_query_with_context(query,df,document_embeddings,show_prompt= False) :
  prompt = construct_prompt(query,document_embeddings,df)
  
  if show_prompt:
      print(prompt)

  response = openai.Completion.create(prompt=prompt,
  temperature=COMPLETIONS_API_PARAMS["temperature"],
  max_tokens=COMPLETIONS_API_PARAMS["max_tokens"],
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0,
  model=COMPLETIONS_API_PARAMS["model"]
          )

  return response["choices"][0]["text"].strip(" \n")