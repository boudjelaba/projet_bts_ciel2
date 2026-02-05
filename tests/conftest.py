import sys
from pathlib import Path

# Ajout de la racine du projet au début de sys.path pour que les imports top-level fonctionnent
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
