
import json
import os

ARQUIVO_CONTATOS = "dados_contatos.json"


def carregar_contatos():
    if os.path.exists(ARQUIVO_CONTATOS):
        with open(ARQUIVO_CONTATOS, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    return []


def salvar_contatos(contatos):
    with open(ARQUIVO_CONTATOS, "w", encoding="utf-8") as arquivo:
        json.dump(contatos, arquivo, ensure_ascii=False, indent=4)


def cadastrar_contato():
    print("\n--- CADASTRO DE CONTATO ---")

    nome = input("Digite o nome: ").strip()
    telefone = input("Digite o telefone: ").strip()
    email = input("Digite o e-mail: ").strip()

    if not nome or not telefone or not email:
        print("Erro: preencha todos os campos.")
        return

    contatos = carregar_contatos()

    contato = {
        "nome": nome,
        "telefone": telefone,
        "email": email
    }

    contatos.append(contato)
    salvar_contatos(contatos)

    print("Contato cadastrado com sucesso!")


def consultar_contatos():
    print("\n--- LISTA DE CONTATOS ---")

    contatos = carregar_contatos()

    if not contatos:
        print("Nenhum contato cadastrado.")
        return

    for numero, contato in enumerate(contatos, start=1):
        print(f"\nContato {numero}")
        print(f"Nome: {contato['nome']}")
        print(f"Telefone: {contato['telefone']}")
        print(f"E-mail: {contato['email']}")



def buscar_contato():

    
 def excluir_contato():
    print("\n--- EXCLUIR CONTATO ---")

    nome_busca = input("Digite o nome do contato que deseja excluir: ").strip().lower()

    contatos = carregar_contatos()

    encontrados = [
        contato for contato in contatos
        if contato["nome"].lower() == nome_busca
    ]

    if not encontrados:
        print("Contato não encontrado.")
        return

    if len(encontrados) > 1:
        print("Há mais de um contato com esse nome. Exclusão cancelada.")
        return

    contato = encontrados[0]
    contatos.remove(contato)
    salvar_contatos(contatos)

    print("Contato excluído com sucesso!")

    print("\n--- BUSCAR CONTATO ---")

    nome_busca = input("Digite o nome do contato: ").strip().lower()

    contatos = carregar_contatos()

    encontrados = [
        contato for contato in contatos
        if nome_busca in contato["nome"].lower()
    ]

    if not encontrados:
        print("Nenhum contato encontrado.")
        return

    for contato in encontrados:
        print("\nContato encontrado!")
        print(f"Nome: {contato['nome']}")
        print(f"Telefone: {contato['telefone']}")
        print(f"E-mail: {contato['email']}")


def excluir_contato():
    print("\n--- EXCLUIR CONTATO ---")

    nome_busca = input(
        "Digite o nome do contato que deseja excluir: "
    ).strip().lower()

    contatos = carregar_contatos()

    encontrados = [
        contato for contato in contatos
        if contato["nome"].lower() == nome_busca
    ]

    if not encontrados:
        print("Contato não encontrado.")
        return

    if len(encontrados) > 1:
        print("Há mais de um contato com esse nome.")
        print("Exclusão cancelada.")
        return

    contato = encontrados[0]
    contatos.remove(contato)
    salvar_contatos(contatos)

    print("Contato excluído com sucesso!")


def editar_contato():
    print("\n--- EDITAR CONTATO ---")

    nome_busca = input(
        "Digite o nome do contato que deseja editar: "
    ).strip().lower()

    contatos = carregar_contatos()

    encontrados = [
        contato for contato in contatos
        if contato["nome"].lower() == nome_busca
    ]

    if not encontrados:
        print("Contato não encontrado.")
        return

    if len(encontrados) > 1:
        print("Há mais de um contato com esse nome.")
        print("Edição cancelada.")
        return

    contato = encontrados[0]

    print(f"Nome: {contato['nome']}")
    print(f"Telefone atual: {contato['telefone']}")
    print(f"E-mail atual: {contato['email']}")

    novo_telefone = input(
        "Digite o novo telefone (Enter para manter): "
    ).strip()

    novo_email = input(
        "Digite o novo e-mail (Enter para manter): "
    ).strip()

    if novo_telefone:
        contato["telefone"] = novo_telefone

    if novo_email:
        contato["email"] = novo_email

    salvar_contatos(contatos)

    print("Contato atualizado com sucesso!")
