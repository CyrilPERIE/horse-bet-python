from typing import Dict, Any, List

from src.domain.entities.horse import Horse, HorseFeatures
from src.domain.entities.enums import TypeOeilleres, TypeDeferre
from src.data_access.mappers.common_mapper import safe_enum_parse

def map_json_to_horse_features(data: Dict[str, Any]) -> HorseFeatures:
    """Convertit les données JSON en objet HorseFeatures"""
    return HorseFeatures(
        musique=data.get("musique", ""),
        age=data.get("age", 0),
        oeilleres=safe_enum_parse(TypeOeilleres, data.get("oeilleres"), TypeOeilleres.SANS_OEILLERES),
        deferre=safe_enum_parse(TypeDeferre, data.get("deferre"), TypeDeferre.NON_DEFERRE),
        nombre_courses=data.get("nombreCourses", 0),
        nombre_victoires=data.get("nombreVictoires", 0),
        nombre_places=data.get("nombrePlaces", 0),
        nombre_places_second=data.get("nombrePlacesSecond", 0),
        nombre_places_troisieme=data.get("nombrePlacesTroisieme", 0),
        driver_change=data.get("driverChange", False),
        avis_entraineur=data.get("avisEntraineur"),
        indicateur_inedit=data.get("indicateurInedit", False),
        driver=data.get("driver", ""),
        entraineur=data.get("entraineur", ""),
        gains_carriere=data.get("gainsCarriere", 0),
        gains_victoires=data.get("gainsVictoires", 0),
        gains_place=data.get("gainsPlace", 0),
        gains_annee_en_cours=data.get("gainsAnneeEnCours", 0),
        gains_annee_precedente=data.get("gainsAnneePrecedente", 0)
    )

def map_json_to_horse(race_id: str, num: int, features_data: Dict[str, Any], odds_data: Dict[str, Any] = None) -> Horse:
    """Convertit les données JSON en objet Horse"""
    # Créer un ID unique pour le cheval (à améliorer si possible)
    driver = features_data.get("driver", "")
    entraineur = features_data.get("entraineur", "")
    horse_id = f"{driver}-{entraineur}-{num}"
    
    features = map_json_to_horse_features(features_data)
    
    # Récupérer les cotes
    odds = {}
    if odds_data:
        odds = {ts: float(val) for ts, val in odds_data.items()}
    
    return Horse(
        id=horse_id,
        numero=num,
        race_id=race_id,
        features=features,
        odds=odds
    )

def map_json_to_horses(race_id: str, data: Dict[str, Any]) -> List[Horse]:
    """Convertit les données JSON en liste d'objets Horse"""
    horses = []
    
    horse_features = data.get("horse_features", {})
    rapports = data.get("rapports", {})
    
    for num_str, features in horse_features.items():
        num = int(num_str)
        odds_data = rapports.get(num_str, {})
        
        horse = map_json_to_horse(race_id, num, features, odds_data)
        horses.append(horse)
    
    return horses