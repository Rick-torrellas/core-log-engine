import logging

import pytest

from core_log_engine import SpecificLevelFilter

# Asumiendo que tu clase está en el mismo archivo o importada
# from mi_modulo import SpecificLevelFilter


def test_filter_allows_exact_level():
    """Verifica que el filtro permita pasar el nivel exacto."""
    filter_info = SpecificLevelFilter(level=logging.INFO)

    # Creamos un LogRecord que coincide
    record = logging.LogRecord(
        name="test", level=logging.INFO, pathname="", lineno=0, msg="Log de prueba", args=(), exc_info=None
    )

    assert filter_info.filter(record) is True


def test_filter_blocks_different_level():
    """Verifica que el filtro bloquee niveles distintos (incluso superiores)."""
    filter_error = SpecificLevelFilter(level=logging.ERROR)

    # Un registro de nivel CRITICAL no debería pasar si buscamos estrictamente ERROR
    record = logging.LogRecord(
        name="test", level=logging.CRITICAL, pathname="", lineno=0, msg="Log crítico", args=(), exc_info=None
    )

    assert filter_error.filter(record) is False


def test_init_with_string():
    """Verifica que la inicialización con string funcione correctamente."""
    filter_debug = SpecificLevelFilter(level="DEBUG")

    record = logging.LogRecord(name="test", level=logging.DEBUG, pathname="", lineno=0, msg="Debug log", args=(), exc_info=None)

    assert filter_debug.level == logging.DEBUG
    assert filter_debug.filter(record) is True


def test_init_with_none():
    """Verifica el comportamiento cuando el nivel es None."""
    filter_none = SpecificLevelFilter(level=None)

    record = logging.LogRecord(name="test", level=logging.INFO, pathname="", lineno=0, msg="Info log", args=(), exc_info=None)

    # Según la lógica record.levelno == None, debería ser False
    assert filter_none.filter(record) is False


@pytest.mark.parametrize(
    "level_input, expected_int",
    [
        ("INFO", logging.INFO),
        ("WARNING", logging.WARNING),
        (logging.ERROR, logging.ERROR),
    ],
)
def test_multiple_levels_parameterized(level_input, expected_int):
    """Prueba rápida de múltiples niveles usando parametrización."""
    f = SpecificLevelFilter(level=level_input)
    assert f.level == expected_int
