import sys
sys.path.append("Modelo")

from Pregunta import Pregunta
from rol import Rol
from Usuario import Usuario
from Categoria import Categoria
from Etiqueta import Etiqueta
from gemini import Gemini
from openAI import OpenAI
from gestorIA import GestorIA
from agenteIA import AgenteIA


# MÓDULO 1: ROLES, USUARIOS Y AUTENTICACIÓN

print("=== 1. MÓDULO DE USUARIOS Y LOGIN ===")
rol_estudiante = Rol(1, "Estudiante", "Usuario estándar del foro")

facu = Usuario(1, "Facu", "facu@mail.com", "1234", rol_estudiante)
gonzalo = Usuario(2, "Gonzalo", "gonza@mail.com", "abcd", rol_estudiante)

print("Login Facu (clave incorrecta):", facu.iniciar_sesion("facu@mail.com", "0000"))
print("Login Facu (clave correcta):  ", facu.iniciar_sesion("facu@mail.com", "1234"))



# MÓDULO 2: FORO (CATEGORÍAS, ETIQUETAS, PREGUNTAS Y RESPUESTAS)

print("\n=== 2. MÓDULO DEL FORO ===")
cat_programacion = Categoria(1, "Programación", "Dudas sobre código y arquitectura")
etiqueta_python = Etiqueta(1, "Python")
etiqueta_ia = Etiqueta(2, "IA")

# Facu crea una pregunta y le asigna etiquetas
pregunta1 = facu.publicar_pregunta(
    titulo="¿Que son los ArrayList?",
    cuerpo="En java",
    categoria=cat_programacion
)
pregunta1.agregar_etiqueta(etiqueta_python)
pregunta1.agregar_etiqueta(etiqueta_ia)

print("Pregunta publicada:", pregunta1._titulo)
print("¿Tiene etiqueta IA?:", pregunta1.tiene_etiqueta_ia())

# Gonzalo responde la pregunta y Facu la acepta
respuesta_gonza = gonzalo.publicar_respuesta(
    pregunta=pregunta1,
    cuerpo="Tenés que crear una interfaz EstrategiaLLM y cambiarla desde GestorIA."
)
facu.aceptar_respuesta(respuesta_gonza)
print("¿Respuesta de Gonzalo aceptada?:", respuesta_gonza._esAceptada)



# MÓDULO 3: SISTEMA DE VOTOS Y PUNTUACIÓN

print("\n=== 3. MÓDULO DE VOTOS ===")
voto1 = gonzalo.votar(elemento_id=1, es_positivo=True)
voto2 = facu.votar(elemento_id=1, es_positivo=True)
voto3 = gonzalo.votar(elemento_id=1, es_positivo=False)

pregunta1.recibir_voto(voto1)
pregunta1.recibir_voto(voto2)
pregunta1.recibir_voto(voto3)

voto_resp = facu.votar(elemento_id=2, es_positivo=True)
respuesta_gonza.recibir_voto(voto_resp)

print("Puntuación total de la pregunta (esperado 1): ", pregunta1.calcular_puntuacion_total())
print("Puntuación total de la respuesta (esperado 1):", respuesta_gonza.calcular_puntuacion_total())



# MÓDULO 4: INTELIGENCIA ARTIFICIAL (PATRÓN STRATEGY)
print("\n=== 4. MÓDULO DE INTELIGENCIA ARTIFICIAL ===")

# Instanciamos las dos estrategias concretas
estrategia_gemini = Gemini(
    "Poner API KEY" ,
    endpointUrl="https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash-lite:generateContent",
)
estrategia_openai = OpenAI(
    "API_KEY_OPENAI_456", 
    "https://api.openai.com/v1/chat/completions")

# Configuramos el GestorIA empezando con Gemini y creamos el AgenteIA
gestor_ia = GestorIA(estrategia_gemini)
agente_ia = AgenteIA(99, "BotAsistente", 0, "Gemini-3.7-flash", gestor_ia)

# Si la pregunta tiene la etiqueta "IA", el agente genera una respuesta automática
if pregunta1.tiene_etiqueta_ia():
    respuesta_ia_1 = agente_ia.procesarGeneracionAutomatica(pregunta1)
    print("Respuesta generada con Gemini:", respuesta_ia_1._cuerpo)

    # Probamos cambiar de estrategia en tiempo de ejecución hacia OpenAI
    gestor_ia.setEstrategia(estrategia_openai)
    respuesta_ia_2 = agente_ia.procesarGeneracionAutomatica(pregunta1)
    print("Respuesta generada con OpenAI:", respuesta_ia_2._cuerpo)