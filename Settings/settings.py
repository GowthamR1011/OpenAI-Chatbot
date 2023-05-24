from transformers import GPT2TokenizerFast



COMPLETIONS_MODEL = "text-davinci-002"
MODEL_NAME = "curie"
tokenizer = GPT2TokenizerFast.from_pretrained("gpt2")
DOC_EMBEDDINGS_MODEL = f"text-search-{MODEL_NAME}-doc-001"
QUERY_EMBEDDINGS_MODEL = f"text-search-{MODEL_NAME}-query-001"

MAX_SECTION_LEN = 300  # filter out context based on the length
SEPARATOR = "\n* "
separator_len = len(tokenizer.tokenize(SEPARATOR))


COMPLETIONS_API_PARAMS = {
  "temperature": 0.0,
  "max_tokens": 300,
  "model": COMPLETIONS_MODEL    
}

header = """Answer the question as truthfully as possible, and if you're unsure of the answer, say "Sorry, I don't know".""" 

text_filepath = r"C:\Users\jt1444\Desktop\OpenAI Chatbot\Text_data\Test3.psv"
processedtext_filepath = r"C:\Users\jt1444\Desktop\OpenAI Chatbot\Text_data\processedtext.psv"
embedding_filepath = r"C:\Users\jt1444\Desktop\OpenAI Chatbot\Text_data\Embeddings.tsv"