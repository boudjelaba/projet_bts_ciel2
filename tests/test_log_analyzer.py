from log_analyzer import analyze_logs
from pathlib import Path


def test_analyze_logs(tmp_path):
    log_file = tmp_path / "log.txt"
    log_file.write_text(
        "INFO Démarrage\nERROR Problème\nINFO Fin\nERROR Autre\n"
    )

    total, errors = analyze_logs(log_file)

    assert total == 4
    assert errors == 2
