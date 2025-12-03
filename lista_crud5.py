import os
import time
from dataclasses import dataclass
os.system("cls || clear") # Limpa o terminal em Windows e Linux

lista_funcionarios = []

@dataclass
class Funcionario:
    # Aributos da classe.
    # Atributos são variáveis que pertecem à classe.
    nome: str
    data_nascimento: str
    cpf: str
    funcao: str

    #Método para mostrar as informações dos clientes.
    # Método é o nome dado a uma função que pertence á classe.
    def mostrar_dados(self):
        print(f"Nome: {self.nome} \nData de nascimento: {self.data_nascimento} \nCPF: {self.cpf}\nFunção: {self.funcao}")


# Função para verificar se a lista está vazia.
def lista_esta_vazia(lista_funcionarios):
    if not lista_funcionarios:
        print("\nNão há funcionários cadstrados.")
        return True
    return False

# Função para adicionar um novo cliente na lista.
def adicionar_funcionario(lista_funcionario):
    print("\n--- Adicionar novo funcionário ---")
    nome = input("Digite seu nome: ")
    data_nascimento = input("Digite sua data de nascimento: ")
    cpf = input("Digite seu CPF: ")
    funcao = input("Digite sua função: ")

    novo_funcionario = Funcionario(nome=nome, data_nascimento=data_nascimento, cpf=cpf, funcao=funcao)
    lista_funcionarios.append(novo_funcionario)
    print(f"\nFuncionário {nome} adicionado com sucesso!")

# Função para encontrar um cliente na lista.
def encontrar_funcionario_por_nome(lista_funcionarios, nome_buscar):
    nome_buscar_lower = nome_buscar.lower()
    for cliente in lista_funcionarios:
        if cliente.nome.lower() == nome_buscar_lower:
            return cliente
    return None # None significa retornar vazio, sem conteúdo.

# Função para mostrar todos os clientes.
def mostrar_todos_funcionarios(lista_funcionarios):
    if lista_esta_vazia(lista_funcionarios):
        return
    
    print("\n--- Lista de funcionários ---")
    for funcionario in lista_funcionarios:
        funcionario.mostrar_dados()

# Função para atualizar clientes.
def atualizar_funcionarios(lista_funcionarios):
    if lista_esta_vazia(lista_funcionarios):
        return
    
    # Mostrara a lista para ajudar o usuário
    mostrar_todos_funcionarios(lista_funcionarios)
    print("--- Atualizar dados do funcionário ---")
    nome_buscar = input("\nDigite o nome do funcionário: ")
    funcionario_para_atualizar = encontrar_funcionario_por_nome(lista_funcionarios, nome_buscar)

    if funcionario_para_atualizar:
        print("\nPessoa encontrada.")
        print("\nDigite os novos dados ou deixe para manter em branco para manter o valor atual.")

        print(f"Nome atual: {funcionario_para_atualizar.nome}")
        novo_nome = input("Novo nome: ")

        print(f"Data de nascimeto atual: {funcionario_para_atualizar.data_nascimento}")
        novo_data_nascimento = input("Novo data_nascimento: ")

        print(f"CPF atual: {funcionario_para_atualizar.cpf}")
        novo_cpf= input("Novo CPF: ")

        print(f"Função atual: {funcionario_para_atualizar.funcao}")
        novo_funcao = input("Nova função: ")

        if novo_nome:
            funcionario_para_atualizar.nome = novo_nome
        if novo_nome:
            funcionario_para_atualizar.data_nascimento = novo_data_nascimento
        if novo_nome:
            funcionario_para_atualizar.cpf = novo_cpf
        if novo_nome:
            funcionario_para_atualizar.funcao = novo_funcao

        print(f"\nDados do cliente: {nome_buscar} atualizados com sucesso!")
    else:
        print(f"\nCliente com nome: {nome_buscar} não encontrado.")

# Função para excluir um cliente.
def excluir_funcionario(lista_funcionarios):
    if lista_esta_vazia(lista_funcionarios):
        return
    
    mostrar_todos_funcionarios(lista_funcionarios)

    nome_buscar = input("\nDigite o nome do funcionário que deseja excluir: ")

    funcionario_para_remover = encontrar_funcionario_por_nome(lista_funcionarios, nome_buscar)

    if funcionario_para_remover:
        lista_funcionarios.remove(funcionario_para_remover)
        print(f"\nFuncionário: {funcionario_para_remover.nome} excluido com sucesso.")
    else:
        print(f"\nFuncionário com o nome {nome_buscar} não encontrado.")


# Mostrando menu.
while True:
    print("""
--- Gerenciardor funcionários ---
1 - Adicionar
2 - Mostrar todos
3 - Atualizar
4 - Excluir
0 - Sair
           """)
    
    # Evitando erros no programa.
    # Caso o usuário digite letras.
    try:
        opcao = int(input("Digite uma das opções acima: "))
    except ValueError:
        print("\nEntrada inválida. Digite um número...")
        time.sleep(2)
        os.system("cls || clear")
        continue

    match opcao:
        case 1:
            adicionar_funcionario(lista_funcionarios)
        case 2:
            mostrar_todos_funcionarios(lista_funcionarios)
        case 3:
            atualizar_funcionarios(lista_funcionarios)
        case 4:
            excluir_funcionario(lista_funcionarios)
        case 0:
            print("\nSaindo do programa...")
            break
        case _:
            print("\nOpção inválida. \nTente novamente.")

# Pausa antes de mudar o menu.
    if opcao != 1 and opcao != 0:
        time.sleep(4)
    elif opcao == 1:
        time.sleep(1)

    # Limpa tela.
    if opcao != 0:
        os.system("cls || clear")