from dataclasses import dataclass
from typing import Optional


@dataclass
class ChevalFeatures:
    """Caractéristiques d'un cheval pour une course spécifique"""
    musique: str  # Historique récent des performances
    age: int
    oeilleres: str
    deferre: Optional[str]
    nombre_courses: int
    nombre_victoires: int
    nombre_places: int
    nombre_places_second: int
    nombre_places_troisieme: int
    driver_change: bool
    avis_entraineur: Optional[str]
    indicateur_inedit: bool
    driver: str
    entraineur: str
    gains_carriere: int
    gains_victoires: int
    gains_place: int
    gains_annee_en_cours: int
    gains_annee_precedente: int