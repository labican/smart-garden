from dataclasses import dataclass
from typing import Dict
from datetime import datetime, timezone

@dataclass
class Clima:
    temperature: Dict[str, float]
    humidity: Dict[str, float]
    precipitation: float
    solar_incidence: float
    request_time: datetime = datetime.now(timezone.utc)
    
    def to_dict(self) -> Dict[str, float]:
        """
        Convert the Clima object to a dictionary.
        """
        clima_dict = self.__dict__.copy()
        clima_dict['request_time'] = self.get_utc_time()
        return clima_dict
    
    def get_utc_time(self) -> float:
        """
        Get the UTC time of the request.
        """
        return self.request_time.strftime('%Y-%m-%d %H:%M:%S')