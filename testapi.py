import requests

payload = {'queryId':"abc","messageHistory":[{"role":"user","content":"Where is jeevan located?"}]}
resp = requests.post(url="http://127.0.0.1:8000/chat",json=payload)
print(resp)