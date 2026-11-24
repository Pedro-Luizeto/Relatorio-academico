from openpyxl import Workbook

arquivo = Workbook()

planilha = arquivo.active

planilha.title = 'Alunos'


cabecalhos = [
    "nome",
    'Curso',
    'Idade',
    'Nota final',
    'Data de matrícula'

]

alunos = [
    ["Pedro", "Python", 17, 8.5, "10/02/2026"],
    ["Ana", "Java", 18, 6.0, "15/02/2026"],
    ["Lucas", "Python", 19, 9.0, "20/02/2026"],
    ["Mariana", "JavaScript", 20, 7.5, "21/02/2026"],
    ["João", "Python", 18, 5.5, "22/02/2026"],
    ["Carlos", "Java", 21, 8.0, "23/02/2026"],
    ["Beatriz", "Python", 19, 6.5, "24/02/2026"],
    ["Rafael", "JavaScript", 22, 9.5, "25/02/2026"],
    ["Julia", "Python", 18, 7.0, "26/02/2026"],
    ["Gabriel", "Java", 20, 4.5, "27/02/2026"],
    ["Fernanda", "Python", 19, 8.8, "01/03/2026"],
    ["Matheus", "JavaScript", 21, 6.8, "02/03/2026"],
    ["Larissa", "Java", 18, 7.8, "03/03/2026"],
    ["Bruno", "Python", 23, 5.0, "04/03/2026"],
    ["Camila", "JavaScript", 20, 9.2, "05/03/2026"],
    ["Diego", "Python", 22, 6.2, "06/03/2026"],
    ["Isabela", "Java", 19, 8.1, "07/03/2026"],
    ["Thiago", "Python", 18, 7.3, "08/03/2026"],
    ["Amanda", "JavaScript", 21, 5.8, "09/03/2026"],
    ["Felipe", "Java", 20, 9.7, "10/03/2026"],
    ["Leticia", "Python", 19, 6.9, "11/03/2026"],
    ["Vinicius", "Java", 22, 8.4, "12/03/2026"],
    ["Bianca", "JavaScript", 18, 7.1, "13/03/2026"],
    ["Eduardo", "Python", 21, 4.8, "14/03/2026"],
    ["Sophia", "Java", 20, 9.3, "15/03/2026"],
    ["Gustavo", "Python", 23, 6.4, "16/03/2026"],
    ["Clara", "JavaScript", 19, 8.7, "17/03/2026"],
    ["Henrique", "Java", 18, 5.9, "18/03/2026"],
    ["Manuela", "Python", 22, 7.9, "19/03/2026"],
    ["Igor", "JavaScript", 20, 6.1, "20/03/2026"]
]

for aluno in alunos:
    planilha.append(aluno)

arquivo.save('alunos.xlsx')

print('planilha criada com sucesso !')
