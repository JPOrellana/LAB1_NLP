import re
import random

# Lista de saludos válidos
saludos_validos = [
    r"\b(hola)\b",
    r"\b(qué tal)\b",
    r"\b(buenos días)\b",
    r"\b(buenas tardes)\b",
    r"\b(buenas noches)\b"
]

# Lista de apodos ofensivos
apodos_ofensivos = ["tonta", "idiota", "estúpida", "inútil"]

# Patrones de conversación y respuestas
patrones_respuestas = {
    r"me siento (.*)": [
        "¿Por qué te sientes así?",
        "Entiendo que te sientas {0}.",
        "¿Desde cuándo te sientes {0}?"
    ],
    r"estoy (.*)": [
        "¿Qué te hace sentir {0}?",
        "¿Crees que estar {0} es algo bueno o malo?",
        "¿Cómo reaccionan los demás cuando estás {0}?"
    ],
    r"mi (.*)": [
        "Cuéntame más sobre tu {0}.",
        "¿Por qué mencionas tu {0}?",
        "¿Cómo te sientes respecto a tu {0}?"
    ],
    r"(.*\btrabajo\b.*)": [
        "Háblame más sobre tu trabajo.",
        "¿Qué es lo que más te gusta de tu trabajo?",
        "¿Te sientes satisfecho con tu trabajo?"
    ],
    r"(.*)\?$": [
        "¿Por qué lo preguntas?",
        "¿Qué opinas tú?",
        "Esa es una buena pregunta."
    ]
}

def eliza_bot(mensaje, estado_saludo):
    saludo_detectado = any(re.search(s, mensaje, re.IGNORECASE) for s in saludos_validos)

    if not estado_saludo:
        if saludo_detectado:
            estado_saludo = True
            return "Hola, ¿cómo estás?", estado_saludo
        else:
            return "Es importante iniciar una conversación con un saludo.", estado_saludo

    if re.search(r"\beliza\b", mensaje, re.IGNORECASE):
        return "Hola, ¿cómo estás?", estado_saludo

    if any(apodo in mensaje.lower() for apodo in apodos_ofensivos):
        return "No me trates así.", estado_saludo

    for patron, respuestas in patrones_respuestas.items():
        match = re.search(patron, mensaje, re.IGNORECASE)
        if match:
            if match.lastindex:
                parte = match.group(1)
                return random.choice(respuestas).format(parte), estado_saludo
            else:
                return random.choice(respuestas), estado_saludo

    return "No puedo comprender tu comentario.", estado_saludo

# Simulación simple
if __name__ == "__main__":
    estado = False
    print("Eliza: ¡Hola! Para iniciar debes saludar.")
    while True:
        entrada = input("Tú: ")
        if entrada.lower() in ["salir", "adiós", "exit", "quit"]:
            print("Eliza: Hasta pronto.")
            break
        respuesta, estado = eliza_bot(entrada, estado)
        print(f"Eliza: {respuesta}")
