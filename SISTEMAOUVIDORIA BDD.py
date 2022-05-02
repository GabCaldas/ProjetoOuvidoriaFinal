#LEMBRAR DE INSTALAR O PYMYSQL PARA QUE O PROGRAMA FUNCIONE
import pymysql
conexao = pymysql.connect(
    host='us-cdbr-east-05.cleardb.net',
    user='b075754281f6a0',
    password='3b62b67b',
    database='heroku_664795534a5f4fa')
class Protocolo:
    codigo = 0
    requisitante = ''
    tipo = ''
    descricao = ''

x="SISTEMA DE OUVIDORIA ABC"

alinhado=x.center(60)

listaProtocolo = []

listaSugestao = []

listaReclamacao = []

listaElogio = []

opcao = 0

while opcao != 7:
    print("=" * 60)
    print(alinhado)
    print("=" * 60)
    print(f"""                1) Listar manifestações
                2) Listar sugestões
                3) Listar reclamações
                4) Listar elogios
                5) Enviar uma manifestação 
                6) Pesquisar protocolo por número
                7) Sair do programa""")
    print("=" * 60)
    opcao = input('Digite a opção desejada: ')
    if opcao in '1234567':
        opcao = int(opcao)
    else:
        print('* ENTRADA INVÁLIDA *  Por favor digite uma opção válida (de 1 a 7) ')
        continue

    if opcao == 1:
        print('=' * 60)
        if listaProtocolo == []:
            print('Você não tem manifestações registradas!')
        else:
            print('Essas são todas as manifestações')
            print("")
            for i in listaProtocolo:
                print(' Protocolo:', i.codigo, '\n Requisitante:', i.requisitante, '\n Tipo:', i.tipo, '\n Descrição:', i.descricao)
                print()

    elif opcao == 2:
        print('=' * 60)
        if listaSugestao == []:
            print('Você não tem sugestões registradas!')
        else:
            print('Essas são todas as sugestões: ')
            for i in listaSugestao:
                print(' Código:', i.codigo, '\n Requisitante:', i.requisitante, '\n Descrição:', i.descricao)
                print()

    elif opcao == 3:
        print('=' * 60)
        if listaReclamacao == []:
            print('Você não tem reclamações registradas!')
        else:
            print('Essas são todas as reclamações: ')
            for i in listaReclamacao:
                print(' Código:', i.codigo, '\n Requisitante:', i.requisitante, '\n Descrição:', i.descricao)
                print()

    elif opcao == 4:
        print('=' * 60)
        if listaElogio == []:
            print('Você não tem elogios registrados!')
        else:
            print('Essas são todos os elogios: ')
            for i in listaElogio:
                print(' Protocolo:', i.codigo, '\n Requisitante:', i.requisitante, '\n Tipo:', i.tipo, '\n Descrição:', i.descricao)
                print()

    elif opcao == 5:
        print('=' * 60)
        print('Criando uma nova manifestação')
        print('=' * 60)
        requisitante = input('Digite seu nome: ').capitalize()
        print('=' * 60)
        bool = True
        while bool:
            tipo = input(f'Olá {requisitante}! Qual tipo de manifestação você quer enviar? \n1) RECLAMAÇÃO \n2) SUGESTÃO \n3) ELOGIO \nDigite o número correspondente: ')
            print('=' * 60)
            if tipo in '123':
                tipo = int(tipo)
            else:
                print('* ENTRADA INVÁLIDA *  Por favor digite uma opção válida (1, 2 ou 3) ')
                continue

            if tipo >= 1 and tipo <= 3:
                bool = False
            else:
                print('* ENTRADA INVÁLIDA *  Por favor digite uma opção válida (1, 2 ou 3) ')

        if tipo == 1:
            tipo = 'Reclamação'
            codigo = len(listaProtocolo) + 1
            descricao=str(input("Digite a descrição da sua reclamação: "))
            print('=' * 60)
            print(f"Sua reclamação foi listada com sucesso {requisitante}! \nO número do seu protocolo é {codigo}")

            sql = f"""INSERT INTO tb_manifestos_caldas (nome_cliente,tipo_manifest,descricao) 
                                        values('{requisitante}', '{tipo}', '{descricao}'
                                        )"""
            cursor = conexao.cursor()
            cursor.execute(sql)
            conexao.commit()
        elif tipo == 2:
            tipo = 'Sugestão'
            codigo = len(listaProtocolo) + 1
            descricao = str(input("Digite a descrição da sua sugestão: "))
            print('=' * 60)
            print(f"Sua sugestão foi listada com sucesso {requisitante}! \nO número do seu protocolo é {codigo}")
            sql2 = f"""INSERT INTO tb_manifestos_caldas (nome_cliente,tipo_manifest,descricao) 
                                                    values('{requisitante}', '{tipo}', '{descricao}'
                                                    )"""
            cursor = conexao.cursor()
            cursor.execute(sql2)
            conexao.commit()
        elif tipo == 3:
            tipo = 'Elogio'
            codigo = len(listaProtocolo) + 1
            descricao = str(input("Digite a descrição do seu elogio: "))
            print(f"Obrigado! {requisitante}!\n O número do seu protocolo é {codigo}")
            sql3 = f"""INSERT INTO tb_manifestos_caldas (nome_cliente,tipo_manifest,descricao) 
                                                    values('{requisitante}', '{tipo}', '{descricao}'
                                                    )"""
            cursor = conexao.cursor()
            cursor.execute(sql3)
            conexao.commit()



        novoProtocolo = Protocolo()
        novoProtocolo.codigo = codigo
        novoProtocolo.requisitante = requisitante
        novoProtocolo.tipo = tipo
        novoProtocolo.descricao = descricao

        listaProtocolo.append(novoProtocolo)

        if tipo == 'Reclamação':
            listaReclamacao.append(novoProtocolo)
        elif tipo == 'Sugestão':
            listaSugestao.append(novoProtocolo)
        else:
            listaElogio.append(novoProtocolo)


    elif opcao == 6:

        listaQuantidade = []

        for i in range(len(listaProtocolo)):
            listaQuantidade.append(i + 1)
        print('=' * 60)
        print('Pesquise um protocolo pelo código')
        print('=' * 60)

        bool = True

        while bool:

            pesquisa = input('Digite o número do código desejado: ')
            print('=' * 60)
            if pesquisa in '0123456789':

                pesquisa = int(pesquisa)

            else:

                print(

                    '* ENTRADA INVÁLIDA *  Por favor digite uma opção de protocolo existente \n Protocolos existentes:',

                    listaQuantidade)

                continue

            if pesquisa in listaQuantidade:

                bool = False

            else:

                print(

                    '* ENTRADA INVÁLIDA *  Por favor digite uma opção de protocolo existente \n Protocolos existentes:',

                    listaQuantidade)

        protocoloPesquisado = listaProtocolo[pesquisa - 1]
        if protocoloPesquisado not in listaProtocolo:
            print(" Não existem protocolos no momento! ")

        print('Protocolo encontrado!')

        codigo = protocoloPesquisado.codigo

        requisitante = protocoloPesquisado.requisitante

        tipo = protocoloPesquisado.tipo

        descricao = protocoloPesquisado.descricao

        print(' Protocolo:', codigo, '\n Requisitante:', requisitante, '\n Tipo:', tipo, '\n Descrição:', descricao)
