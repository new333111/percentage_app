from pathlib import Path
from kivy.lang import Builder


def load_kv_files():

    kv_path = Path("kv")

    if not kv_path.exists():
        return

    for file in sorted(kv_path.glob("*.kv")):
        Builder.load_file(str(file))