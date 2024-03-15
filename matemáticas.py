import random

class MatematicasII:
    def __init__(self):
        self.teoremas = {
            "Teorema de Bolzano": "Si una función es continua en un intervalo cerrado [a, b] y signo f(a) ≠ signo f(b) ≠ signo f(b) ≠ signo f(b) , entonces existe un c ∈ [a, b] tal que f(c) = 0",
            "Teorema de Weierstrass": "Una función continua en un intervalo cerrado y acotado (de números reales) alcanza sus valores máximo y mínimo en puntos del intervalo", 
        }
        self.ejercicios_resueltos = {
            "Teorema de Rolle": "f(x)=1-x no cumple el teorema de Rolle en el intervalo [-1,1], porque aunque es continua y derivable, f(-1) no es igual a f(1).",
            "Teorema del valor medio(TVM)": "f(x)=1/x^2 no cumple el TVM en [0,2] porque no es continua en ese intervalo"
        }

    def pregunta_teorica(self):
        teorema = random.choice(list(self.teoremas.keys()))
        print("Pregunta teórica sobre", teorema)
        print(self.teoremas[teorema])

    def ejercicio_resuelto(self):
        teorema = random.choice(list(self.ejercicios_resueltos.keys()))
        print("Ejercicio resuelto sobre", teorema)
        print(self.ejercicios_resueltos[teorema])

matematicas_ii = MatematicasII()
matematicas_ii.pregunta_teorica()
matematicas_ii.ejercicio_resuelto()
