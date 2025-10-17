from google import genai
from google.genai.types import GenerateContentConfig
import os, hashlib
from src.utils import setup_env, read_text, write_text, save_log, DIR_OUTPUTS, DIR_PROMPTS, DIR_DATA

MODEL = "gemini-2.5-flash"   # bom custo/benefício
TEMPERATURE = 0.7            # postura criativa controlada
TOP_K = 40
TOP_P = 0.95

def render_user_prompt(template: str, base_text: str) -> str:
    return template.replace("{{TEXTO_BASE}}", base_text.strip())

def main():
    setup_env()

    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise RuntimeError("GOOGLE_API_KEY não encontrada no .env.")

    client = genai.Client(api_key=api_key)

    # prompts
    system = read_text(DIR_PROMPTS / "system.md")
    user_template = read_text(DIR_PROMPTS / "user_template.md")
    base_tech = read_text(DIR_DATA / "base_tecnica.md")
    user = render_user_prompt(user_template, base_tech)

    # config (para rastreabilidade no relatório)
    config = GenerateContentConfig(
        system_instruction=system,
        temperature=TEMPERATURE,
        top_k=TOP_K,
        top_p=TOP_P,
        response_mime_type="text/plain"
    )

    # chamada à API
    resp = client.models.generate_content(
        model=MODEL,
        contents=user,
        config=config
    )

    text = resp.text.strip()

    # salva fábula
    out_path = DIR_OUTPUTS / "fabula.md"
    write_text(out_path, text)

    # log completo
    prompt_hash = hashlib.sha256(user.encode("utf-8")).hexdigest()[:12]
    log_payload = {
        "model": MODEL,
        "params": {"temperature": TEMPERATURE, "top_k": TOP_K, "top_p": TOP_P},
        "system_len": len(system),
        "user_len": len(user),
        "user_sha256_12": prompt_hash,
        "output_len": len(text),
        "output_preview": text[:240],
    }
    log_path = save_log(log_payload)

    print(f"✅ Fábula gerada em: {out_path}")
    print(f"🧾 Log salvo em:    {log_path}")

if __name__ == "__main__":
    main()
