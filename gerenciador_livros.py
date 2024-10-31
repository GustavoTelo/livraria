def gerenciamento_livros():
    livraria = []

    # Cria o arquivo db.txt se ele não existir
    with open('db.txt', 'a') as file:
        pass

    def menu():
        print('Escolha uma opção:')
        print('1. Adicionar livro')
        print('2. Visualizar livros')
        print('3. Remover livro')
        print('4. Ler arquivo de livros')
        print('5. Sair do menu')

    def adicionar_livro_arquivo(nome_livro):
        with open('db.txt', 'a') as file:
            file.write(nome_livro + '\n')

    def ler_arquivo():
        print("\nLivros no arquivo:")
        with open('db.txt', 'r') as file:
            conteudo = file.read()
            if conteudo:
                print(conteudo)
            else:
                print("Nenhum livro no arquivo.")
        print()

    print('BEM-VINDO À LIVRARIA!')

    escolha = 0
    while escolha != 5:
        menu()
        escolha = int(input('Qual a sua escolha: '))
        
        if escolha == 1:
            nome_livro = input('Qual o nome do livro? ')
            livraria.append(nome_livro)
            adicionar_livro_arquivo(nome_livro)
            print(f"Sucesso! '{nome_livro}' foi adicionado à sessão de livros e ao arquivo.")
        elif escolha == 2:
            print("Livros na livraria:", livraria)
        elif escolha == 3:
            if livraria:
                numero_livro = int(input('Qual o número do livro para remover? '))
                if 0 <= numero_livro < len(livraria):
                    removido = livraria.pop(numero_livro)
                    print(f"'{removido}' foi removido da sessão de livros.")
                else:
                    print("Número inválido.")
            else:
                print("Não há livros para remover.")
        elif escolha == 4:
            ler_arquivo()
        elif escolha == 5:
            print("Saindo do menu...")
        else:
            print("Escolha inválida, tente novamente.")

# Chamando a função para iniciar o programa
gerenciamento_livros()
