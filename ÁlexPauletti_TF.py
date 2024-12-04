#Álex Capelani Pauletti, 2024006596, BSI24
import csv
import math

partidos = {
    "15": "MDB",
    "12": "PDT",
    "13": "PT",
    "65": "PCdoB",
    "40": "PSB",
    "45": "PSDB",
    "36": "AGIR",
    "33": "MOBILIZA",
    "23": "CIDADANIA",
    "43": "PV",
    "70": "AVANTE",
    "11": "PP",
    "16": "PSTU",
    "21": "PCB",
    "28": "PRTB",
    "27": "DC",
    "29": "PCO",
    "20": "PODE",
    "10": "REPUBLICANOS",
    "50": "PSOL",
    "22": "PL",
    "55": "PSD",
    "77": "SOLIDARIEDADE",
    "30": "NOVO",
    "18": "REDE",
    "35": "PMB",
    "80": "UP",
    "44": "UNIÃO",
    "25": "PRD"
}

def imprimeVotoLongo2000(busca, ondeBuscar):
    cabecalho = ['AGRUPAMENTO', 'VOTOS TOTAIS', 'VOTOS VÁLIDOS %', 'VOTOS BRANCOS %', 'VOTOS NULOS %']

    with open ("ResultadoBusca.csv", "w", newline='', encoding='ISO-8859-15') as Municipio:
        writer = csv.writer(Municipio, delimiter=";")
        writer.writerow(cabecalho)

        data = []
        dataAtual = []

        votos = buscaVoto(busca, ondeBuscar)
        Branco = votos[0]
        Nulo = votos[1]
        Legal = votos[2]
        Total = votos[3]

        dataAtual.append(busca)
        dataAtual.append(Total)
        dataAtual.append(round(((Legal/Total)*100), 2))
        dataAtual.append(round(((Branco/Total)*100), 2))
        dataAtual.append(round(((Nulo/Total)*100), 2))
        data.append(dataAtual)

        dataDecrescente(data, writer)

def buscaVoto(cd, cdAtual):
    Branco = 0
    Nulo = 0
    Legal = 0
    Total = 0

    #municipio
    if cdAtual != NR_VOTAVEL:
        for contagem in range(len(cdAtual)):
            if cdAtual[contagem] == cd:
                if contagem == 0:
                    print("")
                    
                elif NR_VOTAVEL[contagem] == "95":
                    Branco = Branco + (int(QT_VOTOS[contagem]))
                    Total = Total + (int(QT_VOTOS[contagem]))

                elif NR_VOTAVEL[contagem] == "96":
                    Nulo = Nulo + (int(QT_VOTOS[contagem]))
                    Total = Total + (int(QT_VOTOS[contagem]))

                else:
                    Legal = Legal + (int(QT_VOTOS[contagem]))
                    Total = Total + (int(QT_VOTOS[contagem]))

    #partido
    else:
        for contagem in range(len(cdAtual)):
            if cdAtual[contagem] == cd:
                if contagem == 0:
                    print("")

                else:
                    Total = Total + (int(QT_VOTOS[contagem]))

            if cdAtual[contagem][:2] == cd:
                if contagem == 0:
                    print("")

                else:
                    Total = Total + (int(QT_VOTOS[contagem]))
                    
    return Branco, Nulo, Legal, Total   

def dataDecrescente(data, writer):
    maior = 0
    maiorData = 0
    for a in range(len(data)):
        maior = 0
        for b in range(len(data)):
            if data[b][1] > maior:
                maior = data[b][1] 
                maiorData = b 
        
        if maiorData > (len(data) - 1):
            break
        writer.writerow(data[maiorData])

        for c in range(len(data)):
            if c > (len(data) - 1):
                continue
            if data[c][1] == maior:
                del data[c]


