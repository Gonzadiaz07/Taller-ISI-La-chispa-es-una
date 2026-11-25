import requests # Se debe hacer en la terminal powershell: py -m pip install requests
from estrategiaLLM import EstrategiaLLM

class Gemini(EstrategiaLLM):
    def __init__(self, apiKey: str, endpointUrl: str):
        self._apiKey = apiKey
        self._endpointUrl = endpointUrl

   
    def conectarApiGemini(self) -> bool:
        # Se verifica que el codigo verifique los nombres parametros y tipos de retorno del diagrama 
        if not self._apiKey or not self._endpointUrl:
            return False
        
        # Acá iría la lógica real de conexión (por ejemplo, usando la librería requests o google-genai)
        return True

    def generarRespuesta(self, contexto: str) -> str:
        # Utilizamos el metodo de estrategiaLLM para generar una respuesta a partir del contexto recibido
        if not self.conectarApiGemini():
            raise ConnectionError("Falta la API Key o el endpoint de Google DeepMind.")

        headers = {
            "Content-Type": "application/json",
            "x-goog-api-key": self._apiKey,
        }
        payload = {
            "contents": [{"parts": [{"text": contexto}]}]
        }

        response = requests.post(
            self._endpointUrl, headers=headers, json=payload, timeout=90
        )
        if not response.ok:
            print("DETALLE DEL ERROR:", response.text)
        response.raise_for_status()

        data = response.json()
        return data["candidates"][0]["content"]["parts"][0]["text"]