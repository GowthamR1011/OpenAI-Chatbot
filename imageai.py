import openai
from Settings.api_secrets import API_KEY

openai.api_key = API_KEY

response = openai.Image.create(
  prompt="a white siamese cat",
  n=1,
  size="1024x1024"
)
image_url = response['data'][0]['url']
print(image_url)