import os
from pathlib import Path
from dotenv import load_dotenv

print("Config loaded")

PROJECT_ROOT = Path.cwd().parent

def load_env():
    load_dotenv(PROJECT_ROOT / ".env")
    if(load_dotenv(PROJECT_ROOT / ".env")):
        print(".env loaded")
    else:
        print(".env loaded fail")

def get_key(name, default=None):
    return os.getenv(name, default)