nombre = str(input("Ingrese su nombre: ")).upper()
sexo = str(input("Ingrese su sexo (M o F): ")).upper()

match sexo:
        case "F":
            if nombre[0] < "M":
                print(f"Hola {nombre}, usted corresponde al grupo A")
            else:
                print(f"Hola {nombre}, usted corresponde al grupo B")
        case "M":
            if nombre[0] > "N":
                print(f"Hola {nombre}, usted corresponde al grupo A")
            else:
                print(f"Hola {nombre}, usted corresponde al grupo B") 