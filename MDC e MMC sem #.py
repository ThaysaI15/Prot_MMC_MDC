ficar = int(1)
while ficar == 1:
    print("Olá, deseja realizar qual cálculo?\n1 - MMC(Mínimo multiplo comum)\n2 - MDC(Máximo divisor comum)\n ")
    opera = int(input("Insira aqui sua resposta: "))
    while opera == 1:
        print ("\n~~~~~~~~~~~~~~ MMC(Mínimo multiplo comum) ~~~~~~~~~~~~~~\n")
        v1 = int(input("Insira o primeiro valor: "))
        v2 = int(input("Insira o segundo valor: "))
        lista1 = []
        lista2 = []
        
        mmc1 = int(0)
        mmc2 = int(0)
        for i in range(0, 80):
            mmc1, mmc2 = mmc1 + v1, mmc2 + v2
            lista1.append(mmc1) 
            lista2.append(mmc2) 
        
        i = -1
        resultado = 0
        while i < len(lista1) and resultado == 0:
            i = i+1
            if lista1[i] in lista2:
                resultado = round(lista1[i])
                break
        print (f"\nO MMC de {v1} e de {v2} é: {resultado}")
        sair = int(input("\nO que deseja fazer?\n1 - Fazer outro cálculo\n2 - Voltar para o menu\n3 - Sair\n\nInsira sua resposta: "))
        if sair == 2:  
            break 
        if sair == 3:
            opera = 0
            ficar = 0


    while opera == 2:
        print ("\n~~~~~~~~~~~~~~ MDC(Máximo divisor comum) ~~~~~~~~~~~~~~\n")
        v1 = int(input("Insira o primeiro valor: "))
        v2 = int(input("Insira o segundo valor: "))
        lista1 = []
        lista2 = []
        i = 0

        for j in range(1,(v1+1)):
            i = i+1
            rest = v1 % j
            if rest == 0:
                lista1.append(j)
        i = 0
        for j in range(1,(v2+1)):
            i = i+1
            rest = v2 % j
            if rest == 0:
                lista2.append(j)

        lista1.reverse()
        lista2.reverse()

        i = -1
        resultado = 0

        while (i < len(lista1) or i < len(lista2)) and resultado == 0:
            i = i+1
            if lista1[i] in lista2:
                resultado = round(lista1[i])
                break

        lista1 = sorted(lista1)
        lista2 = sorted(lista2)
        print (f"{v1} = {lista1}")
        print (f"{v2} = {lista2}")
        print (f"\nO MDC de {v1} e de {v2} é: {resultado}")
        sair = int(input("\nO que deseja fazer?\n1 - Fazer outro cálculo\n2 - Voltar para o menu\n3 - Sair\n\nInsira sua resposta: "))
        if sair == 2:  
            break 
        if sair == 3:
            opera = 0
            ficar = 0
else:
    print ("Programa fechado")