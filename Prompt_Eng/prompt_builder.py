import pandas as pd
from .get_docs import order_document_sections_by_query_similarity
from Settings.settings import SEPARATOR,separator_len,MAX_SECTION_LEN


def construct_prompt(question: str, context_embeddings: dict, df: pd.DataFrame) -> str:
  # used to get the relevant context based on the question
  most_relevant_document_sections = order_document_sections_by_query_similarity(question, context_embeddings)
  
  chosen_sections = []
  chosen_sections_len = 0
  chosen_sections_indexes = []
  topic = most_relevant_document_sections[0][1]
  for _, section_index in most_relevant_document_sections:
      #print(section_index)
      document_section = df.loc[section_index]
      
      chosen_sections_len += document_section.tokens + separator_len
      if chosen_sections_len > MAX_SECTION_LEN:
          break
          
      chosen_sections.append(SEPARATOR + document_section.content.replace("\n", " "))
      chosen_sections_indexes.append(str(section_index))
          

  #print(f"Selected {len(chosen_sections)} document sections:")
  #print("\n".join(chosen_sections_indexes))
  
  header = """You are a Chatbot for Jeevan Technologies.Answer the question as truthfully as possible using the provided context, and if the answer is not contained within the text below, say "I don't know."\n\nContext:\n"""
  
  return header + "".join(chosen_sections),topic # + "\n\n Q: " + question + "\n A:"
