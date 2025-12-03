def registrar_operacion(lista_operaciones): #para registrar tuplas en lista de operaciones
    correct = False  # para conrolar si correcto es tipo
    while (not correct):
        tipo = input("\nDame tipo puede ser ingreso o gasto: ")
        if (tipo.lower() == "ingreso"  or tipo.lower() == "gasto"):
            correct = True
        else:
            print("Info no es correcto")
        
    categoria = input("\nDame categoria: ")

    numPos = False
    while (not numPos):
        try:
            cantidad = float(input("\nDame cantidad: "))
            if cantidad>0 :
                numPos = True
            else:
                print("Puedes usar solo numeros positivos!")
        except ValueError:
            print("Introduce un número válido")
    lista_operaciones.append((tipo, categoria, cantidad))

# mostrar_resumen
def mostrar_resumen(lista_operaciones):
    if (len(lista_operaciones) == 0):
        print("No hay operaciones registradas")
    else:
        for res in lista_operaciones:
            print("Tipo: " + res[0] + "; Categoria: " + res[1] + "; Cantidad: " + str(res[2]) + ";")

#gasto_por_categoria
def gasto_por_categoria(lista_operaciones, categoria):
    count = 0
    gastoTotalCat = 0
    for elem in lista_operaciones:
        if elem[0].lower() == "gasto":
            if (categoria.lower() == elem[1].lower()):
                count += 1
                gastoTotalCat += elem[2]
                print(("Tipo: " + elem[0] + "; Categoria: " + elem[1] + "; Cantidad: " + str(elem[2]) + ";"))
    if (count == 0):
        print("No hay gastos con esta categoria: " + categoria)
    return gastoTotalCat
#calcular_ahorro (ingresos – gastos)
def calcular_ahorro(lista_operaciones):
    ingreso = 0
    gasto = 0
    for elem in lista_operaciones:
        if (elem[0].lower() == "ingreso"):
            ingreso += elem[2]
        if (elem[0].lower() == "gasto"):
            gasto += elem[2]
    return (ingreso - gasto)

### MENU ###
def menu() -> int:
    """Imprime el menú y devuelve la opcion."""
    # escribo el menú
    print("Menú de opciones")
    print("----------------")
    print("1.Registrar un ingreso o un gasto.\n"
          + "2.Mostrar todas las operaciones registradas.\n"
          + "3.Mostrar el gasto total por categoría.\n"
          + "4.Mostrar el ahorro mensual (ingresos – gastos).\n"
          + "5.Mostrar si la economía mensual es saludable.\n"
          + "6.Finalizar.")
    # leo la opción
    cor = False
    while (not cor):
        try:
            opc = int(input("\nIntroduce una opcion: "))
            if (0<opc<7):
                cor = True
            else:
                print("OPCION DE 1-6")
        except ValueError:
            print("Introduce un número válido.")
    return opc

# ------------------
# PROGRAMA PRINCIPAL
# ------------------
lista_operaciones = [] # list for tuplas
while True:
    opcion = menu()
    if opcion == 1:
        registrar_operacion(lista_operaciones)
    elif opcion == 2:
        mostrar_resumen(lista_operaciones)
    elif opcion == 3:
        if not lista_operaciones:
            print("Vacio!")
        else:
            categoria = input("Dame categoria: ")
            print("Gasto total en "+ categoria + " es "+ str(gasto_por_categoria(lista_operaciones, categoria)))
    elif opcion == 4:
        print(calcular_ahorro(lista_operaciones))
    elif opcion == 5:
        k = calcular_ahorro(lista_operaciones)
        if k>0:
            print("Finanzas saludables")
        elif k<0:
            print("Estás gastando más de lo que ingresas")
        else:
            print("Gastas todos tus ingresos")
    elif opcion == 6:
        print("Adios!")
        break