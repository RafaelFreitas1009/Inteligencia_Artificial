from dotenv import load_dotenv
import os, json, datetime, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
DIR_OUTPUTS = ROOT / "outputs"
DIR_LOGS = ROOT / "logs"
DIR_PROMPTS = ROOT / "prompts"
DIR_DATA = ROOT / "data"

def setup_env():
    load_dotenv()
    os.makedirs(DIR_OUTPUTS, exist_ok=True)
    os.makedirs(DIR_LOGS, exist_ok=True)

def read_text(path):
    return pathlib.Path(path).read_text(encoding="utf-8")

def write_text(path, content):
    pathlib.Path(path).write_text(content, encoding="utf-8")

def now_tag():
    return datetime.datetime.now().strftime("%Y%m%d_%H%M")

def save_log(payload: dict):
    log_path = DIR_LOGS / f"run_{now_tag()}.json"
    write_text(log_path, json.dumps(payload, ensure_ascii=False, indent=2))
    return log_path
