import logging
import logging.config
from typing import Optional, Union


class SpecificLevelFilter(logging.Filter):
    """Custom logging filter that only allows records with a specific log level."""

    def __init__(self, level: Union[int, str, None] = None) -> None:
        super().__init__()
        # Store the target level for filtering
        # If level is provided as string (e.g., "INFO"), convert to
        # corresponding integer constant
        if isinstance(level, str):
            self.level: Optional[int] = getattr(logging, level.upper())
        else:
            self.level = level

    def filter(self, record: logging.LogRecord) -> bool:
        """Determine if the specified record should be logged.

        Returns:
            bool: True only if the record's level exactly matches the configured level
        """
        return record.levelno == self.level
