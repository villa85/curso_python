# Librerías a utilizar

import turtle

# Funciones

def dibuja_cuadrado(t, pasos):

    """  La tortuga t dibujará un cuadrado
         el tamaño Cada lado es = pasos.
    """
    for i in range(4):
        t.forward(pasos)
        t.left(90)  # ángulo del giro

# Código o Programa Principal

wn = turtle.Screen()      # define los atributos de la ventana
alex = turtle.Turtle()    # crea una tortuga llamada alex
alex.shape("turtle")

# Llama a la función pasando los argumentos alex y 150
dibuja_cuadrado(alex, 150)
dibuja_cuadrado(alex, 350)
wn.exitonclick()  # cierra la ventana al hacer clic
