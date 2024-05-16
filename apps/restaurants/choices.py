"""Choices for Restaurants App."""

from django.db.models import TextChoices


class Specialty(TextChoices):
    """Choices for specialty of a restaurant."""

    VARIED = "varied", "Varied"
    CHILEAN = "chilean", "Chilean"
    PERUVIAN = "peruvian", "Peruvian"
    ARGENTINIAN = "argentinian", "Argentinian"
    MEXICAN = "mexican", "Mexican"
    ITALIAN = "italian", "Italian"
    FRENCH = "french", "French"
    JAPANESE = "japanese", "Japanese"
    CHINESE = "chinese", "Chinese"
    INDIAN = "indian", "Indian"
    THAI = "thai", "Thai"
    SPANISH = "spanish", "Spanish"
    RUSSIAN = "russian", "Russian"
    MOROCCAN = "moroccan", "Moroccan"
    KOREAN = "korean", "Korean"
    TURKISH = "turkish", "Turkish"
