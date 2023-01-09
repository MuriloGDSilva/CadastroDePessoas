# Criar novo arquivo/Cdastrar funcionario
def cadastro(nome='xxxx',idade='xxxx',cpf='xxxx',tel='xxxxx-xxxx',email='xxxx',endereco='xxxxx'):
    try:
        arquivo = open('Funcionarios.txt','at+')
        arquivo.write(f'\033[1mNome:\033[m{nome} {idade} Anos \033[1mCPF:\033[m {cpf} \n'
                      f'\033[1mTel:\033[m (11){tel} \033[1mEmail\033[m: {email} \033[1mEndereço:\033[m {endereco}\n\033[m')
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