import os
import openai

openai.api_key = os.getenv("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")

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="Convert movie titles into emoji.\n\nBack to the Future: 👨👴🚗🕒 \nBatman: 🤵🦇 \nTransformers: 🚗🤖 \nStar Wars:",
  temperature=0.8,
  max_tokens=60,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0,
  stop=["\n"]
)
