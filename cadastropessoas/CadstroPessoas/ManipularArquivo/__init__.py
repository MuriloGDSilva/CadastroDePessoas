# Criar novo arquivo/Cdastrar funcionario
def cadastro(nome='xxxx',idade='xxxx',cpf='xxxx',tel='xxxxx-xxxx',email='xxxx',endereco='xxxxx'):
    try:
        arquivo = open('Funcionarios.txt','at+')
        arquivo.write(f'\nId:{tamanho_arquivo()} Nome:{nome} {idade} Anos CPF:{cpf} \n'
                      f'Tel: (11){tel} Email: {email} Endereço:{endereco}\n')
    except:
        print('ERRO!!')
    else:
        print('Sucesso!!')
        arquivo.close()

def mostrarcadsatros(nome=''):
    try:
        arquivo = open('Funcionarios.txt','rt')
        print(arquivo.read())

    except:
        print('Erro!! NÃO HA FUNCIONARIOS CADASTRADOS NESSE ARQUIVO')

    else:
        arquivo.close()

def gerador_id(arq=''):
    arquivo = open('Funcionarios.txt')
    tq = arquivo.readlines()
    return len(tq)
