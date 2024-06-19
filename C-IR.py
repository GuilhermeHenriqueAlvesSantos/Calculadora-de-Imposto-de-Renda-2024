def removerPuloLinha(lista):
    for index in range(len(lista)):
        lista[index] = lista[index].replace('\n', '')
    return lista

try:
    arquivoAliquotas = open('aliquotas2024.txt', 'r')
    listaAliquotas = removerPuloLinha(arquivoAliquotas.readlines())
    listaAliquotasProcessada = []

    for index in range(len(listaAliquotas)):
        if listaAliquotas[index].split(' ')[0] == 'Faixa':
            if index + 1 > len(listaAliquotas)-1 or index + 2 > len(listaAliquotas)-1 or index + 3 > len(listaAliquotas)-1:
                raise Exception("Verifique se as aliquotas estão com todos os valores!")
            else: listaAliquotasProcessada.append([listaAliquotas[index], float(listaAliquotas[index +1].replace(',', '.')), float(listaAliquotas[index +2].replace(',', '.')), float(listaAliquotas[index +3].replace(',', '.'))])

    arquivoContribuintes = open('contribuintes2024.txt', 'r')
    listaContribuintes = removerPuloLinha(arquivoContribuintes.readlines())
    nomesContribuintes = []
    salariosContribuintes = []
    for index in range(len(listaContribuintes)):
        if index%2 == 0:
            nomesContribuintes.append(listaContribuintes[index])
        else:
            salariosContribuintes.append(float(listaContribuintes[index].replace(',', '.')))

    print(listaAliquotasProcessada)

    for i in range(0, len(salariosContribuintes)):
        if(salariosContribuintes[i] > listaAliquotasProcessada[0][1] and salariosContribuintes[i] < listaAliquotasProcessada[0][2]):
            resultado = (nomesContribuintes[i] + " esta isenta de imposto")
            file = open('result.txt', 'a')
            file.write(f'{resultado}\n')
            file.close() 
        
        if(salariosContribuintes[i] > listaAliquotasProcessada[1][1] and salariosContribuintes[i]< listaAliquotasProcessada[1][2]):
            resultado = (nomesContribuintes[i] + ' Deve pagar R$' + str(round((2112*0 + (salariosContribuintes[i] - listaAliquotasProcessada[1][1])*(listaAliquotasProcessada[1][3]/100)), 2)))
            file = open('result.txt', 'a')
            file.write(f'{resultado}\n')
            file.close() 
            
        if(salariosContribuintes[i] > listaAliquotasProcessada[2][1] and salariosContribuintes[i]< listaAliquotasProcessada[2][2]):
            resultado = (nomesContribuintes[i] + ' Deve pagar R$' + str(round((2112*0 + (listaAliquotasProcessada[1][2] - listaAliquotasProcessada[1][1]) * (listaAliquotasProcessada[1][3]/100) + (salariosContribuintes[i] - listaAliquotasProcessada[2][1]) * (listaAliquotasProcessada[2][3]/100)), 2)))
            file = open('result.txt', 'a')
            file.write(f'{resultado}\n')
            file.close() 
        
        if(salariosContribuintes[i] > listaAliquotasProcessada[3][1] and salariosContribuintes[i]< listaAliquotasProcessada[3][2]):
            resultado = (nomesContribuintes[i] + ' Deve pagar R$' + str(round((2112*0 + (listaAliquotasProcessada[1][2] - listaAliquotasProcessada[1][1]) * (listaAliquotasProcessada[1][3]/100) + (listaAliquotasProcessada[2][2] - listaAliquotasProcessada[2][1]) * (listaAliquotasProcessada[2][3]/100) + (salariosContribuintes[i]-listaAliquotasProcessada[3][1])*(listaAliquotasProcessada[3][3]/100)), 2)))
            file = open('result.txt', 'a')
            file.write(f'{resultado}\n')
            file.close() 
       
        if(salariosContribuintes[i] > listaAliquotasProcessada[4][1] and salariosContribuintes[i]< listaAliquotasProcessada[4][2]):
            resultado = (nomesContribuintes[i] + ' Deve pagar R$' + str(round((2112*0 + (listaAliquotasProcessada[1][2] - listaAliquotasProcessada[1][1]) * (listaAliquotasProcessada[1][3]/100) + (listaAliquotasProcessada[2][2] - listaAliquotasProcessada[2][1]) * (listaAliquotasProcessada[2][3]/100) + (listaAliquotasProcessada[3][2] - listaAliquotasProcessada[3][1]) * (listaAliquotasProcessada[3][3]/100) + (salariosContribuintes[i]-listaAliquotasProcessada[4][1]) * (listaAliquotasProcessada[4][3]/100)), 2)))
            file = open('result.txt', 'a')
            file.write(f'{resultado}\n')
            file.close() 


except ValueError:
    print('verifique se os valores passados são valores')
except (NameError):
    print('Algo deu errado\n' + NameError)