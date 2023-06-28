
def calcular_iva():
    precio = float(input("Ingrese el precio del producto: "))
    iva = precio * 0.19
    precio_final = precio + iva
    print(f"El precio final del producto con IVA es:", {precio_final})


def descuento():
    precio = float(input("Ingrese el precio del producto: "))
    descuento = float(input("Ingrese el descuento a aplicar (en porcentaje): "))
    descuento_valor = precio * (descuento / 100)
    precio_final = precio - descuento_valor
    print(f"El precio final del producto con descuento es:", {precio_final})


def calcular_Imc(p, a):
   
    calculo_imc = p / (a ** 2)
    return calculo_imc


while True:
    print("""\nMenu:
          1. Calcular IVA
          2. Descuento
          3. Calcular IMC
          4. Salir  """)


    opcion = int(input("Seleccione una opción: "))
    try:


        if opcion == 1:
            calcular_iva()
        elif opcion == 2:
            descuento()
        elif opcion == 3:
            peso = float(input("Ingresa el peso a consultar(kg): "))
            altura = float(input("Ingresa tu altura (m):  "))
            calcular_Imc(peso, altura)
            if calcular_Imc(peso, altura) <= 18.5:
                print("Tu estado es: Bajo peso")
            elif calcular_Imc(peso, altura) >18.5 and calcular_Imc(peso, altura) <24.9:
                print("Tu estado es: Adecuado")
            elif calcular_Imc(peso, altura) >25.0 and calcular_Imc(peso, altura) <29.9:
                print("Tu estado es: Sobre peso")
            else:
                print("Tu ")
        elif opcion == 4:
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")
    except:
        print("Opción no valida")
