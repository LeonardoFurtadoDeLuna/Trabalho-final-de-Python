
import os
import os.path

# FUNÇÕES DO MENU

#1 - INSERIR CONTEÚDO
def opcao1():
    print("\n{}- Opção 1 selecionada{}".format(cores["azul"], cores["limpa"]))

    nomearq = input('Digite o nome do arquivo: ')
    arquivo = open(nomearq, 'a',) #Abre o arquivo no modo gravação, e se o arquivo não existir a função o cria
    conteudo = input('Insira o conteúdo desejado: ')
    arquivo.write('\n' + conteudo) #Insere o conteúdo informado pelo usuário
    arquivo.close() #Fecha o arquivo
    print("\nConteúdo inserido!")

#2 - EXIBIR CONTEÚDO
def opcao2():
    print("\n{}- Opção 2 selecionada{}".format(cores["roxo"], cores["limpa"]))

    nomearq = input('Digite o nome do arquivo: ')
    arqexiste = os.path.exists(nomearq) #Método que verifica se o arquivo existe, retorna true ou false

    if arqexiste == True:
       arquivo = open(nomearq, 'r',) #Abre o arquivo no modo leitura
       print("\nConteúdo:")
       for linha in arquivo: #Laço para imprimir na tela cada linha do arquivo
           linha = linha.rstrip('\n')  # rstrip() serve pra 'estripar' algum caractere, ou seja, retirar determinado caracter da string.
           print(linha)
       arquivo.close() #Fecha o arquivo
    else:
        print("{}Erro: Arquivo não encontrado, tente novamente!{}".format(cores["vermelho"], cores["limpa"]))

#3 - TRANSFORMAR CONTEÚDO EM MAIÚSCULO
def opcao3():
    print("\n{}- Opção 3 selecionada{}".format(cores["amarelo"], cores["limpa"]))

    nomearq = input('Digite o nome do arquivo: ')
    arqexiste = os.path.exists(nomearq) #verifica se o arquivo existe

    if arqexiste == True:
        arquivo = open(nomearq, 'r', ) #Abre o arquivo no modo leitura
        maiusculo = arquivo.read().upper() #Guarda o conteúdo do arquivo em maiusculo

        arquivo = open(nomearq, 'w', ) #Abre o arquivo no modo gravação e apaga o conteúdo
        arquivo.write(maiusculo) #Insere o conteúdo em maiúsculo

        arquivo.close() #Fecha o arquivo
        print("\nO conteúdo do arquivo já está em maiúsculo!")
    else:
        print("{}Erro: Arquivo não encontrado, tente novamente!{}".format(cores["vermelho"], cores["limpa"]))

#4 - TRANSFORMAR CONTEÚDO EM MINÚSCULO
def opcao4():
    print("\n{}- Opção 4 selecionada{}".format(cores["verde"], cores["limpa"]))

    nomearq = input('Digite o nome do arquivo: ')
    arqexiste = os.path.exists(nomearq)

    if arqexiste == True:
        arquivo = open(nomearq, 'r', ) #Verifica se o arquivo existe
        minusculo = arquivo.read().lower() #Guarda o conteúdo do arquivo em minúsculo

        arquivo = open(nomearq, 'w', ) #Abre o arquivo no modo gravação e apaga o conteúdo
        arquivo.write(minusculo) #Insere o conteúdo em minúsculo

        arquivo.close() #Fecha o arquivo
        print("\nO conteúdo do arquivo já está em minusculo!")
    else:
        print("{}Erro: Arquivo não encontrado, tente novamente!{}".format(cores["vermelho"], cores["limpa"]))

