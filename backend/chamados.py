chamados = []

def abrir_chamado():
    nome = input("Digite o nome do solicitante: ")
    descricao = input("Digite a descrição do problema: ")
    print("Categorias disponíveis:")
    print("1 - Hardware")
    print("2 - Software")
    print("3 - Acesso")
    print("4 - Outro")
    categoria = input("Digite a categoria do chamado: ")

    status = "Aberto"

    if categoria == "1":
        categoria = "Hardware"
    elif categoria == "2":
        categoria = "Software"
    elif categoria == "3":
        categoria = "Acesso"
    elif categoria == "4":
        categoria = "Outro"
    else:
        print("Categoria inválida. Chamado não registrado.")
        return
    chamado = {
        "id": len(chamados) + 1,
        "nome": nome,
        "descricao": descricao,
        "categoria": categoria,
        "status": status
    }
    chamados.append(chamado)
    print(f"ID: {chamado['id']}")
    print(f"Nome: {chamado['nome']}")
    print(f"Descrição: {chamado['descricao']}")
    print(f"Categoria: {chamado['categoria']}")
    print(f"Status: {chamado['status']}")
    print("Chamado aberto com sucesso!")

def listar_chamados():
    print("===== LISTA DE CHAMADOS =====")
    if not chamados:
        print("Nenhum chamado registrado.")
    else:
        for chamado in chamados:
            print(f"ID: {chamado['id']}, Nome: {chamado['nome']}, Categoria: {chamado['categoria']}, Status: {chamado['status']}")

def consultar_chamado():
    print("===== CONSULTAR CHAMADO =====")
    id_chamado = int(input("Digite o ID do chamado: "))
    for chamado in chamados:
        if chamado["id"] == id_chamado:
            print(f"ID: {chamado['id']}")
            print(f"Nome: {chamado['nome']}")
            print(f"Descrição: {chamado['descricao']}")
            print(f"Categoria: {chamado['categoria']}")
            print(f"Status: {chamado['status']}")
            return
        print("Chamado não encontrado.")

def alterar_status():
    print("===== ALTERAR STATUS DO CHAMADO =====")
    id_chamado = int(input("Digite o ID do chamado: "))
    chamado_encontrado = False  
    while True:
        for chamado in chamados:
            if chamado["id"] == id_chamado:
                print("Status disponíveis:")
                print("1 - Em andamento")
                print("2 - Resolvido")
                print("3 - Cancelado")
                print("4 - Voltar")
                novo_status = int(input("Digite o novo status do chamado: "))
                if novo_status == 1:
                    novo_status = "Em andamento"
                elif novo_status == 2:
                    novo_status = "Resolvido"
                elif novo_status == 3:
                    novo_status = "Cancelado"
                elif novo_status == 4:
                    return
                else:
                    print("Status inválido. Tente novamente.")
                    continue
                chamado["status"] = novo_status
                print("Status do chamado alterado com sucesso!")
                chamado_encontrado = True
                return
        if not chamado_encontrado:
            print("Chamado não encontrado.")
