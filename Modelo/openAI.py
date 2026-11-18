from estrategiaLLM import EstrategiaLLM


class OpenAI(EstrategiaLLM):
    def __init__(self, apiKey: str, endpointUrl: str):
        self._apiKey = apiKey
        self._endpointUrl = endpointUrl

   
    def conectarApiOpenAI(self) -> bool:
        # Se verifica que el codigo verifique los nombres parametros y tipos de retorno del diagrama 
        if not self._apiKey or not self._endpointUrl:
            return False
        
        # Acá iría la lógica real de conexión (por ejemplo, usando la librería requests o google-genai)
        return True

    def generarRespuesta(self, contexto: str) -> str:
        # Utilizamos el metodo de estrategiaLLM para generar una respuesta a partir del contexto recibido
        if not self.conectarApiOpenAI():
            raise ConnectionError("No se pudo conectar con la API de OpenAI.")

        # Simulación de la respuesta generada por el modelo
        return f"[Respuesta generada por OpenAI] Basado en: {contexto}"