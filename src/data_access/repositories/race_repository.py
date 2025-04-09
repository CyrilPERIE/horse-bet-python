import os
import json
from datetime import date
from typing import List, Dict, Optional

from src.domain.entities.race import Race
from src.data_access.mappers.race_mapper import map_json_to_race

class RaceRepository:
    def __init__(self, base_path: str = "data/raw"):
        self.base_path = base_path
        self._available_years = self._scan_available_years()

    def _scan_available_years(self) -> List[int]:
        """Scan le répertoire de base pour trouver toutes les années disponibles"""
        years = []
        if os.path.exists(self.base_path):
            for item in os.listdir(self.base_path):
                year_dir = os.path.join(self.base_path, item)
                if os.path.isdir(year_dir) and item.isdigit():
                    years.append(int(item))
        return sorted(years)

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

    def get_race_by_id(self, race_id: str, race_date: date) -> Optional[Race]:
        """Récupère une course spécifique par son ID et sa date"""
        file_path = self._get_file_path(race_date)
        data = self._load_races_file(file_path)
        
        if race_id not in data:
            return None
            
        return map_json_to_race(race_id, data[race_id], race_date.strftime('%d_%m_%Y'))

    def get_races_by_date(self, race_date: date) -> List[Race]:
        """Récupère toutes les courses pour une date donnée"""
        file_path = self._get_file_path(race_date)
        data = self._load_races_file(file_path)
        
        races = []
        date_str = race_date.strftime('%d_%m_%Y')
        
        for race_id, race_data in data.items():
            race = map_json_to_race(race_id, race_data, date_str)
            if race:
                races.append(race)
                
        return races

    def get_races_by_hippodrome(self, hippodrome_code: str, year: Optional[int] = None) -> List[Race]:
        """Récupère toutes les courses d'un hippodrome pour une année donnée"""
        years_to_search = [year] if year else self._available_years
        races = []
        
        for year in years_to_search:
            year_dir = os.path.join(self.base_path, str(year))
            if not os.path.exists(year_dir):
                continue
                
            for file_name in os.listdir(year_dir):
                if not file_name.endswith('.json'):
                    continue
                    
                file_path = os.path.join(year_dir, file_name)
                data = self._load_races_file(file_path)
                
                date_str = file_name.replace('.json', '')
                
                for race_id, race_data in data.items():
                    if race_data.get('hippodrome', {}).get('code') == hippodrome_code:
                        race = map_json_to_race(race_id, race_data, date_str)
                        if race:
                            races.append(race)
                            
        return races

    def get_races_by_distance_range(self, min_distance: int, max_distance: int, 
                                  year: Optional[int] = None) -> List[Race]:
        """Récupère toutes les courses dans une plage de distance donnée"""
        years_to_search = [year] if year else self._available_years
        races = []
        
        for year in years_to_search:
            year_dir = os.path.join(self.base_path, str(year))
            if not os.path.exists(year_dir):
                continue
                
            for file_name in os.listdir(year_dir):
                if not file_name.endswith('.json'):
                    continue
                    
                file_path = os.path.join(year_dir, file_name)
                data = self._load_races_file(file_path)
                
                date_str = file_name.replace('.json', '')
                
                for race_id, race_data in data.items():
                    distance = race_data.get('distance', 0)
                    if min_distance <= distance <= max_distance:
                        race = map_json_to_race(race_id, race_data, date_str)
                        if race:
                            races.append(race)
                            
        return races

    def get_all_hippodromes(self) -> List[str]:
        """Récupère la liste de tous les hippodromes uniques"""
        hippodromes = set()
        
        for year in self._available_years:
            year_dir = os.path.join(self.base_path, str(year))
            if not os.path.exists(year_dir):
                continue
                
            for file_name in os.listdir(year_dir):
                if not file_name.endswith('.json'):
                    continue
                    
                file_path = os.path.join(year_dir, file_name)
                data = self._load_races_file(file_path)
                
                for race_data in data.values():
                    hippodrome_code = race_data.get('hippodrome', {}).get('code')
                    if hippodrome_code:
                        hippodromes.add(hippodrome_code)
                        
        return sorted(list(hippodromes))