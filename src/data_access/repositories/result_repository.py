import os
import json
from datetime import date
from typing import List, Optional, Dict, Set

from src.domain.entities.result import RaceResult
from src.data_access.mappers.result_mapper import map_json_to_result

class ResultRepository:
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

    def get_result_by_race(self, race_id: str, race_date: date) -> Optional[RaceResult]:
        """Récupère le résultat d'une course spécifique"""
        file_path = self._get_file_path(race_date)
        data = self._load_races_file(file_path)
        
        if race_id not in data:
            return None
            
        return map_json_to_result(race_id, data[race_id])

    def get_winning_horses(self, year: int) -> List[int]:
        """Récupère tous les numéros de chevaux gagnants pour une année donnée"""
        year_dir = os.path.join(self.base_path, str(year))
        if not os.path.exists(year_dir):
            return []
            
        winning_numbers = []
        for file_name in os.listdir(year_dir):
            if not file_name.endswith('.json'):
                continue
                
            file_path = os.path.join(year_dir, file_name)
            data = self._load_races_file(file_path)
            
            for race_id, race_data in data.items():
                result = map_json_to_result(race_id, race_data)
                if result and result.ordre_arrivee:
                    # Le premier numéro dans l'ordre d'arrivée est le gagnant
                    winning_numbers.append(result.ordre_arrivee[0])
                    
        return winning_numbers

    def get_results_by_date(self, race_date: date) -> List[RaceResult]:
        """Récupère tous les résultats des courses pour une date donnée"""
        file_path = self._get_file_path(race_date)
        data = self._load_races_file(file_path)
        
        results = []
        for race_id, race_data in data.items():
            result = map_json_to_result(race_id, race_data)
            if result:
                results.append(result)
                
        return results

    def get_placed_horses(self, year: int, top_n: int = 3) -> Dict[int, Set[int]]:
        """
        Récupère les numéros de chevaux placés (top N) pour une année donnée
        Retourne un dictionnaire {position: {numéros de chevaux}}
        """
        year_dir = os.path.join(self.base_path, str(year))
        if not os.path.exists(year_dir):
            return {i: set() for i in range(1, top_n + 1)}
            
        placed_horses = {i: set() for i in range(1, top_n + 1)}
        
        for file_name in os.listdir(year_dir):
            if not file_name.endswith('.json'):
                continue
                
            file_path = os.path.join(year_dir, file_name)
            data = self._load_races_file(file_path)
            
            for race_id, race_data in data.items():
                result = map_json_to_result(race_id, race_data)
                if result and result.ordre_arrivee:
                    for position in range(min(top_n, len(result.ordre_arrivee))):
                        placed_horses[position + 1].add(result.ordre_arrivee[position])
                        
        return placed_horses