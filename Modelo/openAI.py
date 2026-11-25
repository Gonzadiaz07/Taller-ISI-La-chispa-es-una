from estrategiaLLM import EstrategiaLLM
import requests # Se debe hacer en la terminal powershell: py -m pip install requests

class OpenAI(EstrategiaLLM):
    def __init__(self, apiKey: str, endpointUrl: str):
        self._apiKey = apiKey
        self._endpointUrl = endpointUrl

    def conectarApiOpenAI(self) -> bool:
        # Se verifica que el codigo verifique los nombres parametros y tipos de retorno del diagrama 
        return bool(self._apiKey and self._endpointUrl)

    def generarRespuesta(self, contexto: str) -> str:
        if not self.conectarApiOpenAI():
            raise ConnectionError("Faltan la API Key o el endpoint de OpenAI.")

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self._apiKey}",
        }
        payload = {
            "model": "gpt-4o-mini",
            "messages": [{"role": "user", "content": contexto}],
        }

        try:
            response = requests.post(
                self._endpointUrl, headers=headers, json=payload, timeout=30
            )
            response.raise_for_status()
            data = response.json()
            return data["choices"][0]["message"]["content"]
        except requests.exceptions.HTTPError as e:
            codigo = (
                e.response.status_code if e.response is not None else "desconocido"
            )
            return (
                f"[Error OpenAI {codigo}] No se pudo generar la respuesta: "
                "se requiere una API Key activa con plan de pago/saldo."
            )
        except requests.exceptions.RequestException:
            return "[Error OpenAI] No se pudo establecer conexión con el servidor."