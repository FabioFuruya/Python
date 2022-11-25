# Funções

# def nome_da_funcao(parametros):
#   corpo da função

from asyncio import format_helpers


def exibe_mensagem():
    print('Seja Bem-vindo')

exibe_mensagem()                            # retorna um valor de string

def exibe_mensagem():
    return 'Seja Bem-vindo'     

print(exibe_mensagem())                     # pega o retorno da string e exibe com o comando print

def soma(v1,v2):
    try:                                    # tratamento de erro
        return float(v1)+float(v2)
    except:
        return False    

def subtracao(v1,v2):
    return v1-v2

def multiplicacao(v1,v2):
    return v1*v2

def divisao(v1,v2):
    # if v1 == 0 or v2 == 0:
    #    return False
    # return v1/v2
    try:
        return v1/v2
    except ZeroDivisionError as error:              # ATENÇÃO: a variável é admitida como string
        print(error)
        return False
    except:
        print('Erro de conversão')    
        return False


opcao = 1
while opcao:
     v1 = (input('Informa valor1: '))
     v2 = (input('Informe valor2:'))
     operador = int(input('''
     1. somar
     2. subtrair
     3. multiplicar
     4. dividir
     Opção: '''))
     if operador == 1:
        print(f'Soma: {soma(v1,v2)}')
     if operador == 2:
        print(f'Subtração: {subtracao(v1,v2)}')        
     if operador == 3:
        print(f'Multiplicação: {multiplicacao(v1,v2)}')    
     if operador == 4:
        print(f'Divisão: {divisao(v1,v2)}')    

     opcao = input(f'\nAperte 0 para sair ou ENTER para continuar')
     if opcao == "0":
        opcao = int(opcao)
     else:
        opcao = 1   
      

# Uso das funções da Biblioteca MATH

from os import system
import math

# help(math)                # exibe a biblioteca MATH

print(math.ceil(4.2))       # inteiro para cima
print(math.floor(3.9))      # inteiro para baixo
print(math.fabs(-1))        # número absoluto
print(math.fmod(11,4))      # resto de uma divisão
print(math.sqrt(36))        # raiz quadrada
print(math.pow(2,3))        # potenciação  -> é igual a print(2**3)


# arredondamento não faz parte da biblioteca MATH
print(round(3.988,1))


# Funções de DATAS
from datetime import datetime, date, time, timedelta

data = date(1986,2,7)                   # padrão: ano, mês, dia
print(data)
print(data.year)
print(data.month)
print(data.day)

dataHoje = datetime.now()
print(dataHoje.date())
print(dataHoje.time())
print(dataHoje.hour)
print(dataHoje.minute)
print(dataHoje.second)
print(dataHoje.weekday())

calendario = dataHoje.isocalendar()
print(calendario.week)                      # número da semana de dataHoje

def idade(nascimento):
    today = datetime(now())
    return today.year - nascimento.year - ((today.month,today.day < (nascimento.month, nascimento.day)))

def totalDiasVividos(nascimento):
    today = datetime.now()
    return abs((nascimento - today).days)

dataNascimento = input('Informe a sua data de nascimento (dd/mm/yyyy): ')
dataNascimento = datetime.strptime(dataNascimento,'%d/%m/%Y')               # y em maiúscula para yyyy
print(dataNascimento)

# print(f'Sua idade é: {idade(dataNascimento)} anos')                       # TÁ COM ERRO !!!
print(f'Você já viveu {totalDiasVividos(dataNascimento)} dias')

def inicioFimSemana():                                                      # TÁ COM ERRO !!!
    if (datetime.today().isoweekday() % 7 - 1) < 0:
        diaInicioSemana = 7 - 1
    else:
        diaInicioSemana = datetime.today().isoweekday() % 7 -1
    dataInicioSemana = datetime.today() - timedelta(days - diaInicioSemana)
    dataFimSemana = dataInicioSemana + timedelta(days=6)
    print(dataInicioSemana.date())
    print(dataFimsemana.date())











