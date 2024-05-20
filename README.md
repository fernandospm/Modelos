# Modelos

Divercion 

# 1.Instalacion de ollama
''' shell 
  curl -fsSL https://ollama.com/install.sh | sh '''

  # 2.Ejecutar el servidor
  '''shell ollama serve'''

  # 3.Descargar un modelo
  '''shell ollama pull tinyllama'''

  # ver los modelos descargados 
  '''shell ollama list '''
# 4. llamada a la API REST
'''shell curl http://localhost:11434/api/generate -d '{
  "model": "tinyllama",
  "prompt":"¿por que el cielo es azul?"
}'''

