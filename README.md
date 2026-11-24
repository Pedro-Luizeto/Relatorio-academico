# 📊 Relatório Acadêmico — Automação com Python

Projeto desenvolvido em Python para automatizar a análise do desempenho acadêmico de alunos utilizando planilhas Excel.

A aplicação lê os dados de uma planilha, identifica alunos aprovados e reprovados, gera relatórios separados e apresenta estatísticas gerais da turma diretamente no terminal.

---

## 🎯 Funcionalidades

- 📂 Leitura automática de arquivos Excel.
- 👨‍🎓 Processamento dos registros dos alunos.
- ✅ Identificação de alunos aprovados (nota ≥ 7.0).
- ❌ Identificação de alunos reprovados (nota < 7.0).
- 📑 Geração automática de relatórios em Excel.
- 📈 Cálculo da média geral da turma.
- 🏆 Identificação do aluno com a maior nota.
- 📁 Organização automática dos relatórios em uma pasta específica.

## 🛠️ Tecnologias utilizadas

- **Python** — Linguagem principal.
- **OpenPyXL** — Leitura, criação e manipulação de planilhas Excel.
- **OS** — Gerenciamento de diretórios e arquivos.

## 📁 Estrutura do projeto

```text
relatorio_academico/
│
├── criar_planilha.py
├── main.py
├── alunos.xlsx
│
└── relatorios/
    ├── aprovados.xlsx
    └── reprovados.xlsx
```

## ⚙️ Como executar

**1. Clone o repositório**

```bash
git clone URL_DO_REPOSITORIO
```

**2. Entre na pasta do projeto**

```bash
cd relatorio_academico
```

**3. Instale a dependência**

```bash
pip install openpyxl
```

**4. Gere a planilha de alunos**

```bash
python criar_planilha.py
```

**5. Execute o programa principal**

```bash
python main.py
```

Após a execução, os relatórios serão gerados automaticamente dentro da pasta `relatorios`.

## 📊 Critérios de avaliação

| Classificação | Critério |
|---|---|
| Aprovado | Nota final maior ou igual a 7.0 |
| Reprovado | Nota final inferior a 7.0 |

## 💻 Exemplo de execução

```text
===== RELATÓRIO DA TURMA =====

Total de alunos: 30
Aprovados: 23
Reprovados: 7

Média da turma: 7.23
Maior nota: 9.7
Melhor aluno: Felipe

Relatórios gerados com sucesso!
```

*Os resultados acima são ilustrativos.*

## 🧠 Conceitos aplicados

Este projeto foi desenvolvido para colocar em prática conceitos fundamentais de programação:

- Estruturas condicionais (`if/else`).
- Estruturas de repetição (`for`).
- Listas e manipulação de dados.
- Funções e organização de código.
- Manipulação de arquivos.
- Bibliotecas externas.
- Automação de tarefas.
- Leitura e escrita de planilhas Excel.

---

## 👨‍💻 Autor

**Pedro Luizeto**

Estudante de programação com foco em Python, desenvolvimento de software e automação de processos.

🔗 [GitHub — Pedro-Luizeto](https://github.com/Pedro-Luizeto)

---

<p align="center">
  Desenvolvido com Python 🐍
</p>
