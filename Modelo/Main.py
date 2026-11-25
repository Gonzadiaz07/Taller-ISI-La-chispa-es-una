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



# DATOS INICIALES DEL SISTEMA (EN MEMORIA)

rol_estudiante = Rol(1, "Estudiante", "Usuario estándar del foro")
cat_programacion = Categoria(1, "Programación", "Dudas sobre código y arquitectura")
etiqueta_python = Etiqueta(1, "Python")
etiqueta_ia = Etiqueta(2, "IA")

# Usuarios precargados (podés iniciar sesión con estos o registrar nuevos)
usuarios: list[Usuario] = [
    Usuario(1, "Facu", "facu@email.com", "1234", rol_estudiante),
    Usuario(2, "Gonza", "gonza@email.com", "abcd", rol_estudiante),
]

# Lista compartida donde se guardan todas las preguntas publicadas
preguntas_publicadas: list[Pregunta] = []

# FUNCIONES AUXILIARES
def pedir_voto_positivo_negativo(mensaje: str) -> bool:
    while True:
        opinion = input(mensaje).strip().lower()
        if opinion in ("positiva", "positivo", "p", "+"):
            return True
        elif opinion in ("negativa", "negativo", "n", "-"):
            return False
        print("Opción no válida. Escribí 'positiva' o 'negativa'.")


def seleccionar_estrategia_ia():
    while True:
        opcion = input("¿Qué IA querés que responda? (Gemini / OpenAI): ").strip().lower()

        if opcion == "gemini":
            estrategia = Gemini(
                "Poner API KEY",
                endpointUrl="https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash-lite:generateContent",
            )
            return estrategia, "Gemini-3.7-flash"

        elif opcion == "openai":
            estrategia = OpenAI(
                "API_KEY_OPENAI_456",
                "https://api.openai.com/v1/chat/completions"
            )
            return estrategia, "GPT-4o"

        print("Opción no válida. Escribí 'Gemini' o 'OpenAI'.")


def evaluar_respuesta_ia(usuario: Usuario, pregunta: Pregunta, respuesta) -> None:
    print("\nRespuesta de la IA:", respuesta._cuerpo)

    if respuesta._cuerpo.startswith("[Error") or "plan de pago" in respuesta._cuerpo.lower():
        print("No se puede calificar ni aceptar esta respuesta porque no se cuenta con un plan de pago/API Key válida.")
        return

    pregunta.agregar_respuesta(respuesta)
    es_positivo = pedir_voto_positivo_negativo("¿La respuesta fue positiva o negativa? (positiva/negativa): ")

    if es_positivo:
        usuario.aceptar_respuesta(respuesta)

    voto = usuario.votar(elemento_id=respuesta._id, es_positivo=es_positivo)
    respuesta.recibir_voto(voto)

    print(f"Voto {'positivo' if es_positivo else 'negativo'} registrado.")
    print("¿Respuesta aceptada?:", respuesta._esAceptada)
    print("Puntuación total de la respuesta:", respuesta.calcular_puntuacion_total())


def hacer_pregunta(usuario: Usuario) -> None:
    print("\n--- HACER UNA PREGUNTA ---")
    titulo = input("Ingresá tu pregunta: ")
    cuerpo = input("Ingresá el contexto (cuerpo) de la pregunta: ")

    nueva_pregunta = usuario.publicar_pregunta(
        titulo=titulo,
        cuerpo=cuerpo,
        categoria=cat_programacion
    )
    nueva_pregunta.agregar_etiqueta(etiqueta_python)
    nueva_pregunta.agregar_etiqueta(etiqueta_ia)
    preguntas_publicadas.append(nueva_pregunta)

    print("\nPregunta publicada con éxito:", nueva_pregunta._titulo)

    if nueva_pregunta.tiene_etiqueta_ia():
        estrategia, version_modelo = seleccionar_estrategia_ia()
        gestor_ia = GestorIA(estrategia)
        agente_ia = AgenteIA(99, "BotAsistente", 0, version_modelo, gestor_ia)

        respuesta_ia = agente_ia.procesarGeneracionAutomatica(nueva_pregunta)
        evaluar_respuesta_ia(usuario, nueva_pregunta, respuesta_ia)


