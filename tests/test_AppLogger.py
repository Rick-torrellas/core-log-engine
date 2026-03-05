import logging

import pytest

# Ajusta la importación según tu estructura real
from core_log_engine import AppLogger


class TestAppLogger:
    @pytest.fixture
    def app_logger(self):
        """Fixture para inicializar AppLogger con un nombre único para cada test."""
        return AppLogger("test_logger")

    def test_logger_name(self, app_logger):
        """Verifica que el logger interno de Python tenga el nombre asignado."""
        assert app_logger._logger.name == "test_logger"

    # --- Test Parametrizado para los Niveles de Log ---
    @pytest.mark.parametrize(
        "method_name, log_level, message",
        [
            ("debug", logging.DEBUG, "Mensaje de depuración"),
            ("info", logging.INFO, "Información del sistema"),
            ("warning", logging.WARNING, "Advertencia detectada"),
            ("error", logging.ERROR, "Error en el proceso"),
        ],
    )
    def test_logging_levels(self, app_logger, caplog, method_name, log_level, message):
        """
        Verifica dinámicamente que cada método de la interfaz Logger
        registre el nivel y mensaje correctos.
        """
        # Obtenemos el método de nuestra clase (info, debug, etc.)
        method = getattr(app_logger, method_name)

        # caplog captura logs a partir del nivel indicado
        with caplog.at_level(log_level):
            method(message)

        # Verificamos que al menos un registro coincida con lo esperado
        assert len(caplog.records) > 0
        last_record = caplog.records[-1]
        assert last_record.levelname == logging.getLevelName(log_level)
        assert last_record.message == message

    # --- Test de Robustez (Edge Case) ---
    def test_logging_non_string_objects(self, app_logger, caplog):
        """
        Verifica que el logger no falle si se le pasa un objeto (como una lista)
        en lugar de un string, ya que el logger interno debe manejar el __str__.
        """
        data = {"id": 1, "status": "active"}

        with caplog.at_level(logging.INFO):
            app_logger.info(data)

        assert str(data) in caplog.text

    # --- Test de Integridad del Contrato ---
    def test_implements_required_methods(self, app_logger):
        """
        Asegura que AppLogger tiene implementados los métodos esenciales
        del contrato Logger.
        """
        required_methods = ["info", "debug", "warning", "error"]
        for method_name in required_methods:
            assert hasattr(app_logger, method_name), f"Falta el método {method_name}"
            assert callable(getattr(app_logger, method_name)), f"{method_name} debe ser ejecutable"
