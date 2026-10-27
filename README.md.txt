Abstracción y creación de Autoría:
Se diseño la clase abstracta Autor, de la cual heredan Usuario y AgenteIA, la clase respuesta se relaciona únicamente con Autor, esto para generar respuestas tanto de usuarios(humanos) así también como de IA sin duplicar la lógica de la clase Respuesta. Se aplica polimorfismo lo cual es beneficioso para lograr que la plataforma trate a cualquier emisor de igual manera y si en un futuro se agregan mas autores no será necesario modificar la clase Respuesta.


Patrón Strategy:
Se definió la interfaz EstrategiaLLM con la operación generarRespuesta(). La clase GestorIA actúa como el contexto el cual mantiene una referencia a esta interfaz con una composición, las clases concretas OpenAI y Gemini implementan la interfaz encapsulando las peticiones HTTP y credenciales de sus respectivas API. Esto para generar la  integración con modelos de lenguaje (LLM) y respuesta automáticas desacoplando la lógica del dominio.
