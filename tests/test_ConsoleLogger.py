from datetime import datetime

import pytest

from CapsuleCore_logger import ConsoleLogger


class TestConsoleLogger:
    @pytest.fixture
    def logger(self):
        return ConsoleLogger()

    def test_info_logging_format(self, logger, capsys):
        """Verifica que el mensaje INFO tenga el formato, color y nivel correctos."""
        message = "Conexión establecida"
        logger.info(message)

        # Capturamos la salida de stderr
        captured = capsys.readouterr()
        output = captured.err

        # Verificamos componentes clave
        assert "[INFO]" in output
        assert message in output
        # Verifica el código de color ANSI para INFO (92m) y el RESET (0m)
        assert "\033[92m" in output
        assert "\033[0m" in output

    def test_error_logging_color(self, logger, capsys):
        """Verifica que el nivel ERROR use el color rojo (91m)."""
        logger.error("Fallo crítico")

        captured = capsys.readouterr()
        assert "\033[91m" in captured.err
        assert "[ERROR]" in captured.err

    def test_timestamp_presence(self, logger, capsys):
        """Verifica que la salida incluya un timestamp con formato HH:MM:SS."""
        logger.debug("Test de tiempo")

        captured = capsys.readouterr()
        # Buscamos el patrón [XX:XX:XX] usando regex simple o comprobando longitud
        # El timestamp está al inicio: "[HH:MM:SS]"
        timestamp_part = captured.err.split("]")[0].replace("[", "")

        # Validamos que el string se puede parsear como tiempo
        assert datetime.strptime(timestamp_part, "%H:%M:%S")

    @pytest.mark.parametrize(
        "level,color_code",
        [
            ("DEBUG", "\033[94m"),
            ("WARNING", "\033[93m"),
        ],
    )
    def test_all_levels(self, logger, capsys, level, color_code):
        """Prueba parametrizada para asegurar que cada nivel tiene su color respectivo."""
        method = getattr(logger, level.lower())
        method("Mensaje de prueba")

        captured = capsys.readouterr()
        assert color_code in captured.err
        assert f"[{level}]" in captured.err
