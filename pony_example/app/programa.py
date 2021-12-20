from pony.orm import *
from pony import orm
import sys
sys.path.append('/pony/database')
import connection

continuarLoop = True

opcoes = {
        1: 'listar todas as |pessoas|',
        2: 'pesquisar |pessoas| por nome',
        0: 'sair'
        }

def logador(mensagem):
    separador = "\nzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz\n"
    print(separador)
    print(mensagem)
    print(separador)

def gera_lista_menu():
    separador = "\n----------------------------------------\n"
    print(separador)
    for k, v in opcoes.items():
        print(f"opcao {k} = {v}")
    print(separador)

def valida_opcao(op):
    if op == 1:
        connection.db.Person.select().show()
    elif op == 2:
        nome = input("informe por favor o nome para pesquisa: ")
        print("resultado(s):")
        result = orm.select(p.name for p in connection.db.Person if p.name == nome)[:]
        if len(result) > 0:
            print(result)
        else:
            print(f"nenhum registro encontrado com o nome {nome}")
    elif op == 0:
        print("saindo...")
        global continuarLoop
        continuarLoop = False
    else:
        logador(f"zzzzzzzzz OPCAO {op} INVALIDA zzzzzzzzz")

with connection.db_session:
    while continuarLoop == True:
        gera_lista_menu()
        opcao = int(input("Por favor selecione a opcao desejada: "))
        valida_opcao(opcao)
