from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from src.domain.entities.hippodrome import Hippodrome
from src.domain.entities.meteo import Meteo


@dataclass
class Course:
    """Représente une course de chevaux"""
    id: str  # Format "RxCy" (ex: "R1C1")
    date: datetime
    heure_depart: datetime
    distance: int
    discipline: str
    specialite: str
    nombre_participants: int
    condition_sexe: str
    hippodrome: Hippodrome
    meteo: Optional[Meteo] = None
    grand_prix_national_trot: bool = False
    montant_offert_1er: Optional[int] = None
    montant_offert_2eme: Optional[int] = None
    montant_offert_3eme: Optional[int] = None
    nature: Optional[str] = None