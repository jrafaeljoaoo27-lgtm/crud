tarefas = []

# Criando 10 tarefas iniciais automaticamente
for i in range(1, 11):
    tarefas.append({
        "id": i,
        "nome": f"Tarefa {i}",
        "status": "Em andamento"
    })


def mostrar_tarefas():
    print("\n===== LISTA DE TAREFAS =====")

    if len(tarefas) == 0:
        print("Nenhuma tarefa cadastrada.")
    else:
        for tarefa in tarefas:
            print(
                f"ID: {tarefa['id']} | "
                f"Nome: {tarefa['nome']} | "
                f"Status: {tarefa['status']}"
            )

    print("============================\n")


while True:
    print("===== MENU =====")
    print("1 - Criar tarefa")
    print("2 - Atualizar tarefa")
    print("3 - Deletar tarefa")
    print("4 - Reiniciar sistema")
    print("5 - Ver tarefas")
    print("================")

    opcao = input("Escolha uma opção: ")

    # CRIAR TAREFA
    if opcao == "1":

        try:
            novo_id = int(input("Digite o ID da tarefa: "))

            # Verifica se o ID já existe
            existe = False

            for tarefa in tarefas:
                if tarefa["id"] == novo_id:
                    existe = True
                    break

            if existe:
                print("Esse ID já existe!")

            else:
                nome = input("Digite o nome da tarefa: ")
                status = input("Digite o status: ")

                tarefas.append({
                    "id": novo_id,
                    "nome": nome,
                    "status": status
                })

                print("Tarefa criada com sucesso!")

        except ValueError:
            print("Digite um ID válido!")

    # ATUALIZANDO TAREFA
    elif opcao == "2":

        try:
            id_tarefa = int(input("Digite o ID da tarefa: "))

            encontrada = False

            for tarefa in tarefas:

                if tarefa["id"] == id_tarefa:

                    novo_nome = input("Novo nome: ")
                    novo_status = input("Novo status: ")

                    tarefa["nome"] = novo_nome
                    tarefa["status"] = novo_status

                    encontrada = True

                    print("Tarefa atualizada com sucesso!")
                    break

            if not encontrada:
                print("ID não encontrado!")

        except ValueError:
            print("Digite um ID válido!")

    # DELETAR TAREFA
    elif opcao == "3":

        try:
            id_tarefa = int(input("Digite o ID da tarefa: "))

            encontrada = False

            for tarefa in tarefas:

                if tarefa["id"] == id_tarefa:
                    tarefas.remove(tarefa)
                    encontrada = True

                    print("Tarefa deletada com sucesso!")
                    break

            if not encontrada:
                print("ID não encontrado!")

        except ValueError:
            print("Digite um ID válido!")

    # REINICIANDO SISTEMA
    elif opcao == "4":

        print("\nReiniciando sistema...\n")

        tarefas = []

        for i in range(1, 11):
            tarefas.append({
                "id": i,
                "nome": f"Tarefa {i}",
                "status": "Em andamento"
            })

    # MOSTRANDO AS TASKS
    elif opcao == "5":
        mostrar_tarefas()

    else:
        print("Opção inválida!")
