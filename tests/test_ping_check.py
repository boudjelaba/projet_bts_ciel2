from ping_check import ping
from unittest.mock import patch
import subprocess


def test_ping_success():
    with patch("subprocess.run") as mock_run:
        mock_run.return_value.returncode = 0
        assert ping("8.8.8.8") is True


def test_ping_failure():
    with patch("subprocess.run") as mock_run:
        mock_run.return_value.returncode = 1
        assert ping("invalid.host") is False
