import requests

url ='https://api.groq.com/openai/v1/chat/completions"'
promt=input("promt: ")
data={
    "model": "llama3-8b-8192",
    "temperature": 1,
    "max_tokens": 1024,
    "top_p": 1,
    "stream": False,
    "messages" : [ {
             "role": "user",
             "content": promt
           }
    ]
}

headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer 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"
}

response = requests.post(url,json=data,headers=headers)


print('response.txt')
