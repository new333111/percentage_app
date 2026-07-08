from pathlib import Path

from kivy.lang import Builder


def load_kv_files():

    kv_path = Path("kv")

    if not kv_path.exists():
        return

    files = sorted(kv_path.glob("*.kv"))

    for file in files:
        Builder.load_file(str(file))