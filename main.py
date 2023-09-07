import random

def jugar_adivina_el_numero():
    numero_aleatorio = random.randint(1, 20)
    intentos = 0

    print("¡Bienvenido a Adivina el Número!")
    print("Estoy pensando en un número entre 1 y 20.")

    while True:
        intentos += 1
        intento = int(input("Adivina el número: "))

        if intento < numero_aleatorio:
            print("Te has alejado. Intenta un número más alto.")
        elif intento > numero_aleatorio:
            print("Te has alejado. Intenta un número más bajo.")
        else:
            print(f"¡Felicidades! ¡Adivinaste el número en {intentos} intentos!")
            break

    return intentos

def main():
    while True:
        intentos = jugar_adivina_el_numero()
        if intentos == 1:
            print("¡Increíble! Adivinaste en tu primer intento. Eres un experto.")
        elif intentos <= 5:
            print("¡Muy bien! Adivinaste en pocos intentos. ¡Eres bueno en esto!")
        elif intentos <= 10:
            print("Buen trabajo. Adivinaste el número en un número razonable de intentos.")
        else:
            print("Te tomó bastante tiempo, pero adivinaste el número. Sigue practicando.")

        jugar_de_nuevo = input("¿Quieres jugar de nuevo? (s/n): ").lower()
        if jugar_de_nuevo != "s":
            break

    print("¡Gracias por jugar!")

if __name__ == "__main__":
    main()

