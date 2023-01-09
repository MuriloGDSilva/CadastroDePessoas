def linha(tam):
    print('_-'*tam)


def leiaint(msg):
    while True:
        try:
            valor = int(input(msg))
        except(ValueError,TypeError):
            linha(15)
            print('\033[31mERRO!- DIGITE SOMENTE NÚMEROS INTEIROS\033[0m')
            linha(15)
            continue
        else:
            return valor

def formatcpf(cpf):
    dado = str(input(cpf))
    return f'{dado[:3]}.{dado[3:6]}.{dado[6:9]}-{dado[9:]}'


def formattel(tel):
    dado = str(input(tel))
    return f'{dado[0:5]}-{dado[5:]}'