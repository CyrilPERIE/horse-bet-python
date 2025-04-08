from datetime import datetime
from typing import Dict, Any, List, Optional

from src.domain.entities.race import Race, Hippodrome, Weather
from src.domain.entities.horse import Horse, HorseFeatures
from src.domain.entities.result import RaceResult
from src.domain.entities.enums import (
    Discipline, Specialite, ConditionSexe, Nature, 
    TypeOeilleres, TypeDeferre, NebulositeCode, TypePari
)

def map_json_to_race(race_key: str, data: Dict[str, Any], date_str: str) -> Race:
    """Convertit les données JSON en objet Race"""
    date = datetime.strptime(date_str, "%d_%m_%Y")
    
    hippodrome = Hippodrome(
        code=data["hippodrome"]["code"],
        libelle_court=data["hippodrome"]["libelleCourt"],
        libelle_long=data["hippodrome"]["libelleLong"]
    )
    
    weather = None
    if "meteo" in data:
        weather = Weather(
            date_prevision=datetime.fromtimestamp(data["meteo"]["datePrevision"]/1000),
            nebulosite_code=NebulositeCode(data["meteo"]["nebulositeCode"]),
            nebulosite_libelle=data["meteo"]["nebulositeLibelleCourt"],
            nebulosite_description=data["meteo"].get("nebulositeLibelleLong"),
            temperature=data["meteo"]["temperature"],
            force_vent=data["meteo"]["forceVent"],
            direction_vent=data["meteo"]["directionVent"]
        )
    
    return Race(
        id=race_key,
        date=date,
        heure_depart=datetime.fromtimestamp(data["heureDepart"]/1000),
        montant_prix=data["montantPrix"],
        distance=data["distance"],
        discipline=Discipline(data["discipline"]),
        specialite=Specialite(data["specialite"]),
        nombre_participants=data["nombreDeclaresPartants"],
        condition_sexe=ConditionSexe(data["conditionSexe"]),
        hippodrome=hippodrome,
        meteo=weather,
        grand_prix_national_trot=data.get("grandPrixNationalTrot", False),
        montant_offert_1er=data.get("montantOffert1er"),
        montant_offert_2eme=data.get("montantOffert2eme"),
        montant_offert_3eme=data.get("montantOffert3eme"),
        nature=Nature(data.get("nature")) if data.get("nature") else None
    )

def map_json_to_horses(race_key: str, data: Dict[str, Any]) -> List[Horse]:
    """Convertit les données JSON en liste d'objets Horse"""
    horses = []
    
    for num_str, features in data.get("horse_features", {}).items():
        num = int(num_str)
        
        # Récupérer les cotes du cheval
        odds = {}
        if num_str in data.get("rapports", {}):
            odds = {ts: float(val) for ts, val in data["rapports"][num_str].items()}
        
        horse_features = HorseFeatures(
            musique=features.get("musique", ""),
            age=features.get("age", 0),
            oeilleres=TypeOeilleres(features.get("oeilleres", "SANS_OEILLERES")),
            deferre=TypeDeferre(features.get("deferre")),
            nombre_courses=features.get("nombreCourses", 0),
            nombre_victoires=features.get("nombreVictoires", 0),
            nombre_places=features.get("nombrePlaces", 0),
            nombre_places_second=features.get("nombrePlacesSecond", 0),
            nombre_places_troisieme=features.get("nombrePlacesTroisieme", 0),
            driver_change=features.get("driverChange", False),
            avis_entraineur=features.get("avisEntraineur"),
            indicateur_inedit=features.get("indicateurInedit", False),
            driver=features.get("driver", ""),
            entraineur=features.get("entraineur", ""),
            gains_carriere=features.get("gainsCarriere", 0),
            gains_victoires=features.get("gainsVictoires", 0),
            gains_place=features.get("gainsPlace", 0),
            gains_annee_en_cours=features.get("gainsAnneeEnCours", 0),
            gains_annee_precedente=features.get("gainsAnneePrecedente", 0)
        )
        
        # Créer un ID unique pour le cheval (à améliorer si possible)
        horse_id = f"{features.get('driver', '')}-{features.get('entraineur', '')}-{num}"
        
        horse = Horse(
            id=horse_id,
            numero=num,
            race_id=race_key,
            features=horse_features,
            odds=odds
        )
        
        horses.append(horse)
    
    return horses

def map_json_to_result(race_key: str, data: Dict[str, Any]) -> Optional[RaceResult]:
    """Convertit les données JSON en objet RaceResult"""
    if "ordreArrivee" not in data:
        return None
    
    # Convertir les clés de type de pari en énumérations
    rapports_definitifs = {}
    for pari_type_str, rapports in data.get("rapportsDefinitifs", {}).items():
        try:
            pari_type = TypePari(pari_type_str)
            rapports_definitifs[pari_type] = rapports
        except ValueError:
            # Ignorer les types de paris non reconnus
            continue
    
    return RaceResult(
        race_id=race_key,
        ordre_arrivee=data["ordreArrivee"],
        rapports_definitifs=rapports_definitifs
    )