import random

class MatematicasII:
    def __init__(self):
        self.teoremas = {
            "Teorema de Bolzano": "Si una función es continua en un intervalo cerrado [a, b] y signo f(a) ≠ signo f(b), entonces existe un c ∈ (a, b) tal que f(c) = 0.",
            "Teorema de Weierstrass": "Una función continua en un intervalo cerrado y acotado (de números reales) alcanza sus valores máximo y mínimo en puntos del intervalo."
        }
        self.ejercicios_resueltos = {
            "Teorema de Rolle": "f(x) = 1 - x no cumple el teorema de Rolle en el intervalo [-1, 1], porque aunque es continua y derivable, f(-1) no es igual a f(1).",
            "Teorema del valor medio (TVM)": "f(x) = 1/x^2 no cumple el TVM en [0, 2] porque no es continua en ese intervalo."
        }
        self.test_questions = {
            "¿Cuál es el enunciado del Teorema de Bolzano?": "Si una función es continua en un intervalo cerrado [a, b] y signo f(a) ≠ signo f(b), entonces existe un c ∈ (a, b) tal que f(c) = 0.",
            "¿Qué establece el Teorema de Weierstrass?": "Una función continua en un intervalo cerrado y acotado (de números reales) alcanza sus valores máximo y mínimo en puntos del intervalo."
        }
        self.tables_to_complete = {
            "Intervalo donde la función es continua": ["[-1, 1]", "[0, 2]"],
            "Condiciones para que se cumpla el teorema de Rolle": ["Continua y derivable en el intervalo", "f(a) = f(b)"]
        }

    def pregunta_teorica(self):
        teorema = random.choice(list(self.teoremas.keys()))
        print("Pregunta teórica sobre", teorema)
        print(self.teoremas[teorema])

    def ejercicio_resuelto(self):
        teorema = random.choice(list(self.ejercicios_resueltos.keys()))
        print("Ejercicio resuelto sobre", teorema)
        print(self.ejercicios_resueltos[teorema])

    def generar_test(self):
        print("Test:")
        for question, answer in self.test_questions.items():
            print(question)
            user_answer = input("Respuesta: ").strip()
            if user_answer == answer:
                print("Respuesta correcta!\n")
            else:
                print("Respuesta incorrecta. La respuesta correcta es:", answer, "\n")

    def generar_tablas_completar(self):
        print("Completa las siguientes tablas:")
        for title, blanks in self.tables_to_complete.items():
            print(title)
            for blank in blanks:
                user_input = input("Completar: ").strip()
                if user_input == blank:
                    print("Respuesta correcta!")
                else:
                    print("Respuesta incorrecta. La respuesta correcta es:", blank)
            print()  # Agregar línea en blanco entre tablas

matematicas_ii = MatematicasII()
matematicas_ii.pregunta_teorica()
matematicas_ii.ejercicio_resuelto()
matematicas_ii.generar_test()
matematicas_ii.generar_tablas_completar()
