import requests
import json

# URL de tu servidor LLaMA 2
API_URL = 'http://localhost:11434/api/generate'

def generate_response(prompt, model_name):
    headers = {
        'Content-Type': 'application/json'
    }

    data = {
        'model': llama2,
        'prompt': prompt,
        'max_tokens': 150,  # Puedes ajustar este valor según tus necesidades
        'temperature': 0.7  # Controla la creatividad de la respuesta
    }

    response = requests.post(API_URL, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        response_json = response.json()
        return response_json.get('text', '').strip()  # Ajusta esto según la estructura de la respuesta de tu API
    else:
        return f"Error: {response.status_code}, {response.text}"

def chat():
    print("Selecciona el modelo de chatbot:")
    print("1. Modelo 1")
    print("2. Modelo 2")
    
    while True:
        try:
            model_choice = int(input("Elige el modelo (1 o 2): "))
            if model_choice == 1:
                model_name = "llama2-model-1"  # Reemplaza con el nombre real del modelo 1
            elif model_choice == 2:
                model_name = "llama2-model-2"  # Reemplaza con el nombre real del modelo 2
            else:
                raise ValueError("Modelo no válido. Elige 1 o 2.")
            break
        except ValueError:
            print("Por favor, introduce un número válido (1 o 2).")
    
    print("LLaMA 2 Chatbot: ¡Hola! ¿Cómo puedo ayudarte hoy? (Escribe 'salir' para terminar)")
    
    while True:
        user_input = input("Tú: ")
        if user_input.lower() in ['salir', 'exit', 'quit']:
            print("LLaMA 2 Chatbot: ¡Adiós!")
            break

        response = generate_response(user_input, model_name)
        print(f"LLaMA 2 Chatbot: {response}")

if __name__ == "__main__":
    chat()
