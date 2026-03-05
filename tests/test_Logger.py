from unittest.mock import MagicMock

import pytest

from core_log_engine import Logger


def test_logger_cannot_be_instantiated():
    """Verifica que la clase es verdaderamente abstracta."""
    with pytest.raises(TypeError):
        Logger()


def test_logger_interface_methods():
    """
    Verifica que una clase que hereda de Logger debe implementar sus métodos
    y que estos pueden ser llamados.
    """

    # Creamos una implementación concreta para el test
    class ConcreteLogger(Logger):
        def info(self, message: str):
            pass

        def debug(self, message: str):
            pass

        def warning(self, message: str):
            pass

        def error(self, message: str):
            pass

    logger_instance = ConcreteLogger()

    # Verificamos que sea instancia de la interfaz
    assert isinstance(logger_instance, Logger)


def test_logger_mock_behavior():
    """
    Simula el comportamiento de un logger real usando Mocks
    para asegurar que la interfaz responde a los argumentos correctos.
    """
    # Registramos Logger como una clase virtual para el mock
    mock_logger = MagicMock(spec=Logger)

    # Ejecutamos llamadas simuladas
    mock_logger.info("Mensaje de info")
    mock_logger.error("Mensaje de error")

    # Verificaciones
    mock_logger.info.assert_called_once_with("Mensaje de info")
    mock_logger.error.assert_called_once_with("Mensaje de error")
