import os
import json
from datetime import date
from typing import Optional

from src.domain.entities.race import Race
from src.data_access.mappers.csv_mappers import map_json_to_race

class RaceRepository:
    """Repository pour accéder aux données de courses"""
     
    def __init__(self, base_path: str = "data/raw"):
        self.base_path = base_path
    
    
    def get_race_by_id(self, race_id: str, race_date: date) -> Optional[Race]:
        """Récupère une course par son ID et sa date"""
        date_str = race_date.strftime("%d_%m_%Y")
        year_str = str(race_date.year)
        file_path = os.path.join(self.base_path, year_str, f"{date_str}.json")
        
        if not os.path.exists(file_path):
            return None
        
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        if race_id not in data:
            return None
            
        return map_json_to_race(race_id, data[race_id], date_str)
        