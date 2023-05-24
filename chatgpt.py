import openai
from Settings.api_secrets import API_KEY
from datetime import datetime


openai.api_key = API_KEY
current_date = datetime.now().strftime("%A, %d %B %Y, %I:%M %p")
knowledge_cutoff = "Jeevan started operations in 2000 and our growth is attributed to our eye for detail and customer centric solutions. Jeevan is headquartered in Brentwood, Tennessee, USA, Jeevan empowers its workforce to deliver solutions that exceed customer expectations. At Jeevan our business goals are strategically designed towards building value to customers through products and services. We are evolving as new technologies emerge in the market and are at par with the Industry standards."
print("Hi, This is Jeevan Chat Bot. How can I help you today?")
message = [{"role": "user", "content": f"Use the knowledge cutoff only to answer questions.if the question is not related to Jeevan Technologies reply with 'I don't know anything other than Jeevan'. Knowledge Cutoff = {knowledge_cutoff}"},    {"role":"assistant","content":"Hi, This is Jeevan Chat Bot. How can I help you today?"}]
while True:
    userMsg = input("User : ")
    
    if userMsg.lower() == "exit":
        break
    if len(message) > 10:
        del message[2:4]

    newMsg = {"role":"user","content": userMsg}
    message.append(newMsg)

    #print(message)
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", 
    messages=message,
    temperature = 0.2,
    max_tokens=200
    )

    reply = response["choices"][0]["message"]
    message.append({"role":reply['role'] ,"content": reply["content"]})
    print(reply["role"] + " : " + reply["content"])
    

print("Thanks for contacting Jeevan, Have a nice Day")