import random

# IDENTIFICAÇÃO DA MISSÃO

nome_missao = "MISSÃO HÉCATE"
nome_equipe = "Equipe Gablora"

areas_monitoradas = [
    "Temperatura Interna",
    "Comunicação com a Base",
    "Sistema de Energia",
    "Suporte de Oxigênio",
    "Estabilidade Operacional"
]


# LIMITES DOS CICLOS

limites_ciclos = {
    "Lançamento": {
        "temperatura": (18, 45),
        "comunicacao": (50, 100),
        "bateria": (70, 100),
        "oxigenio": (90, 100),
        "estabilidade": (60, 100)
    },

    "Ascensão": {
        "temperatura": (20, 45),
        "comunicacao": (45, 100),
        "bateria": (60, 100),
        "oxigenio": (88, 100),
        "estabilidade": (50, 100)
    },

    "Inserção Orbital": {
        "temperatura": (18, 40),
        "comunicacao": (40, 100),
        "bateria": (50, 95),
        "oxigenio": (85, 100),
        "estabilidade": (50, 100)
    },

    "Operação Espacial": {
        "temperatura": (15, 35),
        "comunicacao": (35, 100),
        "bateria": (40, 90),
        "oxigenio": (80, 100),
        "estabilidade": (40, 100)
    },

    "Manobras e Correções": {
        "temperatura": (18, 45),
        "comunicacao": (20, 100),
        "bateria": (15, 85),
        "oxigenio": (75, 100),
        "estabilidade": (30, 100)
    },

    "Retorno ou Desativação": {
        "temperatura": (18, 50),
        "comunicacao": (20, 90),
        "bateria": (10, 80),
        "oxigenio": (70, 95),
        "estabilidade": (20, 90)
    }
}


# GERAÇÃO DOS DADOS

def gerar_dados_ciclo(nome_ciclo):
    ciclo = limites_ciclos[nome_ciclo]

    return [
        random.randint(*ciclo["temperatura"]),
        random.randint(*ciclo["comunicacao"]),
        random.randint(*ciclo["bateria"]),
        random.randint(*ciclo["oxigenio"]),
        random.randint(*ciclo["estabilidade"])
    ]


# FUNÇÕES DE ANÁLISE

def analisar_temperatura(valor):
    if valor < 18:
        return "ATENÇÃO", 1
    elif valor <= 30:
        return "NORMAL", 0
    elif valor <= 35:
        return "ATENÇÃO", 1
    else:
        return "CRÍTICO", 2


def analisar_comunicacao(valor):
    if valor < 30:
        return "CRÍTICO", 2
    elif valor < 60:
        return "ATENÇÃO", 1
    else:
        return "NORMAL", 0


def analisar_bateria(valor):
    if valor < 20:
        return "CRÍTICO", 2
    elif valor < 50:
        return "ATENÇÃO", 1
    else:
        return "NORMAL", 0


def analisar_oxigenio(valor):
    if valor < 80:
        return "CRÍTICO", 2
    elif valor < 90:
        return "ATENÇÃO", 1
    else:
        return "NORMAL", 0


def analisar_estabilidade(valor):
    if valor < 40:
        return "CRÍTICO", 2
    elif valor < 70:
        return "ATENÇÃO", 1
    else:
        return "NORMAL", 0


# CLASSIFICAÇÃO DO CICLO

def classificar_ciclo(risco):
    if risco <= 2:
        return "Missão estável"
    elif risco <= 5:
        return "MISSÃO EM ATENÇÃO"
    else:
        return "!!! MISSÃO CRÍTICA !!!"


# RECOMENDAÇÕES

def gerar_recomendacao(risco):
    if risco <= 2:
        return "Manter operação normal e continuar monitoramento."

    elif risco <= 5:
        return "MONITORAR SISTEMA EM ATENÇÃO E PREPARAR PLANO DE CONTINGÊNCIA"

    else:
        return "!!! ATIVAR MODO DE SEGURANÇA E PRIORIZAR COMNICAÇÃO, ENERGIA E SUPORTE À VIDA !!!"


# TENDÊNCIA DA MISSÃO

def analisar_tendencia(lista_riscos):
    if lista_riscos[-1] > lista_riscos[0]:
        return "A missão apresentou tendência de piora."

    elif lista_riscos[-1] < lista_riscos[0]:
        return "A missão apresentou tendência de melhora."

    else:
        return "A missão permaneceu estável em relação ao início."


# ÁREA MAIS AFETADA

def identificar_area_mais_afetada(pontuacoes):
    maior_pontuacao = max(pontuacoes)
    indice = pontuacoes.index(maior_pontuacao)

    return areas_monitoradas[indice], maior_pontuacao


# GERAÇÃO DA MATRIZ DA MISSÃO

dados_missao = []

for ciclo in limites_ciclos:
    dados_missao.append(gerar_dados_ciclo(ciclo))


# VARIÁVEIS DE CONTROLE

nomes_ciclos = list(limites_ciclos.keys())
riscos_ciclos = []
avancos = []
ciclo_mais_critico = 0
maior_risco = -1
quantidade_ciclos_criticos = 0
pontuacao_areas = [0, 0, 0, 0, 0]
soma_temperatura = 0
soma_comunicacao = 0
soma_bateria = 0
soma_oxigenio = 0
soma_estabilidade = 0


# RELATÓRIO DOS CICLOS

print("=" * 60)
print(f"Missão: {nome_missao}")
print(f"Equipe: {nome_equipe}")
print("=" * 60)

