from typing import TypeVar, Generic, Optional, Dict, Any
from dataclasses import dataclass

T = TypeVar('T')

@dataclass
class Error:
    """Représente une erreur lors d'une opération"""
    message: str
    code: str = "UNKNOWN_ERROR"
    details: Optional[Dict[str, Any]] = None
    exception: Optional[Exception] = None

@dataclass
class Method_Result(Generic[T]):
    """
    Pattern de résultat encapsulant succès/échec et données/erreurs.
    Permet de gérer les erreurs de manière cohérente sans exceptions.
    """
    is_success: bool
    error: Optional[Error] = None
    data: Optional[T] = None
    
    @classmethod
    def success(cls, data: T) -> 'Method_Result[T]':
        """Crée un résultat de succès avec les données"""
        return cls(is_success=True, data=data)
    
    @classmethod
    def failure(cls, message: str, code: str = "UNKNOWN_ERROR", 
              details: Optional[Dict[str, Any]] = None, 
              exception: Optional[Exception] = None) -> 'Method_Result[T]':
        """Crée un résultat d'échec avec les informations d'erreur"""
        error = Error(message=message, code=code, details=details, exception=exception)
        return cls(is_success=False, error=error)
    
    def on_success(self, func):
        """
        Exécute une fonction avec les données si le résultat est un succès
        Retourne this pour chaînage
        """
        if self.is_success and self.data is not None:
            func(self.data)
        return self
    
    def on_failure(self, func):
        """
        Exécute une fonction avec l'erreur si le résultat est un échec
        Retourne this pour chaînage
        """
        if not self.is_success and self.error is not None:
            func(self.error)
        return self

# Catalogue d'erreurs standard
class ErrorCodes:
    """Codes d'erreur standardisés"""
    VALIDATION_ERROR = "VALIDATION_ERROR"
    NOT_FOUND = "NOT_FOUND"
    PARSE_ERROR = "PARSE_ERROR"
    NETWORK_ERROR = "NETWORK_ERROR"
    DATA_INTEGRITY_ERROR = "DATA_INTEGRITY_ERROR"
    UNKNOWN_ERROR = "UNKNOWN_ERROR"