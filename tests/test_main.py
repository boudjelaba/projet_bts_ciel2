from main import main
from unittest.mock import patch
import builtins


def test_main_output(capsys):
    with patch.object(builtins, "input", return_value="Alice"):
        main()

    captured = capsys.readouterr()
    assert "Bonjour Alice" in captured.out
