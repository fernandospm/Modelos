import requests

while True:
    pregunta = input("PROMPt:")
    data = {
        "model": "llama3",
        "prompt": pregunta,
        "system":"Responde como Goku ssj2",
        "stream":False 
    }

requests=requests.post('http://localhost:11434/api/generate', json=data)

response= json.loads(response.text)
print(response['response'])
