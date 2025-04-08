from dataclasses import dataclass


@dataclass
class Hippodrome:
    """Représente un hippodrome"""
    code: str
    libelle_court: str
    libelle_long: str