#5 - FREQUÊNCIA
def opcao5():
    print("\n{}- Opção 5 selecionada{}".format(cores["cinza"], cores["limpa"]))

    nomearq = input('Digite o nome do arquivo: ')
    arqexiste = os.path.exists(nomearq) #Verifica se o arquivo exite
    
    if arqexiste == True:
        arquivo = open(nomearq, 'r',) #Abre o arquivo no modo leitura
        conteudo = arquivo.read()
       
        #Variáveis contadoras
        qtdletra = 0 
        qtdnum = 0
        
        for caracter in conteudo: #Laço que avaliar os caracteres
            
            #Quantidades letras
            letra = caracter.isalpha()
            if letra == True:
                qtdletra+=1
            
            #Quantidades números
            num = caracter.isnumeric()
            if num == True:
                qtdnum+=1
                
            """
            #Quantidade de espaços II
            espaco = caracter.isspace()
            if espaco == True:
               qtdespaco+=1
            """
        #Quantidade de espaços
        qtdespaco = conteudo.count(' ')

        # Quantidade de linhas
        qtdlinhas = conteudo.count('\n')
            
        #Quantidade de caracteres
        qtdcaracter = len(conteudo)
    
        #Quantidade de vogais
        
        #TRATAMENTO DO CONTEÚDO I - DEIXANDO EM MINÚSCULO
        conteudo = conteudo.lower()
        
        #TRATAMENTO DO CONTEÚDO II - TIRANDO ACENTOS 
        for item in "áàãâéêíóõôú":
            
            if ( (item == "á") or (item == "à") or (item == "ã") or (item == "â") ):
              conteudo_sem_acento = conteudo.replace(item, "a")
              conteudo = conteudo_sem_acento
            elif ( (item == "é") or (item == "ê") ):
                 conteudo_sem_acento = conteudo.replace(item, "e")
                 conteudo = conteudo_sem_acento
            elif (item == "í"):
                 conteudo_sem_acento = conteudo.replace(item, "i")
                 conteudo = conteudo_sem_acento
            elif ( (item == "ó") or (item == "ô") or (item == "õ") ):
                 conteudo_sem_acento = conteudo.replace(item, "o")
                 conteudo = conteudo_sem_acento
            else:
                 conteudo_sem_acento = conteudo.replace(item, "u")
                 conteudo = conteudo_sem_acento

            # A função replace() substitui uma parte da string por uma outra String.
        
        #QUEBRANDO A STRING QUANDO HÁ UMA VOGAL E CONVERTENDO-A PARA LISTA
        a = conteudo.split("a")
        e = conteudo.split("e")
        i = conteudo.split("i")
        o = conteudo.split("o")
        u = conteudo.split("u")

        # A função split() divide um texto todas as vezes que a String passada como argumento for localizada.
        
        #CONTANDO QUANTIDADES DE ELEMENTOS DA LISTA
        qtdvogais = (len(a)-1) + (len(e)-1) + (len(i)-1) + (len(o)-1) + (len(u)-1)
        
        #Impressão dos resultados obtidos
        print("\nQuantidade de caracteres: {} "
              "\nQuantidade de letras: {}     "
              "\nQuantidade de números: {}    "
              "\nQuantidade de linhas: {}    "
              "\nQuantidade de vogais: {}    "
              "\nQuantidade de espaços: {}    ".format(qtdcaracter, qtdletra, qtdnum, qtdlinhas, qtdvogais, qtdespaco))
        
        arquivo.close()
    
    else:
        print("{}Erro: Arquivo não encontrado, tente novamente!{}".format(cores["vermelho"], cores["limpa"]))

#6 - SUBSTITUIR PALAVRA
def opcao6():

    print("\n{}- Opção 6 selecionada{}".format(cores["vermelho"], cores["limpa"]))

    nomearq = input('Digite o nome do arquivo: ')
    arqexiste = os.path.exists(nomearq) #Verifica se o arquivo existe

    if arqexiste == True:
       palavra = input("Digite a palavra a ser substituída: ").lower() #Guarda a palavra a ser substituida como minuscula
       
       arquivo = open(nomearq, 'r',) #Abre o arquivo no modo leitura
       conteudo = arquivo.read().lower() #Guarda o conteúdo do arquivo
       
       if palavra in conteudo: #Se a palavra estiver no arquivo a seubstituição ocorrerá
           palavra_substituta = input("Informe a palavra substituta: ")
           conteudo_novo = conteudo.replace(palavra, palavra_substituta)
           
           arquivo = open(nomearq, 'w',)
           arquivo.write(conteudo_novo)
           print("\nSubstituição realizada!")
           arquivo.close()
       else:
           arquivo.close()
           print("\n{}Erro: Palavra inexistente no arquivo, tente novamente!{}".format(cores["vermelho"], cores["limpa"]))

    else:
       print("{}Erro: Arquivo não encontrado, tente novamente!{}".format(cores["vermelho"], cores["limpa"]))

#7 - SAIR DO PROGRAMA
def opcao7():
    print("\nPrograma finalizado!")
    exit(0)

#8 - OPÇÃO INVÁLIDA
def opcao8():
    print("{}Erro: Opção informada inválida tente novamente!{}".format(cores["vermelho"], cores["limpa"]))

# PROGRAMA PRINCIPAL
cores = {'limpa':'\033[m',
         'cinza':'\033[37m',
         'vermelho':'\033[31m',
         'amarelo':'\033[33m',
         'verde':'\033[32m',
         'azul':'\033[34m',
         'roxo':'\033[35m',
         'negrito':'\033[1m'}

while True:

    print('{}\n--------------------------------------------'
          '\n|                  MENU                    |'
          '\n| 1 - Inserir conteúdo em arquivo          |'
          '\n| 2 - Exibir conteúdo do arquivo           |'
          '\n| 3 - Transformar o conteúdo em maiúsculo  |'
          '\n| 4 - Tranformar o conteúdo em minúsculo   |'
          '\n| 5 - Exibir relação de ocorrência         |'
          '\n| 6 - Substituir palavra                   |'
          '\n| 7 - Sair                                 |'
          '\n--------------------------------------------{}'
          .format(cores["roxo"], cores["limpa"]))

    menu = {1: opcao1, 2: opcao2, 3: opcao3, 4: opcao4, 5: opcao5, 6: opcao6, 7: opcao7, 8: opcao8}
    opcao = int(input("\nDigite a opção desejada: "))

    if ((opcao < 1) or (opcao > 7)):
        opcao = 8

    menu.get(opcao)()

    input("\nDigite enter para continuar...")
    os.system("cls")
    
    # A função get pode receber dois valores, sendo o 1° como obrigatório e o 2° opcional.
    # No caso do código faz a captura o valor da chave presente no dicionário e executa a função correspondente

