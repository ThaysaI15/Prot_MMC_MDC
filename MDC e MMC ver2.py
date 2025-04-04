import math
ficar = int(1)
def mdc ():
    v1 = int(input("Insira o primeiro valor: "))
    v2 = int(input("Insira o segundo valor: "))
    va1, va2 = v1, v2
    resultado = 0
    while resultado == 0:

        if va1 % va2 == 0 or va2 % va1 == 0:
            resultado = min(va1, va2)
            return v1, v2, resultado
        
        if v1 > v2:
            d = va1//va2
            rest = va1 - va2 * d
            if rest == 0:
                resultado = va1
                return v1, v2, resultado
            else:
                va1, va2 = va2, rest
        if v2 > v1:
            d = va2//va1
            rest = va2 - va1 * d
            if rest == 0:
                resultado = va1
                return v1, v2, resultado
            else:
                va2, va1 = va1, rest
        
while ficar == 1:
    print ("\n----------------------------------")
    print("Olá, deseja realizar qual cálculo?\n\n1 - MMC(Mínimo multiplo comum)\n2 - MDC(Máximo divisor comum)")
    print ("----------------------------------\n")
    opera = math.floor(float(input("Insira aqui sua resposta: ")))
    if opera != 1 and opera != 2:
        print ("--------------------------------------------")
        print ("Valor inválido. Por favor, digite novamente")
        print ("--------------------------------------------")
    while opera == 1:
        print ("\n~~~~~~~~~~~~~~ MMC(Mínimo multiplo comum) ~~~~~~~~~~~~~~\n")
        v1, v2, resultado = mdc()
        resultado = round(v1*v2/resultado)

        print (f"\nO MMC de {v1} e de {v2} é: {resultado}")
        sair = int(input("\nO que deseja fazer?\n1 - Fazer outro cálculo\n2 - Voltar para o menu\n3 - Sair\n\nInsira sua resposta: "))
        if sair == 2:  
            break 
        if sair == 3:
            opera = 0
            ficar = 0


    while opera == 2:
        print ("\n~~~~~~~~~~~~~~ MDC(Máximo divisor comum) ~~~~~~~~~~~~~~\n")
        v1, v2, resultado = mdc()
        print (f"\nO MDC de {v1} e de {v2} é: {resultado}")
        sair = int(input("\nO que deseja fazer?\n1 - Fazer outro cálculo\n2 - Voltar para o menu\n3 - Sair\n\nInsira sua resposta: "))
        if sair == 2:  
            break 
        if sair == 3:
            opera = 0
            ficar = 0
else:
    print ("Programa fechado")
