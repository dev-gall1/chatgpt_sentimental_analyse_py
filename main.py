#Library
import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")
text = """Content"""

response = openai.Completion.create(
  model="text-davinci-003",
  prompt=text,
  temperature=0,
  max_tokens=60,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0
)