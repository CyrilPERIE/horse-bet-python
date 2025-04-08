from enum import Enum

class Discipline(Enum):
    """Types de disciplines de courses"""
    ATTELE = "ATTELE"
    MONTE = "MONTE"
    PLAT = "PLAT"
    OBSTACLE = "OBSTACLE"

class Specialite(Enum):
    """Spécialités des courses"""
    TROT_ATTELE = "TROT_ATTELE"
    TROT_MONTE = "TROT_MONTE"
    GALOP_PLAT = "GALOP_PLAT"
    GALOP_OBSTACLE = "GALOP_OBSTACLE"

class ConditionSexe(Enum):
    """Conditions de sexe pour les courses"""
    MALES_ET_HONGRES = "MALES_ET_HONGRES"
    FEMELLES = "FEMELLES"
    MIXTE = "MIXTE"

class Nature(Enum):
    """Nature de la course (diurne/nocturne)"""
    DIURNE = "DIURNE"
    NOCTURNE = "NOCTURNE"

class TypeOeilleres(Enum):
    """Types d'oeillères portées par les chevaux"""
    SANS_OEILLERES = "SANS_OEILLERES"
    OEILLERES_AUSTRALIENNES = "OEILLERES_AUSTRALIENNES"
    OEILLERES_AMERICAINES = "OEILLERES_AMERICAINES"

class TypeDeferre(Enum):
    """Types de déferrage"""
    DEFERRE_ANTERIEURS = "DEFERRE_ANTERIEURS"
    DEFERRE_POSTERIEURS = "DEFERRE_POSTERIEURS"
    DEFERRE_ANTERIEURS_POSTERIEURS = "DEFERRE_ANTERIEURS_POSTERIEURS"
    NON_DEFERRE = None

class NebulositeCode(Enum):
    """Codes de nébulosité météo"""
    P0 = "P0"  # Ensoleillé
    P1 = "P1"  # Peu nuageux
    P2 = "P2"  # Partiellement nuageux
    P3 = "P3"  # Nuageux
    P4 = "P4"  # Très nuageux
    P5 = "P5"  # Couvert

class TypePari(Enum):
    """Types de paris disponibles"""
    E_SIMPLE_GAGNANT = "E_SIMPLE_GAGNANT"
    E_SIMPLE_PLACE = "E_SIMPLE_PLACE"
    E_COUPLE_GAGNANT = "E_COUPLE_GAGNANT" 
    E_COUPLE_PLACE = "E_COUPLE_PLACE"
    E_TRIO = "E_TRIO"
    E_SUPER_QUATRE = "E_SUPER_QUATRE"