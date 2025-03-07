import csv

arquivo_csv = "dados.csv"

def carregar_dados():
    with open(arquivo_csv, mode="r", newline="") as arquivo:
        leitor = csv.reader(arquivo)
        dados = list(leitor)
    return dados

dados_alunos = carregar_dados()
print(dados_alunos)