from pathlib import Path

def get_project_root() -> Path:
    """
    Trova la root della repo in modo robusto.
    Se esegui notebook dentro /notebooks, risale di 1 livello.
    """
    cwd = Path.cwd()
    # caso tipico: repo/notebooks -> repo
    if cwd.name.lower() == "notebooks":
        return cwd.parent
    return cwd

PROJECT_ROOT = get_project_root()

# genera il path assoluto a partire da uno relativo alla root della repo
def abs_path(rel_posix: str) -> Path:
    """
    rel_posix: 'data/raw_flat/cardboard/cardboard2.jpg'
    """
    return PROJECT_ROOT / Path(rel_posix)
