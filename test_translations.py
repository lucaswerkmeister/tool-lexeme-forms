import toolforge
from toolforge_i18n import lang_autonym


toolforge.set_user_agent('lexeme-forms', email='mail@lucaswerkmeister.de')


def test_english_messages_exist(translations):
    """English is hard-coded as the final language fallback,
    so English messages must exist."""
    assert 'en' in translations


def test_language_code_leq_20(language_code: str):
    """We use 20 characters as an arbitrary limit for language setting length,
    so actual language codes must not be longer than that."""
    assert len(language_code) <= 20

def test_autonym_exists(language_code: str) -> None:
    """Autonyms are used e.g. in the settings page,
    they should exist and be nonempty."""
    assert lang_autonym(language_code)