for i, ciclo in enumerate(dados_missao):

    temperatura, comunicacao, bateria, oxigenio, estabilidade = ciclo

    soma_temperatura += temperatura
    soma_comunicacao += comunicacao
    soma_bateria += bateria
    soma_oxigenio += oxigenio
    soma_estabilidade += estabilidade

    status_temp, pontos_temp = analisar_temperatura(temperatura)
    status_com, pontos_com = analisar_comunicacao(comunicacao)
    status_bat, pontos_bat = analisar_bateria(bateria)
    status_oxi, pontos_oxi = analisar_oxigenio(oxigenio)
    status_est, pontos_est = analisar_estabilidade(estabilidade)

    risco_total = (
            pontos_temp +
            pontos_com +
            pontos_bat +
            pontos_oxi +
            pontos_est
    )


    # Avanço do ciclo

    if i == 0:
        avancos.append("INÍCIO")
    else:
        risco_anterior = riscos_ciclos[-1]

        if risco_total < risco_anterior:
            avancos.append("MELHORA")
        elif risco_total > risco_anterior:
            avancos.append("PIORA")
        else:
            avancos.append("PERMANÊNCIA")

    riscos_ciclos.append(risco_total)


    # Pontuação das áreas

    pontuacao_areas[0] += pontos_temp
    pontuacao_areas[1] += pontos_com
    pontuacao_areas[2] += pontos_bat
    pontuacao_areas[3] += pontos_oxi
    pontuacao_areas[4] += pontos_est

    classificacao = classificar_ciclo(risco_total)

    if classificacao == "MISSÃO CRÍTICA":
        quantidade_ciclos_criticos += 1

    if risco_total > maior_risco:
        maior_risco = risco_total
        ciclo_mais_critico = i + 1

    print("\n" + "=" * 60)
    print(f"\nCICLO {i + 1} - {nomes_ciclos[i]}")

    print(f"Temperatura : {temperatura}°C -> {status_temp}")
    print(f"Comunicação : {comunicacao}% -> {status_com}")
    print(f"Bateria     : {bateria}% -> {status_bat}")
    print(f"Oxigênio    : {oxigenio}% -> {status_oxi}")
    print(f"Estabilidade: {estabilidade}% -> {status_est}")

    print(f"\nPontuação de risco: {risco_total}")
    print(f"Classificação: {classificacao}")
    print(f"Recomendação: {gerar_recomendacao(risco_total)}")




# RELATÓRIO FINAL

print("\n" + "=" * 60)
print("RELATÓRIO FINAL DA MISSÃO")
print("=" * 60)

print(f"Missão: {nome_missao}")
print(f"Equipe: {nome_equipe}")

print("\n" + "." * 60)
print("CICLOS")
print("." * 60)
print(f"\nQuantidade de ciclos analisados: {len(dados_missao)}")
print(f"Quantidade de ciclos críticos: {quantidade_ciclos_criticos}")
print(f"Ciclo mais crítico: {ciclo_mais_critico}")
print(analisar_tendencia(riscos_ciclos))

media_temperatura = soma_temperatura / len(dados_missao)
media_comunicacao = soma_comunicacao / len(dados_missao)
media_bateria = soma_bateria / len(dados_missao)
media_oxigenio = soma_oxigenio / len(dados_missao)
media_estabilidade = soma_estabilidade / len(dados_missao)

print("\n" + "." * 60)
print("MÉDIAS")
print("." * 60)
print(f"\nMédia de temperatura: {media_temperatura:.2f}°C")
print(f"Média de comunicação: {media_comunicacao:.2f}%")
print(f"Média de bateria: {media_bateria:.2f}%")
print(f"Média de oxigênio: {media_oxigenio:.2f}%")
print(f"Média de estabilidade: {media_estabilidade:.2f}%")

print(f"Maior pontuação de risco: {maior_risco}")

risco_medio = sum(riscos_ciclos) / len(riscos_ciclos)
print(f"Risco médio da missão: {risco_medio:.2f}")


print("\n" + "." * 60)
print("PONTUAÇÃO ACUMULADA POR ÁREA")
print("." * 60)

for i in range(len(areas_monitoradas)):
    print(f"{areas_monitoradas[i]}: {pontuacao_areas[i]} pontos")

area_mais_afetada, pontos = identificar_area_mais_afetada(
    pontuacao_areas
)

print(F"\nÁrea mais afetada: {area_mais_afetada} ({pontos} pontos)")

# ============================================================
# TABELA RESUMO DOS CICLOS
# ============================================================

print("\n" + "." * 120)
print("TABELA RESUMO DOS CICLOS")
print("." * 120)

print(
    f"{'Ciclo':<28}"
    f"{'Temp':>8}"
    f"{'Com':>8}"
    f"{'Bat':>8}"
    f"{'Oxi':>8}"
    f"{'Est':>8}"
    f"{'Risco':>10}"
    f"{'Avanço':>15}"
)

print("-" * 120)

for i, ciclo in enumerate(dados_missao):

    temperatura, comunicacao, bateria, oxigenio, estabilidade = ciclo

    print(
        f"{nomes_ciclos[i]:<28}"
        f"{temperatura:>8}"
        f"{comunicacao:>8}"
        f"{bateria:>8}"
        f"{oxigenio:>8}"
        f"{estabilidade:>8}"
        f"{riscos_ciclos[i]:>10}"
        f"{avancos[i]:>15}"
    )



classificacao_final = classificar_ciclo(round(risco_medio))

print("\nClassificação final:")
print(classificacao_final)

print("\nConclusão:")

if classificacao_final == "Missão estável":
    print(
        "A missão manteve seus sistemas operando dentro dos parâmetros esperados."
    )

elif classificacao_final == "MISSÃO EM ATENÇÃO":
    print(
        "A missão apresentou instabilidades moderadas que exigem acompanhamento contínuo."
    )

else:
    print(
        "A missão apresentou condições críticas e requer ações corretivas imediatas."
    )