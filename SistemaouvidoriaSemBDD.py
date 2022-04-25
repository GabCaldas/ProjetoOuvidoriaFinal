#LISTAS UTILIZADAS!
manifest = []
suges = []
reclama = []
elogio = []


#FUNÇÃO PARA LISTAR MANIFESTAÇÕES
def opcao1():
    if manifest == []:
        print("Não existem manifestações feitas!")
    else:
        print("Essas são suas manifestações")
        print("")
        for mani in range(len(manifest)):
            print(
            f" Protocolo: {manifest[mani][0]} \n Requisitante: {manifest[mani][1]} \n Tipo: {manifest[mani][2]} \n Descrição: {manifest[mani][3]}")
            print("")
#FUNÇÃO PARA LISTAR APENAS SUGESTÕES
def opcao2():
    if suges == []:
        print("Não existem sugestões feitas!")
    else:
        print("Essas são suas sugestões")
        for sugi in range(len(suges)):
            print(f" Protocolo: {suges[sugi][0]} \n Requisitante: {suges[sugi][1]} \n Descrição: {suges[sugi][2]}")
        print("")

#FUNÇÃO PARA LISTAR APENAS RECLAMAÇÕES
def opcao3():
    if reclama == []:
        print("Não existem reclamações feitas!")
    else:
        print("Essas são suas reclamações")
        for rec in range(len(reclama)):
            print(f" Protocolo: {reclama[rec][0]} \n Requisitante: {reclama[rec][1]} \n Descrição: {reclama[rec][2]}")
        print("")

#FUNÇÃO PARA LISTAR APENAS ELOGIOS
def opcao4():
    if elogio == []:
        print("Não existem elogios feitos!")
    else:
        print("Esses são seus elogios")
        for elo in range(len(elogio)):
            print(f" Protocolo: {elogio[elo][0]} \n Requisitante: {elogio[elo][1]} \n Descrição: {elogio[elo][2]}")
        print("")

#FUNÇÃO DE BUSCA POR PROTOCOLO
def opcao6():
    protnumero = int(input("Digite o número do seu protocolo!  "))
    # CONVERSOR DE STR PARA INT, DE MODO QUE SEJA POSSÍVEL UTILIZAR OS SINAIS MATEMÁTICOS PARA DETERMINAR O PROTOCOLO
    conversao = int(manifest[protnumero - 1][0])
    if protnumero == conversao:
        print(
            f" Protocolo: {manifest[protnumero - 1][0]} \n Requisitante: {manifest[protnumero - 1][1]} \n Manifestação: {manifest[protnumero - 1][2]} \n Descrição: {manifest[protnumero - 1][3]}")
    if protnumero not in conversao:
        print("Esse protocolo não existe, tente novamente!")



#TELA INICIAL DE ESCOLHAS
while True:
    print("=" * 60)
    print(f"""                   SISTEMA DE OUVIDORIA ABC""")
    print("=" * 60)
    print(f"""                    1) Listar manifestações
                    2) Listar sugestões
                    3) Listar reclamações
                    4) Listar elogios
                    5) Enviar uma manifestação 
                    6) Pesquisar protocolo por número
                    7) Sair do programa""")
    print("=" * 60)
    opcoes = (str(input("Digite o número correspondente a ação: ")))
    if opcoes in "1234567":
        opcoes=int(opcoes)
    else:
        print("Entrada inválida, tente digitar de 1 a 7!")
        continue
    print("=" * 60)
    if opcoes < 1 or opcoes > 7:
        print("Número inválido!")
    if opcoes == 7:
        print("=" * 60)
        print("Encerrando!")
        print("=" * 60)
        break

    #LISTAR MANIFESTAÇÕES
    if opcoes==1:
        opcao1()

    #LISTAR APENAS SUGESTÕES
    if opcoes == 2:
        opcao2()

    #LISTAR APENAS RECLAMAÇÕES
    if opcoes == 3:
        opcao3()

    #LISTAR APENAS ELOGIOS
    if opcoes == 4:
        opcao4()
    #BUSCA PROTOCOLO
    if opcoes==6:
        opcao6()

    #INTRODUÇÃO PARA LISTAR MANIFESTAÇÕES
    if opcoes == 5:
        nome = str(input("Qual é o seu nome?  ")).capitalize()
        print("=" * 60)
        bool=True
        while bool:
            tipo =input(f"""Olá, {nome}! Qual tipo de manifestação você quer enviar?
    1) RECLAMAÇÃO
    2) SUGESTÃO
    3) ELOGIO
    Digite o número correspondente: """)
    #VALIDAÇÃO CONTRA STRINGS E NÚMEROS INCORRESPONDENTES NA ESCOLHA DO TIPO
            if tipo in '123':
                tipo = int(tipo)
            else:
                print("ENTRADA INVÁLIDA! Digite apenas 1, 2 ou 3!")
                continue
            if tipo >= 1 and tipo <= 3:
                bool = False
            else:
                print("ENTRADA INVÁLIDA! Digite apenas 1, 2 ou 3!")

    #VARIÁVEL PARA TRANSFORMAR OS NÚMEROS NAS MANIFESTAÇÕES CORRESPONDENTES
        novotipo=""
        if tipo == 1:
            novotipo = "Reclamação"
            print("=" * 60)
            descri = str(input("Digite uma descrição sobre a sua reclamação: ")).capitalize()
            print("=" * 60)
            protocolo = str(len(manifest) + 1)
            manifesta = protocolo + "#" + nome + "#" + novotipo + "#" + descri
            maniquebrada = manifesta.split("#")
            manifest.append(maniquebrada[:])
            recll = protocolo + "#" + nome + "#" + descri
            recllquebrado = recll.split("#")
            reclama.append(recllquebrado)
            print(f"Sua reclamação foi listada, {nome}! O número do seu protocolo é {protocolo}")
        if tipo == 2:
            novotipo = "Sugestão"
            print("=" * 60)
            descri = str(input("Digite sua sugestão!: ")).capitalize()
            print("=" * 60)
            protocolo = str(len(manifest) + 1)
            manifesta = protocolo + "#" + nome + "#" + novotipo + "#" + descri
            maniquebrada = manifesta.split("#")
            manifest.append(maniquebrada[:])
            sugg = protocolo + "#" + nome + "#" + descri
            suggquebrado = sugg.split("#")
            suges.append(suggquebrado)
            print(f"Sua sugestão foi listada, {nome}! O número do seu protocolo é {protocolo}")
        if tipo == 3:
            novotipo = "Elogio"
            print("=" * 60)
            descri = str(input("Digite seu elogio!: ")).capitalize()
            print("=" * 60)
            protocolo = str(len(manifest) + 1)
            manifesta = protocolo + "#" + nome + "#" + novotipo + "#" + descri
            maniquebrada = manifesta.split("#")
            manifest.append(maniquebrada[:])
            ello = protocolo + "#" + nome + "#" + descri
            elloquebrado = ello.split("#")
            elogio.append(elloquebrado)
            print(f"Seu elogio foi enviado. Obrigado {nome}! O número do seu protocolo é {protocolo}")