def resumo(cdAtual, nmAtual):
    if cdAtual == CD_MUNICIPIO:
        cabecalho = ['AGRUPAMENTO', 'VOTOS TOTAIS', 'VOTOS VÁLIDOS %', 'VOTOS BRANCOS %', 'VOTOS NULOS %']
    else:
        cabecalho = ['AGRUPAMENTO', 'VOTOS TOTAIS']

    if cdAtual == CD_MUNICIPIO:
        agrupamentoAtual = []
        for item in cdAtual:
            if item not in agrupamentoAtual:
                agrupamentoAtual.append(item)
        del agrupamentoAtual[0]
        nomeamentoAtual = []
        for item in nmAtual:
            if item not in nomeamentoAtual:
                nomeamentoAtual.append(item)
        del nomeamentoAtual[0]
    
        with open ("Resumo.csv", "w", newline='', encoding='ISO-8859-15') as Municipio:
            writer = csv.writer(Municipio, delimiter=";")
            writer.writerow(cabecalho)

            data = []
            for cod in range(len(agrupamentoAtual)):
                dataAtual = []

                nm = nomeamentoAtual[cod]
                cd = agrupamentoAtual[cod]

                votos = buscaVoto(cd, cdAtual)
                Branco = votos[0]
                Nulo = votos[1]
                Legal = votos[2]
                Total = votos[3]

                dataAtual.append(nm)
                dataAtual.append(Total)
                dataAtual.append(round(((Legal/Total)*100), 2))
                dataAtual.append(round(((Branco/Total)*100), 2))
                dataAtual.append(round(((Nulo/Total)*100), 2))
                data.append(dataAtual)

            dataDecrescente(data, writer)
    
    #busca partido aqui
    else:   
         with open ("Resumo.csv", "a+", newline='', encoding='ISO-8859-15') as Municipio:
            writer = csv.writer(Municipio, delimiter=";")
            writer.writerow(cabecalho)

            data = []
            for cod in range(len(cdAtual)):
                dataAtual = []

                nm = nmAtual[cod]
                cd = cdAtual[cod]

                votos = buscaVoto(cd, NR_VOTAVEL)
                Branco = votos[0]
                Nulo = votos[1]
                Legal = votos[2]
                Total = votos[3]

                
                dataAtual.append(nm)
                dataAtual.append(Total)
                data.append(dataAtual)

            dataDecrescente(data, writer)

def filtraPFV(partido, file, munis, nomisMunis):
    cabecalho = ['MUNICÍPIO', 'VOTOS TOTAIS']

    
    with open (f"{file}.csv", "a+", newline='', encoding='ISO-8859-15') as filtragem:
        writer = csv.writer(filtragem, delimiter=";")
        writer.writerow(cabecalho)

        agrupamentoAtual = []
        for item in munis:
            if item not in agrupamentoAtual:
                agrupamentoAtual.append(item)
        del agrupamentoAtual[0]
        nomeamentoAtual = []
        for item in nomisMunis:
            if item not in nomeamentoAtual:
                nomeamentoAtual.append(item)
        del nomeamentoAtual[0]

        data = []
        for cod in range(len(agrupamentoAtual)):
            dataAtual = []

            nm = nomeamentoAtual[cod]
            cd = agrupamentoAtual[cod]

            votos = buscaVoto2(cd, munis, partido)
            Total = votos

            dataAtual.append(nm)
            dataAtual.append(Total)
            data.append(dataAtual)
        dataDecrescente(data, writer)    

    f = open(f"{file}.csv", "r+")
    deletaLinhas = f.readlines()
    num = 6 - len(deletaLinhas) 
    deletaLinhas = deletaLinhas[:-(num*-1)]

    with open(f"{file}.csv", "w") as f:
        for a in deletaLinhas:
            f.write(a)

def buscaVoto2(munis, munici, partido):
    Total = 0

    for contagem in range(len(munici)):
            if munici[contagem] == munis:
                if contagem == 0:
                    print("")

                elif NR_VOTAVEL[contagem][:2] == partido:
                    Total = Total + (int(QT_VOTOS[contagem]))
    
    return Total








