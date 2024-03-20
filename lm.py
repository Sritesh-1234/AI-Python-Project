# from openai import OpenAI
# import re
# # Point to the local server
# client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")
#
# query = 'create a python program to extract the content part alone from this sentence - ChatCompletionMessage(content="Sure, here\'s a rhyme for you:\n\nWho\'s the leader of India\'s might?\n\nModi, shining bright, day and night!", role=\'assistant\', function_call=None, tool_calls=None)'
#
# completion = client.chat.completions.create(
#   model="local-model", # this field is currently unused
#   messages=[
#     {"role": "system", "content": "Always answer in rhymes."},
#     {"role": "user", "content": "Introduce Yourself"}
#   ],
#   temperature=0.7,
# )
# sentence = completion.choices[0].message
# # print(completion.choices[0].message)
#
# content = re.search(r'content="(.*?)"', sentence).group(1)
#
# content = content.replace('\\n', '\n')
#
# print("Extracted content:")
# print(content)
#
from json import dumps

from openai import OpenAI
import re

def ask_question(Query):

  # Point to the local server
  client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

  # Define the query
  # query = 'create a python program to extract the content part alone from this sentence - ChatCompletionMessage(content="Sure, here\'s a rhyme for you:\n\nWho\'s the leader of India\'s might?\n\nModi, shining bright, day and night!", role=\'assistant\', function_call=None, tool_calls=None)'

  # Create the completion
  completion = client.chat.completions.create(
    model="local-model", # this field is currently unused
    messages=[
      {"role": "system", "content": "Always answer in rhymes."},
      {"role": "user", "content": Query}
    ],
    temperature=0.7,
  )

  # Extract the message from the completion
  sentence = str(completion.choices[0].message)
  # sentence = completion.choices[0].message.content if hasattr(completion.choices[0].message, 'content') else ''

  # print(completion.choices[0].message)
  # Use regular expression to extract the content part
  match = re.search(r'content="(.*?)"', sentence)

  # Check if the pattern was found
  if match:
      content = match.group(1)
      # Replace escaped newlines with actual newlines
      content = content.replace('\\n', '\n')
  else:
      content = 'Pattern not found.'

  # print("Extracted content:")
  return (content)
