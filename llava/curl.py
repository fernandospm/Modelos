import base64
import requests
import json

def image_to_base64(image_path):
    try:
        with open(image_path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read())
            return encoded_string.decode('utf-8')
    except FileNotFoundError:
        print("La ruta de la imagen no es válida. Por favor, introduce una ruta correcta.")
        return None

# Solicitar la ruta de la imagen al usuario
ruta_imagen = input("Ruta de la imagen: ")

# Convertir la imagen a base64
base64_image = image_to_base64(ruta_imagen)
if not base64_image:
    exit()  # Si la ruta de la imagen no es válida, salir del programa

# Solicitar el prompt al usuario
prompt_usuario = input("Prompt: ")

# Datos para la solicitud a la API
data = {
    "model": "llava",
    "prompt": prompt_usuario,
    "system": "Responde como si fueras un profesional de artes",
    "stream": False,
    "images": [base64_image]  
}

# Realizar solicitud a la API local
response = requests.post('http://localhost:11434/api/generate', json=data)

# Manejar la respuesta de la API
if response.status_code == 200:
    response_data = json.loads(response.text)
    print("Asistente: " + response_data.get('response', 'No se obtuvo una respuesta válida de la API.'))
else:
    print("Error al realizar la solicitud a la API. Código de estado:", response.status_code)