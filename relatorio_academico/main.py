from openpyxl import load_workbook 
from openpyxl import Workbook
import os

os.makedirs('relatorios', exist_ok=True)

arquivo = load_workbook('alunos.xlsx')
planilha = arquivo.active

aprovados = []
reprovados = []
notas = []

for linha in planilha.iter_rows(min_row=2, values_only=True):

    nome = linha[0]
    curso = linha[1]
    idade = linha[2]
    nota = linha[3]
    matricula = linha[4]

    notas.append(nota)

    if nota >= 6:
        aprovados.append(linha)
    else:
        reprovados.append(linha)

def gerar_relatorio(nome_arquivo, alunos):

    novo_arquivo = Workbook()
    nova_planilha = novo_arquivo.active

    nova_planilha.title = 'Alunos'

    nova_planilha.append([
        'Nome',
        'Curso',
        'idade', 
        'Nota Final',
        'Data de matrícula'

    ])

    for aluno in alunos:
        nova_planilha.append(list(aluno))

    novo_arquivo.save(f'relatorios/ {nome_arquivo}.')


gerar_relatorio('aprovados.xlsx', aprovados)
gerar_relatorio('reprovados.xlsx', reprovados)

media = sum(notas) / len(notas)

maior_nota = max(notas)

for linha in planilha.iter_rows(min_row=2, values_only=True):

    if linha[3] == maior_nota:
        melhor_aluno = linha[0]
        break


print("\n===== RELATÓRIO DA TURMA =====")

print(f"Total de alunos: {len(notas)}")
print(f"Aprovados: {len(aprovados)}")
print(f"Reprovados: {len(reprovados)}")

print(f"Média da turma: {media:.2f}")
print(f"Maior nota: {maior_nota}")
print(f"Melhor aluno: {melhor_aluno}")

print("\nRelatórios gerados com sucesso!")