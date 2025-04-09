from datetime import datetime
from typing import Dict, Any, Optional

from src.domain.entities.race import Race, Hippodrome, Weather
from src.domain.entities.enums import (
    Discipline, Specialite, ConditionSexe, Nature, NebulositeCode
)
from src.data_access.mappers.common_mapper import safe_enum_parse, parse_timestamp

def map_json_to_hippodrome(data: Dict[str, Any]) -> Hippodrome:
    """Convertit les données JSON en objet Hippodrome"""
    return Hippodrome(
        code=data.get("code", ""),
        libelle_court=data.get("libelleCourt", ""),
        libelle_long=data.get("libelleLong", "")
    )

def map_json_to_weather(data: Dict[str, Any]) -> Optional[Weather]:
    """Convertit les données JSON en objet Weather"""
    if not data:
        return None
        
    return Weather(
        date_prevision=parse_timestamp(data.get("datePrevision")),
        nebulosite_code=safe_enum_parse(NebulositeCode, data.get("nebulositeCode"), NebulositeCode.P0),
        nebulosite_libelle=data.get("nebulositeLibelleCourt", ""),
        nebulosite_description=data.get("nebulositeLibelleLong"),
        temperature=data.get("temperature", 0),
        force_vent=data.get("forceVent", 0),
        direction_vent=data.get("directionVent", "")
    )

def map_json_to_race(race_key: str, data: Dict[str, Any], date_str: str) -> Race:
    """Convertit les données JSON en objet Race"""
    try:
        day, month, year = map(int, date_str.split('_'))
        race_date = datetime(year, month, day).date()
    except (ValueError, IndexError):
        # En cas d'erreur de parsing de la date, utiliser la date actuelle
        print(f"Warning: Impossible de parser la date {date_str}")
        race_date = datetime.now().date()
    
    hippodrome = map_json_to_hippodrome(data.get("hippodrome", {}))
    weather = map_json_to_weather(data.get("meteo"))
    
    return Race(
        id=race_key,
        date=race_date,
        heure_depart=parse_timestamp(data.get("heureDepart")),
        montant_prix=data.get("montantPrix", 0),
        distance=data.get("distance", 0),
        discipline=safe_enum_parse(Discipline, data.get("discipline"), Discipline.ATTELE),
        specialite=safe_enum_parse(Specialite, data.get("specialite"), Specialite.TROT_ATTELE),
        nombre_participants=data.get("nombreDeclaresPartants", 0),
        condition_sexe=safe_enum_parse(ConditionSexe, data.get("conditionSexe"), ConditionSexe.MIXTE),
        hippodrome=hippodrome,
        meteo=weather,
        grand_prix_national_trot=data.get("grandPrixNationalTrot", False),
        montant_offert_1er=data.get("montantOffert1er"),
        montant_offert_2eme=data.get("montantOffert2eme"),
        montant_offert_3eme=data.get("montantOffert3eme"),
        nature=safe_enum_parse(Nature, data.get("nature"))
    )