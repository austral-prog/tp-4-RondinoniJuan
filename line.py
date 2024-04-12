import math
def line():
    A = float(input (""))
    B = float(input (""))
    X1 = float(input (""))
    Y1 = float(((A * X1) + B))
    X2 = float(input (""))
    Y2 = float(((A * X2) + B))

    print (f"El Coeficiente A de su ecuacion de la recta es: {A}")
    print (f"El Coeficiente B de su ecuacion de la recta es: {B}")
    print (f"El Coeficiente X1 de su ecuacion de la recta es: {X1}")
    print (f"El Coeficiente X2 de su ecuacion de la recta es: {X2}\n")\ 
    print ("Para la siguiente ecuacion: ")
    print (f"\t Y = {A}X + {B}\n")

    print ("Dados los siguientes puntos:")
    print (f"\tP1 ({X1}, {Y1})")
    print (f"\tP2 ({X2}, {Y2})\n")
    print (f"La distancia entre ellos es: {math.sqrt((X1 - X2)**2 + (Y1 - Y2)**2)}")
