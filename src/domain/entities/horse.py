from dataclasses import dataclass
from typing import Dict, Optional

from src.domain.entities.enums import TypeOeilleres, TypeDeferre

@dataclass
class HorseFeatures:
    """Caractéristiques d'un cheval pour une course spécifique"""
    musique: str  # Historique récent des performances
    age: int
    oeilleres: TypeOeilleres
    deferre: TypeDeferre
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

@dataclass
class Horse:
    """Représente un cheval participant à une course"""
    id: str  # Identifiant unique du cheval
    numero: int  # Numéro dans la course
    race_id: str  # Référence à la course
    features: HorseFeatures
    odds: Dict[str, float]  # Cotes à différents moments (timestamp: cote)