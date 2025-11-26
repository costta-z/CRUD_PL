import os
os.system("cls || clear")

# CRUD usando lista.
# Create = criar / salvar
# Read = buscar / selecionar
# Update = atualizar / modificar
# Delete = excluir

# Criando uma lista.
lista_clientes = []

# CREATE
print("CREATE - Adicionar / Inserir")
nome = "Marta"
lista_clientes.append(nome)
print(f"O nome: {nome} foi inserido com sucesso!")

# READ
print("\nRead - ler / Mostrar")
print(lista_clientes)

# UPDATE
print("\nUpdate - Atualizar / Alterar")
nome_para_atualizar = "Marta"
if nome_para_atualizar in lista_clientes:
    novo_nome = "Marta Silva"
    indice = lista_clientes.index(nome_para_atualizar)
    lista_clientes[indice] = novo_nome
    print(f"O nome {nome_para_atualizar} foi atualizado para {novo_nome}")
else:
    print(f"O nome {nome_para_atualizar} não foi encontrado.")

print(lista_clientes)

# DELETE
print("\nDelete - Excluir / Remover")
nome_para_excluir = "Maria"
if nome_para_excluir in lista_clientes:
    lista_clientes.remove(nome_para_excluir)
    print(f"{nome_para_excluir} foi excluido com sucesso!")
else:
    print(f"O nome {nome_para_excluir} não foi encontrado.")

print(lista_clientes)