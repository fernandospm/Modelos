import request
import json
url ='https://api.groq.com/openai/v1/chat/completions"'

data={
    "model": "llama3-8b-8192",
    "temperature": 1,
    "max_tokens": 1024,
    "top_p": 1,
    "stream": true,
    "stop": null
}

headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer ${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}"
}


response =requuest.post(url,json=data,headers=headers)

print(response.text)