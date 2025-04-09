from datetime import datetime
from typing import Any, Dict, Optional, TypeVar, Type, Callable

T = TypeVar('T')

def safe_enum_parse(enum_class: Type[T], value: Any, default: Optional[T] = None) -> Optional[T]:
    """Parse en toute sécurité une valeur vers une énumération"""
    if value is None:
        return default
    try:
        return enum_class(value)
    except (ValueError, KeyError):
        print(f"Warning: Valeur non reconnue {value} pour {enum_class.__name__}")
        return default

def parse_timestamp(timestamp: Optional[int]) -> Optional[datetime]:
    """Convertit un timestamp en millisecondes en datetime"""
    if timestamp is None:
        return None
    try:
        return datetime.fromtimestamp(timestamp/1000)
    except (ValueError, TypeError, OverflowError):
        print(f"Warning: Impossible de convertir le timestamp {timestamp}")
        return None

def extract_subdict(data: Dict[str, Any], keys: list[str]) -> Dict[str, Any]:
    """Extrait un sous-dictionnaire à partir des clés spécifiées"""
    return {k: data.get(k) for k in keys if k in data}