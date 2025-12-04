import os
import time
from dataclasses import dataclass

os.system("cls || clear")  # Limpa o terminal em Windows e Linux

lista_clientes = []
lista_produtos = []

@dataclass
class Produto:
    nome_produto: str
    quantidade: int
    lote: str
    validade: str

@dataclass
class Cliente:
    nome: str
    email: str
    telefone: str
    endereco: str

    def mostrar_dados(self):
        print(f"Nome: {self.nome} \nE-mail: {self.email} \nTelefone: {self.telefone}\nEndereço: {self.endereco}")

def lista_esta_vazia(lista):
    if not lista:
        print("\nNão há itens cadastrados.")
        return True
    return False

# Função para adicionar um novo cliente na lista
def adicionar_cliente(lista_clientes):
    print("\n--- Adicionar novo cliente ---")
    nome = input("Digite seu nome: ")
    email = input("Digite seu e-mail: ")
    telefone = input("Digite seu telefone: ")
    endereco = input("Digite seu endereço: ")

    novo_cliente = Cliente(nome=nome, email=email, telefone=telefone, endereco=endereco)
    lista_clientes.append(novo_cliente)
    print(f"\nCliente {nome} adicionado com sucesso!")

# Função para adicionar um novo produto na lista
def adicionar_produto(lista_produtos):
    print("\n--- Adicionar novo produto ---")
    nome_produto = input("Digite o nome do produto: ")
    quantidade = int(input("Digite a quantidade: "))
    lote = input("Digite o lote do produto: ")
    validade = input("Digite a validade do produto: ")

    novo_produto = Produto(nome_produto=nome_produto, quantidade=quantidade, lote=lote, validade=validade)
    lista_produtos.append(novo_produto)
    print(f"\nProduto {nome_produto} adicionado com sucesso!")

# Função para mostrar todos os clientes
def mostrar_todos_clientes(lista_clientes):
    if lista_esta_vazia(lista_clientes):
        return
    
    print("\n--- Lista de Clientes ---")
    for cliente in lista_clientes:
        cliente.mostrar_dados()

# Função para mostrar todos os produtos
def mostrar_todos_produtos(lista_produtos):
    if lista_esta_vazia(lista_produtos):
        return
    
    print("\n--- Lista de Produtos ---")
    for produto in lista_produtos:
        print(f"Nome: {produto.nome_produto} | Quantidade: {produto.quantidade} | Lote: {produto.lote} | Validade: {produto.validade}")

# Função para encontrar cliente pelo nome
def encontrar_cliente_por_nome(lista_clientes, nome_buscar):
    nome_buscar_lower = nome_buscar.lower()
    for cliente in lista_clientes:
        if cliente.nome.lower() == nome_buscar_lower:
            return cliente
    return None

# Função para encontrar produto pelo nome
def encontrar_produto_por_nome(lista_produtos, nome_produto_buscar):
    nome_produto_buscar_lower = nome_produto_buscar.lower()
    for produto in lista_produtos:
        if produto.nome_produto.lower() == nome_produto_buscar_lower:
            return produto
    return None

# Função para atualizar os dados de um cliente
def atualizar_cliente(lista_clientes):
    if lista_esta_vazia(lista_clientes):
        return
    
    mostrar_todos_clientes(lista_clientes)
    nome_buscar = input("\nDigite o nome do cliente para atualizar: ")
    cliente_para_atualizar = encontrar_cliente_por_nome(lista_clientes, nome_buscar)

    if cliente_para_atualizar:
        print("\nCliente encontrado.")
        print("\nDigite os novos dados ou deixe em branco para manter os valores atuais.")

        novo_nome = input(f"Novo nome (atual: {cliente_para_atualizar.nome}): ")
        if novo_nome:
            cliente_para_atualizar.nome = novo_nome
        
        novo_email = input(f"Novo e-mail (atual: {cliente_para_atualizar.email}): ")
        if novo_email:
            cliente_para_atualizar.email = novo_email
        
        novo_telefone = input(f"Novo telefone (atual: {cliente_para_atualizar.telefone}): ")
        if novo_telefone:
            cliente_para_atualizar.telefone = novo_telefone
        
        novo_endereco = input(f"Novo endereço (atual: {cliente_para_atualizar.endereco}): ")
        if novo_endereco:
            cliente_para_atualizar.endereco = novo_endereco
        
        print(f"\nDados do cliente {cliente_para_atualizar.nome} atualizados com sucesso!")
    else:
        print(f"\nCliente com nome {nome_buscar} não encontrado.")

