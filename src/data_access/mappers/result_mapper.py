from typing import Dict, Any, Optional

from src.domain.entities.result import RaceResult
from src.domain.entities.enums import TypePari
from src.data_access.mappers.common_mapper import safe_enum_parse

def map_json_to_result(race_id: str, data: Dict[str, Any]) -> Optional[RaceResult]:
    """Convertit les données JSON en objet RaceResult"""
    if "ordreArrivee" not in data:
        return None
    
    # Convertir les clés de type de pari en énumérations
    rapports_definitifs = {}
    for pari_type_str, rapports in data.get("rapportsDefinitifs", {}).items():
        try:
            pari_type = safe_enum_parse(TypePari, pari_type_str)
            if pari_type:  # Ignorer les valeurs None (types de paris non reconnus)
                rapports_definitifs[pari_type] = rapports
        except (ValueError, KeyError):
            # Ignorer les types de paris non reconnus
            continue
    
    return RaceResult(
        race_id=race_id,
        ordre_arrivee=data["ordreArrivee"],
        rapports_definitifs=rapports_definitifs
    )