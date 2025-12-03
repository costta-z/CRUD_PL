import os
import time
from dataclasses import dataclass
os.system("cls || clear")  # Limpa o terminal em Windows e Linux

lista_alunos = []

@dataclass
class Endereco:
    estado: str
    cidade: str
    logadouro: str
    numero: int

@dataclass
class Aluno:
    nome: str
    data_nascimento: str
    r_a: str
    curso: str
    endereco: Endereco

    def mostrar_dados(self):
        endereco_str = f"{self.endereco.logadouro}, {self.endereco.numero} - {self.endereco.cidade}/{self.endereco.estado}"
        print(f"Nome: {self.nome}\nData de nascimento: {self.data_nascimento}\nR.A: {self.r_a}\nCurso: {self.curso}\nEndereço: {endereco_str}")

def lista_esta_vazia(lista_alunos):
    if not lista_alunos:
        print("\nNão há alunos cadastrados.")
        return True
    return False

def adicionar_aluno(lista_alunos):
    print("\n--- Adicionar novo aluno ---")
    nome = input("Digite seu nome: ")
    data_nascimento = input("Digite sua data de nascimento: ")
    r_a = input("Digite seu R.A: ")
    curso = input("Digite seu curso: ")
    estado = input("Digite seu estado: ")
    cidade = input("Digite sua cidade: ")
    logadouro = input("Digite seu logadouro: ")
    numero = int(input("Digite o número da sua residência: "))

    endereco = Endereco(estado=estado, cidade=cidade, logadouro=logadouro, numero=numero)
    novo_aluno = Aluno(nome=nome, data_nascimento=data_nascimento, r_a=r_a, curso=curso, endereco=endereco)
    lista_alunos.append(novo_aluno)
    print(f"\naluno {nome} adicionado com sucesso!")

def encontrar_aluno_por_nome(lista_alunos, nome_buscar):
    nome_buscar_lower = nome_buscar.lower()
    for aluno in lista_alunos:
        if aluno.nome.lower() == nome_buscar_lower:
            return aluno
    return None

def mostrar_todos_alunos(lista_alunos):
    if lista_esta_vazia(lista_alunos):
        return
    
    print("\n--- Lista de alunos ---")
    for aluno in lista_alunos:
        aluno.mostrar_dados()

def atualizar_alunos(lista_alunos):
    if lista_esta_vazia(lista_alunos):
        return

    mostrar_todos_alunos(lista_alunos)
    print("--- Atualizar dados do aluno ---")
    nome_buscar = input("\nDigite o nome do aluno: ")
    aluno_para_atualizar = encontrar_aluno_por_nome(lista_alunos, nome_buscar)

    if aluno_para_atualizar:
        print("\nPessoa encontrada.")
        print("\nDigite os novos dados ou deixe em branco para manter o valor atual.")
        
        # Inicializando as variáveis com os valores atuais
        novo_nome = aluno_para_atualizar.nome
        novo_data_nascimento = aluno_para_atualizar.data_nascimento
        novo_r_a = aluno_para_atualizar.r_a
        novo_curso = aluno_para_atualizar.curso
        novo_estado = aluno_para_atualizar.endereco.estado
        novo_cidade = aluno_para_atualizar.endereco.cidade
        novo_logadouro = aluno_para_atualizar.endereco.logadouro
        novo_numero = aluno_para_atualizar.endereco.numero

        # Atualizando os dados, se o usuário quiser
        novo_nome_input = input(f"Nome atual: {novo_nome}\nNovo nome: ")
        if novo_nome_input:
            novo_nome = novo_nome_input

        novo_data_nascimento_input = input(f"Data de nascimento atual: {novo_data_nascimento}\nNova data de nascimento: ")
        if novo_data_nascimento_input:
            novo_data_nascimento = novo_data_nascimento_input

        novo_r_a_input = input(f"R.A. atual: {novo_r_a}\nNovo R.A: ")
        if novo_r_a_input:
            novo_r_a = novo_r_a_input

        novo_curso_input = input(f"Curso atual: {novo_curso}\nNovo curso: ")
        if novo_curso_input:
            novo_curso = novo_curso_input

        novo_estado_input = input(f"Estado atual: {novo_estado}\nNovo Estado: ")
        if novo_estado_input:
            novo_estado = novo_estado_input

        novo_cidade_input = input(f"Cidade atual: {novo_cidade}\nNova cidade: ")
        if novo_cidade_input:
            novo_cidade = novo_cidade_input

        novo_logadouro_input = input(f"Logadouro atual: {novo_logadouro}\nNovo logadouro: ")
        if novo_logadouro_input:
            novo_logadouro = novo_logadouro_input

        novo_numero_input = input(f"Número atual: {novo_numero}\nNovo número: ")
        if novo_numero_input:
            novo_numero = int(novo_numero_input)

        # Atualizando o objeto aluno
        aluno_para_atualizar.nome = novo_nome
        aluno_para_atualizar.data_nascimento = novo_data_nascimento
        aluno_para_atualizar.r_a = novo_r_a
        aluno_para_atualizar.curso = novo_curso
        aluno_para_atualizar.endereco.estado = novo_estado
        aluno_para_atualizar.endereco.cidade = novo_cidade
        aluno_para_atualizar.endereco.logadouro = novo_logadouro
        aluno_para_atualizar.endereco.numero = novo_numero

        print(f"\nDados do aluno {nome_buscar} atualizados com sucesso!")
    else:
        print(f"\nAluno com nome {nome_buscar} não encontrado.")

def excluir_aluno(lista_alunos):
    if lista_esta_vazia(lista_alunos):
        return
    
    mostrar_todos_alunos(lista_alunos)

    nome_buscar = input("\nDigite o nome do aluno que deseja excluir: ")
    aluno_para_remover = encontrar_aluno_por_nome(lista_alunos, nome_buscar)

    if aluno_para_remover:
        lista_alunos.remove(aluno_para_remover)
        print(f"\nAluno: {aluno_para_remover.nome} excluído com sucesso.")
    else:
        print(f"\nAluno com nome {nome_buscar} não encontrado.")

# Mostrando menu.
while True:
    print("""
--- Gerenciador de alunos ---
1 - Adicionar
2 - Mostrar todos
3 - Atualizar
4 - Excluir
0 - Sair
           """)
    
    try:
        opcao = int(input("Digite uma das opções acima: "))
    except ValueError:
        print("\nEntrada inválida. Digite um número...")
        time.sleep(2)
        os.system("cls || clear")
        continue

    match opcao:
        case 1:
            adicionar_aluno(lista_alunos)
        case 2:
            mostrar_todos_alunos(lista_alunos)
        case 3:
            atualizar_alunos(lista_alunos)
        case 4:
            excluir_aluno(lista_alunos)
        case 0:
            print("\nSaindo do programa...")
            break
        case _:
            print("\nOpção inválida. Tente novamente.")

    if opcao != 1 and opcao != 0:
        time.sleep(4)
    elif opcao == 1:
        time.sleep(1)

    if opcao != 0:
        os.system("cls || clear")