#Menu para acessar todas as funções do programa
def menuInterativo (contLinhas):
    global opcao
    menu = True
    while menu == True:
        opcao = input("1- Relatório do documento original \n2- Resumo \n3- Busca \n4- Dados estatísticos da votação \n5- Filtragem de Dados Partidários \n6- Pega Prefeito \n0- Finalizar programa \nDigite o número para acessar a função associada à ele: ")

        if opcao == "1":
            with open ("Relatório.txt", "w", encoding= "utf-8") as relatorio:
                relatorio.write(f"O documento original possui {contLinhas} linhas. Ele possui 26 colunas, que são: \n\n DT_GERACAO - Data de extração de dados para o arquivo. \n HH_GERACAO - Hora da extração de dados para o arquivo.\n\
 ANO_ELEICAO - Ano de referência da eleição para geração do arquivo. \n CD_TIPO_ELEICAO - Código do tipo de eleição. Pode assumir os valores: 1 - Eleção Suplementar, 2 - Eleição Ordinária e 3 - Consulta Popular.\n\
 NM_TIPO_ELEICAO - Nome do tipo de eleição. \n NR_TURNO - Número do turno da eleição. \n CD_ELEICAO - Código único da eleição no âmbito da Justiça Eleitoral. \n DS_ELEICAO - Descrição da eleição.\n\
 DT_ELEICAO - Data em que ocorreu a eleição. \n TP_ABRANGENCIA - Abrangência da eleição. \n SG_UF - Sigla da Unidade da Federação em que ocorreu a eleição \n SG_UE - Sigla da Unidade Eleitoral em que a candidata ou o candidato concorre na eleição.\n\
 NM_UE - Nome de Unidade Eleitoral da candidata ou candidato. \n CD_MUNICIPIO - Código TSE do município onde ocorreu a eleição. \n NM_MUNICIPIO - Nome do município onde ocorreu a eleição.\n\
 NR_ZONA - Número da zona onde ocorreu a eleição. \n NR_SECAO - Número da seção em que ocorreu a eleição. \n CD_CARGO - Código do cargo da candidata ou candidato. \n DS_CARGO - Descrição do cargo da candidata ou candidato.\n\
 NR_VOTAVEL - Número do votável. \n NM_VOTAVEL - Nome do votável. \n QT_VOTOS - Quantidade de votos recebidos pelo votável naquele município, zona e seção. \n NR_LOCAL_VOTACAO - Número do local de votação da eleitora ou eleitor.\n\
 SQ_CANDIDATO - Número sequencial da candidata ou candidato, gerado internamente pelos sistemas eleitorais para cada eleição. \n NM_LOCAL_VOTACAO - Nome do local de votação da eleitora ou eleitor. \n DS_LOCAL_VOTACAO_ENDERECO - Descrição do endereço do local de votação da eleitora ou eleitor. ")

        if opcao == "2":
            resumo(CD_MUNICIPIO, NM_MUNICIPIO)

            partidosCDList = []
            partidosNMList = []
            for a in NR_VOTAVEL[1:]:
                final = a[:2]
                if final == "95" or final == "96":
                    continue
                elif final not in partidosCDList:
                    partidosCDList.append(final)
            
            for a in partidosCDList:
                nomePartido = partidos.get(a)
                if nomePartido not in partidosNMList:
                    partidosNMList.append(f"{nomePartido}")

            resumo(partidosCDList, partidosNMList)

        if opcao == "3":
            while True:
                opcao2 = input("O que você quer buscar? \n1- Candidato \n2- Seção \n3- Zona \n0- Voltar ao menu \nInsira a opção que deseja acessar: ")

                if opcao2 == "1":
                    candidatoNM = input("Você pode encontrar o nome completo de seu candidato no site: https://divulgacandcontas.tse.jus.br/divulga/#/home \nInforme o número completo de seu candidato, entre aspas: ")
                    votos = buscaVoto(candidatoNM, NM_VOTAVEL)
                    Totais = votos[3]
                    print(f"Candidato(a) {candidatoNM} teve {Totais} votos no total.")

                if opcao2 == "2":
                    secaoNR = input("Informe o número da seção que deseja buscar: ")
                    imprimeVotoLongo2000(secaoNR, NR_SECAO)

                if opcao == "3":
                    zonaNR = input("Informe o número da zona que deseja buscar: ")
                    imprimeVotoLongo2000(zonaNR, NR_ZONA)
        
        if opcao == "4":
            with open("Dados.txt", "w") as dados:
                jaVi = []
                nrJaVi = []
                for a in QT_VOTOS:
                    if a not in (jaVi):
                        jaVi.append(a)
                        cont = 0
                        for b in QT_VOTOS:
                            if b == a:
                                cont+=1
                        nrJaVi.append(cont)

                maior = 0
                for a in range(len(nrJaVi)):
                    if nrJaVi[a] > maior:
                        maior = nrJaVi[a]
                        moda = jaVi[a]  

                soma = 0      
                somaDP = 0  
                votosA = []
                for a in QT_VOTOS[1:]:
                    soma = soma + int(a)
                    votosA.append(a)
                
                media = soma/((len(QT_VOTOS))-1)
                mediana = votosA[round((len(votosA))/2)]
 
                for a in QT_VOTOS[1:]:
                    somaDP = somaDP + ((int(a)-media)**2)

                desvioPadrao = math.sqrt(somaDP/((len(QT_VOTOS))-1))


                dados.write(f"Dados coletados sobre o número de votos totais: \n\nModa: {moda}. Número de votos mais comum de ser registrado ao mesmo tempo.\
                            \nMédia: {media}\
                            \nMediana: {mediana}\
                            \nDesvio Padrão: {desvioPadrao}")

        if opcao == "5":
            queroVer = input("Digite o número do partido que gostaria de ver sobre: ")
            nomeFile = input("Qual o nome desejado para o arquivo de filtragem? ")
            filtraPFV(queroVer, nomeFile, CD_MUNICIPIO, NM_MUNICIPIO)
            print("Foi criado um arquivo apresentando as 5 cidades onde seu partido recebeu mais votos!")

        if opcao == "6":
            candidatosCity = []
            votosCity = []
            munis = input("Informe o município qual queira saber o candidato eleito como prefeito: ")
            for contagem in range(len(NM_MUNICIPIO)):
                if munis == NM_MUNICIPIO[contagem]:
                    if CD_CARGO[contagem] == "11":
                        if SQ_CANDIDATO[contagem] != "-1":
                            if NM_VOTAVEL[contagem] not in candidatosCity:
                                candidatosCity.append(NM_VOTAVEL[contagem])

            for candidato in candidatosCity:
                somaVotos = 0
                for contagem in range(len(NM_MUNICIPIO)):
                    if candidato == NM_VOTAVEL[contagem]:
                        somaVotos = somaVotos + int(QT_VOTOS[contagem])

                votosCity.append(somaVotos)
            
            maior = 0
            prefeito = 0
            for a in range(len(votosCity)):
                if votosCity[a] > maior:
                    prefeito = candidatosCity[a]

            print(f"O prefeito de {munis} é o candidato(a) {prefeito}")
                    
                

        if opcao == "0":
            break