# Função para atualizar os dados de um produto
def atualizar_produto(lista_produtos):
    if lista_esta_vazia(lista_produtos):
        return
    
    mostrar_todos_produtos(lista_produtos)
    nome_produto_buscar = input("\nDigite o nome do produto para atualizar: ")
    produto_para_atualizar = encontrar_produto_por_nome(lista_produtos, nome_produto_buscar)

    if produto_para_atualizar:
        print("\nProduto encontrado.")
        print("\nDigite os novos dados ou deixe em branco para manter os valores atuais.")

        novo_nome_produto = input(f"Novo nome (atual: {produto_para_atualizar.nome_produto}): ")
        if novo_nome_produto:
            produto_para_atualizar.nome_produto = novo_nome_produto
        
        nova_quantidade = input(f"Nova quantidade (atual: {produto_para_atualizar.quantidade}): ")
        if nova_quantidade:
            produto_para_atualizar.quantidade = int(nova_quantidade)
        
        novo_lote = input(f"Novo lote (atual: {produto_para_atualizar.lote}): ")
        if novo_lote:
            produto_para_atualizar.lote = novo_lote
        
        nova_validade = input(f"Nova validade (atual: {produto_para_atualizar.validade}): ")
        if nova_validade:
            produto_para_atualizar.validade = nova_validade
        
        print(f"\nDados do produto {produto_para_atualizar.nome_produto} atualizados com sucesso!")
    else:
        print(f"\nProduto com nome {nome_produto_buscar} não encontrado.")

# Função para excluir um cliente
def excluir_cliente(lista_clientes):
    if lista_esta_vazia(lista_clientes):
        return
    
    mostrar_todos_clientes(lista_clientes)
    nome_buscar = input("\nDigite o nome do cliente para excluir: ")
    cliente_para_remover = encontrar_cliente_por_nome(lista_clientes, nome_buscar)

    if cliente_para_remover:
        lista_clientes.remove(cliente_para_remover)
        print(f"\nCliente {cliente_para_remover.nome} excluído com sucesso!")
    else:
        print(f"\nCliente com nome {nome_buscar} não encontrado.")

# Função para excluir um produto
def excluir_produto(lista_produtos):
    if lista_esta_vazia(lista_produtos):
        return
    
    mostrar_todos_produtos(lista_produtos)
    nome_produto_buscar = input("\nDigite o nome do produto para excluir: ")
    produto_para_remover = encontrar_produto_por_nome(lista_produtos, nome_produto_buscar)

    if produto_para_remover:
        lista_produtos.remove(produto_para_remover)
        print(f"\nProduto {produto_para_remover.nome_produto} excluído com sucesso!")
    else:
        print(f"\nProduto com nome {nome_produto_buscar} não encontrado.")

# Menu de opções
while True:
    print("""
--- Gerenciador de Clientes e Produtos ---
1 - Adicionar Cliente
2 - Mostrar Todos os Clientes
3 - Atualizar Cliente
4 - Excluir Cliente
5 - Adicionar Produto
6 - Mostrar Todos os Produtos
7 - Atualizar Produto
8 - Excluir Produto
0 - Sair
           """)
    
    try:
        opcao = int(input("Escolha uma opção: "))
    except ValueError:
        print("\nEntrada inválida. Tente novamente.")
        time.sleep(2)
        os.system("cls || clear")
        continue

    match opcao:
        case 1:
            adicionar_cliente(lista_clientes)
        case 2:
            mostrar_todos_clientes(lista_clientes)
        case 3:
            atualizar_cliente(lista_clientes)
        case 4:
            excluir_cliente(lista_clientes)
        case 5:
            adicionar_produto(lista_produtos)
        case 6:
            mostrar_todos_produtos(lista_produtos)
        case 7:
            atualizar_produto(lista_produtos)
        case 8:
            excluir_produto(lista_produtos)
        case 0:
            print("\nSaindo do programa...")
            break
        case _:
            print("\nOpção inválida. Tente novamente.")

    if opcao != 1 and opcao != 0:
        time.sleep(4)
    elif opcao == 1:
        time.sleep(1)

    # Limpa tela.
    if opcao != 0:
        os.system("cls || clear")
