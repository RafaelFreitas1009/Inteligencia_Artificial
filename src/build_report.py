import json, pathlib, datetime, shutil, subprocess
from src.utils import read_text, write_text, DIR_OUTPUTS, DIR_LOGS, DIR_PROMPTS, DIR_DATA

ROOT = pathlib.Path(__file__).resolve().parents[1]

def latest_log_path():
    logs = sorted(DIR_LOGS.glob("run_*.json"))
    return logs[-1] if logs else None

def md_section(title, body=""):
    return f"# {title}\n\n{body.strip()}\n\n"

def hr():  # linha horizontal
    return "\n---\n\n"

def try_pandoc(md_path, pdf_path):
    pandoc = shutil.which("pandoc")
    if not pandoc:
        print("ℹ️ Pandoc não encontrado. Pulei a geração de PDF.")
        return
    try:
        subprocess.run(["pandoc", md_path, "-o", pdf_path, "--pdf-engine=xelatex"], check=True)
        print(f"✅ PDF gerado em: {pdf_path}")
    except Exception as e:
        print("⚠️ Falha ao gerar PDF via pandoc:", e)

def main():
    # entradas necessárias
    fabula_md = DIR_OUTPUTS / "fabula.md"
    cobertura_md = DIR_OUTPUTS / "cobertura_topicos.md"
    base_md = DIR_DATA / "base_tecnica.md"

    if not fabula_md.exists():
        raise FileNotFoundError("outputs/fabula.md não encontrado. Rode antes: python -m src.generate_fable")
    if not cobertura_md.exists():
        raise FileNotFoundError("outputs/cobertura_topicos.md não encontrado. Rode antes: python -m src.build_coverage")
    if not base_md.exists():
        print("⚠️ data/base_tecnica.md não encontrado (seguirei sem anexar o texto técnico).")

    # metadados (último log)
    log_path = latest_log_path()
    log_data = {}
    if log_path and log_path.exists():
        log_data = json.loads(log_path.read_text(encoding="utf-8"))

    hoje = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
    titulo = "Relatório — Transposição Narrativa (Fábula) com IA Generativa"

    # ===== Montagem do relatório =====
    partes = []

    # Capa
    capa = f"""\
**{titulo}**  
Data de geração: {hoje}

Alune: Rafael Freitas de Paula  
Disciplina: Introdução à Inteligência Artificial (UFMA)
"""
    partes.append(capa + hr())

    # Contexto
    contexto = """\
A atividade consiste em transpor um conteúdo técnico (IA, ML, Deep Learning e suas aplicações)
para o **formato de fábula**, narrada pela própria IA, conforme especificação do professor.
O processo deveria ser realizado com **ajuda (não exclusiva)** de IA generativa via **Python + API**.
"""
    partes.append(md_section("1. Contexto", contexto))

    # Objetivos
    objetivos = """\
**Geral:** Comunicar conceitos e evolução da IA em linguagem acessível, por meio de narrativa.

**Específicos:**
- Reforçar os **conceitos básicos** de IA, ML e Deep Learning e suas **aplicações**;
- Cobrir **mudanças históricas** (Dartmouth, LISP/Eliza, Deep Blue, avanços de ML/DL/IA generativa);
- Evidenciar a **interdisciplinaridade** (visão, linguagem, música/áudio, robótica).
"""
    partes.append(md_section("2. Objetivos", objetivos))

    # Metodologia
    params_txt = ""
    if log_data:
        params = log_data.get("params", {})
        params_txt = f"""\
**Modelo:** {log_data.get("model","(não informado)")}  
**Parâmetros:** temperature={params.get('temperature','-')}, top_k={params.get('top_k','-')}, top_p={params.get('top_p','-')}  
**Tamanho:** prompt≈{log_data.get('user_len','-')} chars • saída≈{log_data.get('output_len','-')} chars  
**Rastreabilidade:** prompt_sha256_12={log_data.get('user_sha256_12','-')}
"""
    metodologia = f"""\
**Arquitetura (pipeline):** Python → API (Gemini) → Pós-processamento (Markdown) → Cobertura de tópicos → (opcional) PDF/LaTeX.

**Engenharia de prompts:** prompts versionados em `prompts/system.md` (persona) e `prompts/user_template.md` (template).

**Parâmetros da API:**  
{params_txt if params_txt else "- Não há log disponível desta execução."}

**Controle de versões & reprodutibilidade:**  
- `requirements.txt` para dependências;  
- `logs/` com metadados de cada execução;  
- arquivos de prompt separados;  
- utilitários em `src/utils.py`.  
"""
    partes.append(md_section("3. Metodologia", metodologia))

    # Resultados: fábula + cobertura
    partes.append(md_section("4. Resultados"))

    partes.append("### 4.1 Fábula (texto gerado)\n")
    partes.append(read_text(fabula_md))

    partes.append("\n### 4.2 Cobertura dos Tópicos\n")
    partes.append(read_text(cobertura_md))

    # Discussão (modelo para você personalizar)
    discussao = """\
- **Limitações observadas:** possibilidade de alucinações, sensibilidade ao prompt, variação com temperature/top_p, custo/latência.  
- **Mitigações adotadas:** revisão humana, termos de busca no texto para validar cobertura, controle de versões e parâmetros registrados em `logs/`.  
- **Intervenção humana vs. modelo:** a IA gerou a narrativa; a curadoria, correções factuais e organização do relatório foram humanas.  
"""
    partes.append(md_section("5. Discussão", discussao))

    # (Opcional) Anexo com texto técnico
    if base_md.exists():
        partes.append(md_section("Anexo A — Texto Técnico Base"))
        partes.append(read_text(base_md))

    # Grava
    relacao = "\n".join(partes).strip() + "\n"
    rel_md = DIR_OUTPUTS / "relatorio.md"
    write_text(rel_md, relacao)
    print(f"✅ Relatório gerado em: {rel_md}")

    # Tentar PDF com pandoc (opcional)
    try_pandoc(str(rel_md), str(DIR_OUTPUTS / "relatorio.pdf"))

if __name__ == "__main__":
    main()
