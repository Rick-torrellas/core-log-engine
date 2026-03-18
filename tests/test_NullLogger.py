import pytest

from CapsuleCore_logger import NullLogger


class TestNullLogger:
    @pytest.fixture
    def logger(self):
        """Fixture para proveer una instancia limpia de NullLogger."""
        return NullLogger()

    def test_null_logger_instantiation(self, logger):
        """Verifica que el logger se instancie correctamente."""
        assert isinstance(logger, NullLogger)

    @pytest.mark.parametrize("method_name", ["info", "debug", "warning", "error"])
    def test_methods_execute_without_error(self, logger, method_name):
        """
        Verifica que todos los métodos de log acepten un string
        y no retornen nada (o no lancen excepciones).
        """
        method = getattr(logger, method_name)

        # Ejecutamos el método. No debería pasar nada.
        result = method("Mensaje de prueba")

        assert result is None

    def test_methods_handle_different_types(self, logger):
        """
        Opcional: Verificar que el logger no explote si recibe algo
        que no sea estrictamente un string (tipado dinámico de Python).
        """
        try:
            logger.info(None)
            logger.error(123)
        except Exception as e:
            pytest.fail(f"NullLogger lanzó una excepción inesperada: {e}")
