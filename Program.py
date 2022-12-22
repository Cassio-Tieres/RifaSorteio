import random as rd
import time as t

lista_de_numeros_rifa = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', 
                        '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', 
                        '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', 
                        '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', 
                        '42', '43', '44', '45', '46', '47', '48', '49', '50']

def iniciaprograma():

    print('***** RIFA DE NATAL *****')
    print(' ')
    print('Lista de números concorrentes abaixo:')

    for number in lista_de_numeros_rifa:
        print(number)

    print(' ')
    print('Este programa roda uma lista (impressa acima), escolhendo um número de maneira aleatória.')
    print(' ')
    
    iniciar = input('Você deseja rodar o programa? S para sim e N para não: \n').upper()

    if iniciar == 'S':
        counter = 0
        while counter < 5:
            counter += 1
            print('Loading...')
        
        print(f'O ganhador é: {lista_de_numeros_rifa[rd.randrange(len(lista_de_numeros_rifa))]}')
    else:
        iniciaprograma()


iniciaprograma()
t.sleep(5)