DT_GERACAO = []
HH_GERACAO = []
ANO_ELEICAO = []
CD_TIPO_ELEICAO = []
NM_TIPO_ELEICAO = []
NR_TURNO = []
CD_ELEICAO = []
DS_ELEICAO = []
DT_ELEICAO = []
TP_ABRANGENCIA = []
SG_UF = []
SG_UE = []
NM_UE = []
CD_MUNICIPIO = []
NM_MUNICIPIO = []
NR_ZONA = []
NR_SECAO = []
CD_CARGO = []
DS_CARGO = []
NR_VOTAVEL = []
NM_VOTAVEL = []
QT_VOTOS = []
NR_LOCAL_VOTACAO = []
SQ_CANDIDATO = []
NM_LOCAL_VOTACAO = []
DS_LOCAL_VOTACAO_ENDERECO = []

contLinhas = 0

with open ("votos.csv", "r") as arquivo:
    for a in arquivo.readlines():
        contLinhas += 1
        separacao = a.split(";")
        DT_GERACAO.append(separacao[0])
        HH_GERACAO.append(separacao[1])
        ANO_ELEICAO.append(separacao[2])
        CD_TIPO_ELEICAO.append(separacao[3])
        NM_TIPO_ELEICAO.append(separacao[4])
        NR_TURNO.append(separacao[5])
        CD_ELEICAO.append(separacao[6])
        DS_ELEICAO.append(separacao[7])
        DT_ELEICAO.append(separacao[8])
        TP_ABRANGENCIA.append(separacao[9])
        SG_UF.append(separacao[10])
        SG_UE.append(separacao[11])
        NM_UE.append(separacao[12])
        CD_MUNICIPIO.append(separacao[13])
        NM_MUNICIPIO.append(separacao[14])
        NR_ZONA.append(separacao[15])
        NR_SECAO.append(separacao[16])
        CD_CARGO.append(separacao[17])
        DS_CARGO.append(separacao[18])
        NR_VOTAVEL.append(separacao[19])
        NM_VOTAVEL.append(separacao[20].strip('"'))
        QT_VOTOS.append(separacao[21])
        NR_LOCAL_VOTACAO.append(separacao[22])
        SQ_CANDIDATO.append(separacao[23])
        NM_LOCAL_VOTACAO.append(separacao[24])
        DS_LOCAL_VOTACAO_ENDERECO.append(separacao[25])


menuInterativo(contLinhas)