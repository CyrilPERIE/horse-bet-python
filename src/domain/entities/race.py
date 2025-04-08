from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from src.domain.entities.enums import (
    Discipline, Specialite, ConditionSexe, Nature, NebulositeCode
)

@dataclass
class Weather:
    """Représente les conditions météorologiques lors d'une course"""
    date_prevision: datetime
    nebulosite_code: NebulositeCode
    nebulosite_libelle: str
    nebulosite_description: Optional[str] = None
    temperature: int = 0
    force_vent: int = 0
    direction_vent: str = ""

@dataclass
class Hippodrome:
    """Représente un hippodrome"""
    code: str
    libelle_court: str
    libelle_long: str

@dataclass
class Race:
    """Représente une course de chevaux"""
    id: str  # Format "RxCy" (ex: "R1C1")
    date: datetime
    heure_depart: datetime
    montant_prix: int
    distance: int
    discipline: Discipline
    specialite: Specialite
    nombre_participants: int
    condition_sexe: ConditionSexe
    hippodrome: Hippodrome
    meteo: Optional[Weather] = None
    grand_prix_national_trot: bool = False
    montant_offert_1er: Optional[int] = None
    montant_offert_2eme: Optional[int] = None
    montant_offert_3eme: Optional[int] = None
    nature: Optional[Nature] = None