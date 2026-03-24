from tablero import Tablero  # Importa la clase Tablero para crear el tablero del juegoo

class Juego:
    def __init__(self):
        # Crea una instancia del tablero
        self.tablero = Tablero()

        # Lanza varios ataques de prueba al iniciar el juego
        self.lanzar_ataque(1, 0)
        self.lanzar_ataque(1, 0)
        self.lanzar_ataque(1, 1)
        self.lanzar_ataque(1, 2)
        self.lanzar_ataque(2, 1)
        self.lanzar_ataque(1, 4)

    def mostrar_resultado(self, resultado):
        # Muestra por pantalla el resultado del disparo según el valor recibido
        if resultado == 0:
            print("Agua")
        elif resultado == 1:
            print("Tocado")
        elif resultado == 2:
            print("Hundido")

    def lanzar_ataque(self, x, y):
        # Muestra las coordenadas a las que se dispara
        print(f"Ataque a {x},{y}")

        # Accede a la casilla concreta del tablero usando fila y columna
        casilla = self.tablero.casillero[x][y]

        # Llama al método de la casilla para procesar el disparo
        resultado = casilla.recibir_disparo()

        # Si el resultado no es None, significa que el disparo sí produce un resultado válido
        # None ocurre cuando la casilla ya había sido disparada antes
        if resultado is not None:
            self.mostrar_resultado(resultado)

# Crea y ejecuta el juego
juego = Juego()