# scripts/mkdocs_modules_hook.py
from mkdocs.structure.files import Files

def on_files(files, config):
    """Zostaw w buildzie TYLKO pliki z docs/modules/**."""
    kept = [f for f in files if f.src_uri.startswith("modules/")]
    return Files(kept)
