
import json
import os

ARQUIVO_COMPROMISSOS = "dados_compromissos.json"


def carregar_compromissos():
    if os.path.exists(ARQUIVO_COMPROMISSOS):
        with open(
            ARQUIVO_COMPROMISSOS, "r", encoding="utf-8"
        ) as arquivo:
            return json.load(arquivo)

    return []


def salvar_compromissos(compromissos):
    with open(
        ARQUIVO_COMPROMISSOS, "w", encoding="utf-8"
    ) as arquivo:
        json.dump(
            compromissos,
            arquivo,
            ensure_ascii=False,
            indent=4
        )


def cadastrar_compromisso():
    print("\n--- CADASTRO DE COMPROMISSO ---")

    titulo = input("Digite o título: ").strip()
    data = input("Digite a data (DD/MM/AAAA): ").strip()
    horario = input("Digite o horário (HH:MM): ").strip()
    descricao = input("Digite a descrição: ").strip()

    if not titulo or not data or not horario or not descricao:
        print("Erro: preencha todos os campos.")
        return

    compromissos = carregar_compromissos()

    compromisso = {
        "titulo": titulo,
        "data": data,
        "horario": horario,
        "descricao": descricao
    }

    compromissos.append(compromisso)
    salvar_compromissos(compromissos)

    print("Compromisso cadastrado com sucesso!")


def consultar_compromissos():
    print("\n--- LISTA DE COMPROMISSOS ---")

    compromissos = carregar_compromissos()

    if not compromissos:
        print("Nenhum compromisso cadastrado.")
        return

    for numero, compromisso in enumerate(compromissos, start=1):
        print(f"\nCompromisso {numero}")
        print(f"Título: {compromisso['titulo']}")
        print(f"Data: {compromisso['data']}")
        print(f"Horário: {compromisso['horario']}")
        print(f"Descrição: {compromisso['descricao']}")


def editar_compromisso():
    print("\n--- EDITAR COMPROMISSO ---")

    titulo_busca = input(
        "Digite o título do compromisso que deseja editar: "
    ).strip().lower()

    compromissos = carregar_compromissos()

    encontrados = [
        compromisso for compromisso in compromissos
        if compromisso["titulo"].lower() == titulo_busca
    ]

    if not encontrados:
        print("Compromisso não encontrado.")
        return

    if len(encontrados) > 1:
        print("Há mais de um compromisso com esse título.")
        print("Edição cancelada.")
        return

    compromisso = encontrados[0]

    print(f"Título atual: {compromisso['titulo']}")
    print(f"Data atual: {compromisso['data']}")
    print(f"Horário atual: {compromisso['horario']}")
    print(f"Descrição atual: {compromisso['descricao']}")

    novo_titulo = input(
        "Novo título (Enter para manter): "
    ).strip()

    nova_data = input(
        "Nova data (Enter para manter): "
    ).strip()

    novo_horario = input(
        "Novo horário (Enter para manter): "
    ).strip()

    nova_descricao = input(
        "Nova descrição (Enter para manter): "
    ).strip()

    if novo_titulo:
        compromisso["titulo"] = novo_titulo

    if nova_data:
        compromisso["data"] = nova_data

    if novo_horario:
        compromisso["horario"] = novo_horario

    if nova_descricao:
        compromisso["descricao"] = nova_descricao

    salvar_compromissos(compromissos)

    print("Compromisso atualizado com sucesso!")

   
def excluir_compromisso():
    print("\n--- EXCLUIR COMPROMISSO ---")

    titulo_busca = input(
        "Digite o título do compromisso que deseja excluir: "
    ).strip().lower()

    compromissos = carregar_compromissos()

    encontrados = [
        compromisso for compromisso in compromissos
        if compromisso["titulo"].lower() == titulo_busca
    ]

    if not encontrados:
        print("Compromisso não encontrado.")
        return

    if len(encontrados) > 1:
        print("Há mais de um compromisso com esse título.")
        print("Exclusão cancelada.")
        return

    compromisso = encontrados[0]
    compromissos.remove(compromisso)
    salvar_compromissos(compromissos)

    print("Compromisso excluído com sucesso!")
