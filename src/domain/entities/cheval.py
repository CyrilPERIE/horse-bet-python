from dataclasses import dataclass
from typing import Dict

from src.domain.entities.cheval_features import ChevalFeatures

@dataclass
class Cheval:
    """Représente un cheval participant à une course"""
    id: str  # Identifiant unique du cheval
    numero: int  # Numéro dans la course
    race_id: str  # Référence à la course
    features: ChevalFeatures
    odds: Dict[str, float]  # Cotes à différents moments (timestamp: cote)