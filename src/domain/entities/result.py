# src/domain/entities/result.py
from dataclasses import dataclass
from typing import Dict, List, Optional

from src.domain.entities.enums import TypePari

@dataclass
class RaceResult:
    """Résultat d'une course"""
    race_id: str
    ordre_arrivee: List[List[int]]  # Format des résultats officiels
    rapports_definitifs: Dict[TypePari, Dict[str, float]]  # Type de pari -> combinaison -> rapport
    
    def get_winner(self) -> Optional[int]:
        """Retourne le numéro du cheval gagnant"""
        if self.ordre_arrivee and len(self.ordre_arrivee) > 0:
            return self.ordre_arrivee[0][0]
        return None
    
    def get_podium(self) -> List[int]:
        """Retourne les numéros des 3 premiers chevaux"""
        podium = []
        for i in range(min(3, len(self.ordre_arrivee))):
            podium.extend(self.ordre_arrivee[i])
        return podium