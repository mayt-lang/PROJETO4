
from compromissos import cadastrar_compromisso, consultar_compromissos
from compromissos import cadastrar_compromisso, consultar_compromissos, editar_compromisso, excluir_compromisso
def exibir_menu():
    print("\n===================================")
    print(" SISTEMA DE AGENDA")
    print(" CONTATOS E COMPROMISSOS")
    print("===================================")
    print("1 - Cadastrar contato")
    print("2 - Consultar contatos")
    print("3 - Cadastrar compromisso")
    print("4 - Consultar compromissos")
    print("5 - Buscar contato pelo nome")
    print("6 - Excluir contato")
    print("7 - Editar contato")
    print("8 - Editar compromisso")
    print("9 - Excluir compromisso")
    print("0 - Sair")
    print("===================================")


while True:
    exibir_menu()

    opcao = input("Escolha uma opção: ").strip()

    if opcao == "1":
        cadastrar_contato()

    elif opcao == "2":
        consultar_contatos()

    elif opcao == "3":
        cadastrar_compromisso()

    elif opcao == "4":
        consultar_compromissos()

    elif opcao == "5":
        buscar_contato()

    elif opcao == "6":
      excluir_contato()

    elif opcao == "7":
     editar_contato()

    elif opcao == "8":
     editar_compromisso()

    elif opcao == "9":
     excluir_compromisso()

    elif opcao == "0":
        print("Sistema encerrado. Até logo!")
        break

    else:
        print("Opção inválida. Tente novamente.")