def valorar_respuesta(usuario: Usuario) -> None:
    print("\n--- VALORAR UNA RESPUESTA ---")
    preguntas_con_respuestas = [
        (preg, resp)
        for preg in preguntas_publicadas
        for resp in preg._respuestas
    ]

    if not preguntas_con_respuestas:
        print("No hay respuestas publicadas todavía para valorar.")
        return

    print("Preguntas y respuestas disponibles:")
    for indice, (preg, resp) in enumerate(preguntas_con_respuestas, start=1):
        autor_preg = preg._autor._nombre if preg._autor else "Anónimo"
        autor_resp = resp._autor._nombre if resp._autor else "IA"
        print(f"\n{indice}. Pregunta ({autor_preg}): {preg._titulo}")
        print(f"   Contexto: {preg._cuerpo}")
        print(f"   Respuesta ({autor_resp}): {resp._cuerpo}")
        print(f"   [Puntuación actual: {resp.calcular_puntuacion_total()} | Aceptada: {resp._esAceptada}]")

    while True:
        seleccion = input("\nElegí el número de la respuesta que querés valorar (o 0 para volver): ").strip()
        if seleccion == "0":
            return
        if seleccion.isdigit() and 1 <= int(seleccion) <= len(preguntas_con_respuestas):
            pregunta_elegida, respuesta_elegida = preguntas_con_respuestas[int(seleccion) - 1]
            break
        print("Número inválido. Intentá de nuevo.")

    es_positivo = pedir_voto_positivo_negativo("¿Tu valoración para esta respuesta es positiva o negativa? (positiva/negativa): ")

    if es_positivo and pregunta_elegida._autor == usuario:
        usuario.aceptar_respuesta(respuesta_elegida)

    voto = usuario.votar(elemento_id=respuesta_elegida._id, es_positivo=es_positivo)
    respuesta_elegida.recibir_voto(voto)

    print(f"Valoración {'positiva' if es_positivo else 'negativa'} registrada.")
    print("¿Respuesta aceptada?:", respuesta_elegida._esAceptada)
    print("Nueva puntuación total de la respuesta:", respuesta_elegida.calcular_puntuacion_total())



# MENÚS DE NAVEGACIÓN (AUTENTICACIÓN Y SESIÓN ACTIVA)

def registrar_usuario() -> None:
    print("\n--- REGISTRO DE USUARIO ---")
    nombre = input("Nombre: ").strip()
    email = input("Email: ").strip()

    if any(u._email == email for u in usuarios):
        print("Ya existe un usuario registrado con ese email.")
        return

    contraseña = input("Contraseña: ").strip()
    nuevo_id = len(usuarios) + 1
    nuevo_usuario = Usuario(nuevo_id, nombre, email, contraseña, rol_estudiante)
    usuarios.append(nuevo_usuario)
    print(f"Usuario '{nombre}' registrado correctamente. Ya podés iniciar sesión.")


def iniciar_sesion_menu() -> Usuario | None:
    print("\n--- INICIAR SESIÓN ---")
    email = input("Email: ").strip()
    contraseña = input("Contraseña: ").strip()

    for u in usuarios:
        if u.iniciar_sesion(email, contraseña):
            print(f"\n¡Bienvenido/a, {u._nombre}!")
            return u

    print("Email o contraseña incorrectos.")
    return None


def menu_sesion_activa(usuario: Usuario) -> None:
    while True:
        print(f"\n=== MENÚ PRINCIPAL ({usuario._nombre}) ===")
        print("1. Hacer una pregunta")
        print("2. Valorar una respuesta")
        print("3. Cerrar sesión")

        opcion = input("Elegí una opción: ").strip()

        if opcion == "1":
            hacer_pregunta(usuario)
        elif opcion == "2":
            valorar_respuesta(usuario)
        elif opcion == "3":
            print(f"Cerrando sesión de {usuario._nombre}...")
            break
        else:
            print("Opción no válida. Elegí 1, 2 o 3.")



# BUCLE PRINCIPAL DEL PROGRAMA

while True:
    print("\n===============================")
    print("   FORO ACADÉMICO CON IA")
    print("===============================")
    print("1. Registrarse")
    print("2. Iniciar sesión")
    print("0. Salir")

    opcion_inicio = input("Elegí una opción: ").strip()

    if opcion_inicio == "1":
        registrar_usuario()
    elif opcion_inicio == "2":
        usuario_logueado = iniciar_sesion_menu()
        if usuario_logueado is not None:
            menu_sesion_activa(usuario_logueado)
    elif opcion_inicio == "0":
        print("Saliendo del sistema...")
        break
    else:
        print("Opción no válida. Elegí 1, 2 o 0.")