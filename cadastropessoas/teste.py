from CadstroPessoas.Funcoes import *
from CadstroPessoas.ManipularArquivo import *

# Titulo
linha(15)
print('\033[1;36m', end='')
print(f'{"Cadastro De funcionário".title():^30}')
print('\033[0m', end='')
linha(15)
# Fucoes
while True:
    # menu
    print('''[1] Novo Cadastro\n[2] Ver Pessoas Cadastradas\n[3] Sair''')
    linha(15)
    usuario = leiaint('\033[1;36mEscolha uma opção:\033[0m ')
    # Novo Cadastro
    if usuario == 1:
        linha(20)
        print(f'\033[34m{"Novo Cadastro":^40}\033[m')
        nome = str(input('Nome: '.title())).strip()
        idade = str(input('Idade: '.upper())).strip()
        cpf = formatcpf('CPF: ').strip()
        tel = formattel('Tel: ').strip()
        email = str(input('Email: ')).strip()
        endereco = str(input('Endereço de residencia')).title().strip()
        cadastro(nome, idade, cpf, tel, email, endereco)
        linha(20)
        # Pessoas Cadastradas
    elif usuario == 2:
        linha(20)
        print(f'\033[34m{"Funcionarios Cadastrados".title():^40}\033[m')
        mostrarcadsatros()
        linha(20)
        # Encerar Programa
    elif usuario == 3:
        linha(20)
        print('\033[4;33mPrograma Encerrado Com Sucesso - Volte Sempre\033[0m')
        break
    else:
        print('\033[31mErro!- NÃO EXISTE ESSA OPÇÃO\033[m')
