
def comparar_cadena(cadena):
    lista_cadena = list()
    for letra in cadena : lista.append(letra)
    lista_invertida = lista_cadena[::-1]
    if lista_invertida == lista_cadena:
        print("Enhorabuena, son iguales al invertirla")
    else:
        print("las inverti pero son distintas")


def main():
    cadena = input("ingresa cadena para comparar: ")
    comparar_cadena(cadena)
main()
