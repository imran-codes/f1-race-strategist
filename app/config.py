"""Application configuration helpers."""

from dotenv import load_dotenv


def load_environment() -> None:
    """Load local configuration without overriding shell environment values."""
    load_dotenv()
