import os
import json
from datetime import date
from typing import List, Optional, Dict

from src.domain.entities.horse import Horse
from src.data_access.mappers.horse_mapper import map_json_to_horses, map_json_to_horse

class HorseRepository:
    def __init__(self, base_path: str = "data/raw"):
        self.base_path = base_path

    def _get_file_path(self, race_date: date) -> str:
        """Construit le chemin du fichier pour une date donnée"""
        return os.path.join(
            self.base_path,
            str(race_date.year),
            f"{race_date.strftime('%d_%m_%Y')}.json"
        )

    def _load_races_file(self, file_path: str) -> Dict:
        """Charge le fichier JSON des courses"""
        if not os.path.exists(file_path):
            return {}
        
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def get_horses_by_race(self, race_id: str, race_date: date) -> List[Horse]:
        """Récupère tous les chevaux participant à une course"""
        file_path = self._get_file_path(race_date)
        data = self._load_races_file(file_path)
        
        if race_id not in data:
            return []
            
        return map_json_to_horses(race_id, data[race_id])

    def get_horse_by_number_in_race(self, race_id: str, horse_number: int, race_date: date) -> Optional[Horse]:
        """Récupère un cheval spécifique dans une course par son numéro"""
        file_path = self._get_file_path(race_date)
        data = self._load_races_file(file_path)
        
        if race_id not in data:
            return None
            
        race_data = data[race_id]
        horse_features = race_data.get("horse_features", {})
        
        if str(horse_number) not in horse_features:
            return None
            
        features = horse_features[str(horse_number)]
        odds_data = race_data.get("rapports", {}).get(str(horse_number), {})
        
        return map_json_to_horse(race_id, horse_number, features, odds_data)

    def get_horses_by_driver(self, driver_name: str, year: int) -> List[Horse]:
        """Récupère tous les chevaux conduits par un driver donné sur une année"""
        year_dir = os.path.join(self.base_path, str(year))
        if not os.path.exists(year_dir):
            return []
            
        horses = []
        for file_name in os.listdir(year_dir):
            if not file_name.endswith('.json'):
                continue
                
            file_path = os.path.join(year_dir, file_name)
            data = self._load_races_file(file_path)
            
            for race_id, race_data in data.items():
                race_horses = map_json_to_horses(race_id, race_data)
                horses.extend([
                    horse for horse in race_horses 
                    if horse.features.driver.lower() == driver_name.lower()
                ])
                
        return horses

    def get_horses_by_trainer(self, trainer_name: str, year: int) -> List[Horse]:
        """Récupère tous les chevaux entraînés par un entraîneur donné sur une année"""
        year_dir = os.path.join(self.base_path, str(year))
        if not os.path.exists(year_dir):
            return []
            
        horses = []
        for file_name in os.listdir(year_dir):
            if not file_name.endswith('.json'):
                continue
                
            file_path = os.path.join(year_dir, file_name)
            data = self._load_races_file(file_path)
            
            for race_id, race_data in data.items():
                race_horses = map_json_to_horses(race_id, race_data)
                horses.extend([
                    horse for horse in race_horses 
                    if horse.features.entraineur.lower() == trainer_name.lower()
                ])
                
        return horses