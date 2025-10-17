# 🤖 Projeto: Inteligência Artificial Generativa

Este projeto foi desenvolvido como parte da **Atividade de um Projeto de Inteligência Artificial**, atendendo a todos os requisitos propostos para o projeto.
O trabalho consiste em **elaborar um texto e uma fábula narrativa sobre a evolução da IA**, utilizando ferramentas de **IA generativa (Python + API Gemini)**, além de gerar um **relatório técnico automatizado em PDF** via **Pandoc + XeLaTeX**.


```
## 📁 Estrutura do Projeto

📂 Inteligência Artificial
 ┣ 📂 data
 ┃ ┗ 📄 base_tecnica.md → Base conceitual da IA, ML e DL
 ┣ 📂 histórico
 ┣ 📂 logs
 ┃ ┗ 📄 run_YYYYMMDD_HHMM.json → Log de execução das requisições à API
 ┣ 📂 outputs
 ┃ ┣ 📄 cobertura_topicos.md → Tabela de cobertura dos tópicos abordados
 ┃ ┣ 📄 fabula.md → Texto da fábula gerado via IA
 ┃ ┣ 📄 relatorio.md → Relatório técnico em Markdown
 ┃ ┗ 📄 relatorio.pdf → Relatório final em PDF (gerado via XeLaTeX)
 ┣ 📂 prompts
 ┃ ┣ 📄 system.md → Prompt de contexto (instruções da IA)
 ┃ ┗ 📄 user_template.md → Estrutura da interação com o modelo
 ┣ 📂 src
 ┃ ┣ 📄 build_coverage.py → Gera a tabela de cobertura dos tópicos
 ┃ ┣ 📄 build_report.py → Converte o relatório final para PDF
 ┃ ┣ 📄 generate_fable.py → Gera a fábula narrativa com IA generativa
 ┃ ┗ 📄 utils.py → Funções utilitárias (logs, leitura e escrita)
 ┣ 📄 .env → Variáveis de ambiente (API_KEY)
 ┗ 📄 Requirements.txt → Dependências do projeto
```


## ⚙️ Instalação e Execução

### 🧩 1) Pré-requisitos

- [Python 3.10+](https://www.python.org/downloads/)
- [Pandoc](https://pandoc.org/installing.html)
- [MiKTeX (XeLaTeX)](https://miktex.org/download)
- Chave da **Gemini API**: crie em https://aistudio.google.com/app/apikey

### 🧰 2) Instalar dependências

```bash
pip install -r Requirements.txt
```

### 🔑3) Configurar o .env

Crie um arquivo `.env` na raiz com sua chave:

GOOGLE_API_KEY=AIza...sua_chave_aqui...

### ▶️ 4). Execute as etapas do projeto

#### Modo manual

1️⃣ Gerar o texto narrativo:

python -m src.generate_fable

Saída: `outputs/fabula.md`

2️⃣ Gerar a cobertura dos tópicos:

python -m src.build_coverage

👉 Saída: `outputs/cobertura_topicos.md`

3️⃣ Gerar o relatório completo (Markdown + PDF):

👉 Saída:

* `outputs/relatorio.md`
* `outputs/relatorio.pdf`

## 🧾 Outputs Gerados

| Arquivo                  | Descrição                                                                               |
| ------------------------ | ----------------------------------------------------------------------------------------- |
| `fabula.md`            | Texto narrativo gerado via IA sobre a história e evolução da Inteligência Artificial. |
| `cobertura_topicos.md` | Tabela que mostra os tópicos cobertos pela fábula.                                      |
| `relatorio.md`         | Documento consolidado contendo contexto, objetivos, metodologia e resultados.             |
| `relatorio.pdf`        | Versão final em PDF formatada via LaTeX.                                                 |
| `run_*.json`           | Log com as requisições e respostas da IA generativa.                                    |

## 📘 Requisitos Atendidos

✅ Utilização de **IA Generativa (Gemini API)** para produzir o conteúdo.

✅ Desenvolvimento e execução de **código Python** para geração automatizada.

✅ Estrutura de **prompts** e controle de versões.

✅ Geração de **relatório técnico automatizado** em Markdown e PDF via  **Pandoc + XeLaTeX** .

✅ Inclusão de **logs e rastreabilidade** das execuções.

✅ Organização modular e reprodutível do projeto.

## 🧠 Conclusão

O projeto atendeu a  **todos os requisitos da Atividade Proposta**, mostrando a integração entre **ferramentas de IA, automação em Python** e  **geração documental científica**.

A fábula e o relatório representam uma  **transposição textual criativa e técnica**, demonstrando como a Inteligência Artificial pode ser aplicada tanto na **produção de conhecimento** quanto na  **automatização de processos** .

## 💡 Autor

**Rafael Freitas de Paula**

📅 Outubro de 2025
