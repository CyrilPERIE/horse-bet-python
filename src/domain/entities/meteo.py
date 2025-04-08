from dataclasses import dataclass
from datetime import datetime


@dataclass
class Meteo:
    """Représente les conditions météorologiques lors d'une course"""
    date_prevision: datetime
    nebulosite_code: str
    nebulosite_libelle: str
    temperature: int
    force_vent: int
    direction_vent: str