from chamados import abrir_chamado, listar_chamados, consultar_chamado, alterar_status
def menu():
    while True:
        print("===== CONTROLE DE CHAMADOS =====")
        print("1 - Abrir chamado")
        print("2 - Listar chamados")
        print("3 - Consultar chamado")
        print("4 - Alterar status")
        print("5 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            abrir_chamado()
        elif opcao == "2":
            listar_chamados()
        elif opcao == "3":
            consultar_chamado()
        elif opcao == "4":
            alterar_status()
        elif opcao == "5":
            print("programa encerrado")
            break
        else:
            print("Opção inválida. Tente novamente.")

menu()
    

    