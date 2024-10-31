# Gerenciamento de Livros

Um sistema simples de gerenciamento de livros em Python que permite adicionar, visualizar e remover livros, além de salvar os dados em um arquivo.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação utilizada para desenvolver o sistema.
- **Arquivo de Texto (db.txt)**: Utilizado para armazenar os nomes dos livros adicionados.

## Funcionalidades

1. **Adicionar Livro**: Permite ao usuário adicionar um novo livro à livraria e salvar o nome no arquivo `db.txt`.
2. **Visualizar Livros**: Exibe todos os livros atualmente na livraria.
3. **Remover Livro**: Permite ao usuário remover um livro da livraria com base na sua posição na lista.
4. **Ler Arquivo de Livros**: Lê e exibe os livros salvos no arquivo `db.txt`.
5. **Sair do Menu**: Finaliza o programa.

## Estrutura do Código

O código é dividido em várias funções para facilitar a leitura e a manutenção:

gerenciamento_livros(): Função principal que gerencia a interação com o usuário.
menu(): Exibe as opções disponíveis para o usuário.
adicionar_livro_arquivo(nome_livro): Adiciona um livro ao arquivo.
ler_arquivo(): Lê e exibe o conteúdo do arquivo de livros.

## Considerações Finais

Este projeto é um exemplo básico de como gerenciar dados em Python usando listas e arquivos de texto. Sinta-se à vontade para expandir e adicionar mais funcionalidades, como edição de livros, pesquisa, ou até mesmo integração com um banco de dados.
