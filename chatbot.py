import openai
from Prompt_Eng.prompt_builder import construct_prompt
from Settings.api_secrets import API_KEY
import pandas as pd
from Embeddings import create_embeddings as cembd
from Embeddings.load_embeddings import load_embeddings
from Get_response.answers import answer_query_with_context
from Settings.settings import text_filepath,processedtext_filepath,embedding_filepath


def setup(create_embedding = False):
  #Settings
  openai.api_key = API_KEY
  # create_embedding = False


  #File Sources
  

  if create_embedding:
    text_df = pd.read_csv(text_filepath,sep='|', header=0)
    text_df = text_df.set_index(["title","header"])
    text_df['tokens'] = [cembd.count_tokens(x) for x in text_df['content']]
    text_df.to_csv(processedtext_filepath,sep="|")
    cembd.create_ebd(text_filepath,embedding_filepath)
  
  else:
    processed_df = pd.read_csv(processedtext_filepath,sep='|')
    processed_df = processed_df.set_index(["title","header"])
    context_embeddings = load_embeddings(embedding_filepath)

    query = input("Enter Your Question or Enter exit to exit: \n User: ")
  #print(processed_df.loc['Jeevan','About Jeevan']['content'])
    
    print("Current Topic :"+topic[1] + ". Enter Change Topic Anytime to change to change the topic ")
    messageHistory = [{'role':"system","content":prompt},{'role':'user',"content":query}]
    


    while True:
      response = openai.ChatCompletion.create(model="gpt-3.5-turbo", 
        messages=messageHistory,
        temperature = 0.2,
        max_tokens=200
        )
      reply = response["choices"][0]["message"]
      print(reply["role"] + " : " + reply["content"])
      messageHistory.append({"role":reply['role'] ,"content": reply["content"]})
      
      newQuery = input(" \nUser: ")
      
      if newQuery.lower() == "exit":
          break
      elif newQuery.lower() == "change topic":
        query = input("Enter the question about new topic: \nUser:")
        prompt,topic = construct_prompt(query,context_embeddings,processed_df)

        print("Current Topic :"+topic[1] + ". Enter Change Topic Anytime to change to change the topic ")
        messageHistory = [{'role':"system","content":prompt},{'role':'user',"content":query}]
        continue
      if len(messageHistory) > 10:
          del messageHistory[1:3]
      
      newMessage = {'role':'user','content':newQuery}
      messageHistory.append(newMessage)



def setTopic(query):
  #setOpenAPIKey()
  openai.api_key = API_KEY
  processed_df = pd.read_csv(processedtext_filepath,sep='|')
  processed_df = processed_df.set_index(["title","header"])
  context_embeddings = load_embeddings(embedding_filepath)
  prompt,topic = construct_prompt(query,context_embeddings,processed_df)
  return prompt,topic



def chat(query):
  
  openai.api_key = API_KEY
  messageHistory = query.messageHistory

  
  
 
  prompt= query.prompt
  topic = query.topic
  messageHistory.insert(0,{'role':'system',"content":prompt})
  
  
  response = openai.ChatCompletion.create(model="gpt-3.5-turbo", 
        messages=messageHistory,
        temperature = 0.2,
        max_tokens=200
        )
  reply = response["choices"][0]["message"]

  resp = {
    "prompt":prompt,
    "reply":reply,
    "topic":topic
  } 
    
  return resp


def newChat(query):
  openai.api_key = API_KEY
  messageHistory = query.messageHistory
  newMsg = messageHistory[-1]['content']
  
  prompt, topic = setTopic(newMsg)
  messageHistory.insert(0,{'role':"system","content":prompt})  #,{'role':'user',"content":newMsg}]

  response = openai.ChatCompletion.create(model="gpt-3.5-turbo", 
        messages=messageHistory,
        temperature = 0.2,
        max_tokens=200
        )
  reply = response["choices"][0]["message"]


  resp = {
    "prompt":prompt,
    "reply":reply,
    "topic":topic
  } 

    
  return resp


if __name__ == "__main__":
   setup()