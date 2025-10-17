from src.utils import read_text, write_text, DIR_OUTPUTS

TOPICOS = {
    "Conceitos básicos (IA/ML/DL) e aplicações": ["inteligência artificial", "aprendizado de máquina", "deep learning", "aplicações", "visão", "linguagem"],
    "Mudanças históricas (Dartmouth, LISP/Eliza, Deep Blue, DL)": ["Dartmouth", "LISP", "Eliza", "Deep Blue", "2010", "gera texto", "IA generativa"],
    "Interdisciplinaridade (visão, linguagem, música, robótica)": ["visão", "linguagem", "música", "robótica", "áudio", "imagem", "sensores"]
}

def main():
    fabula = read_text(DIR_OUTPUTS / "fabula.md").lower()
    linhas = ["| Tópico | Cobertura | Evidências (palavras-chave encontradas) |",
              "|-------|-----------|----------------------------------------|"]
    for nome, termos in TOPICOS.items():
        encontrados = [t for t in termos if t.lower() in fabula]
        cobertura = "✅" if encontrados else "⚠️"
        linhas.append(f"| {nome} | {cobertura} | {', '.join(encontrados) if encontrados else '-'} |")

    out = "\n".join(linhas)
    write_text(DIR_OUTPUTS / "cobertura_topicos.md", out)
    print("🗂️  Tabela de cobertura gerada em outputs/cobertura_topicos.md")

if __name__ == "__main__":
    main()
