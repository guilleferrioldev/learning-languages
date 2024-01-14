"""
#1 Too many parameters (do not pass many parameters to functions)
#2 Too deep nesting (Separate responsabilities)
#3 Not using the right data structure
#4 Nested conditional expressions
#5 Using wildcard imports
#6 Asymmetrical code
#7 Using self when it's not needed
#8 (BONUS): Not using a main() function
"""

from dataclasses import dataclass, field
from enum import Enum, auto 
import random
import string 
from datetime import datetime
from typing import Optional, Tuple

class FuelType(Enum):
    """Type of fuel used in a vehicle"""

    ELECTRIC = auto()
    PETROL = auto()

class RegistryStatus(Enum):
    """Possible statuses for the vehicle registry system"""

    ONLINE = auto()
    CONNECTION_ERROR = auto() 
    OFFLINE = auto()


taxes = {FuelType.ELECTRIC: 0.02, FuelType.PETROL: 0.05}


@dataclass 
class VehicleModelInfo: 
    """Class that contains basic information about a vehicle model"""
    
    brand: str 
    model: str
    catalogue_price: int 
    fuel_type: FuelType = FuelType.ELECTRIC 
    launch_year: int = datetime.now().date()

    @property 
    def tax(self) -> float:
        """Tax to be paid when registering a vehicle of this type"""

        tax_percentage = taxes[self.fuel_type]
        return tax_percentage * self.catalogue_price

    def __str__(self) -> str:
        return f"Brand: {self.brand} - type: {self.model} - tax: {self.tax} "


@dataclass 
class Vehicle:
    """Class representing a vehicle (electric or fossil fuel)"""

    vehicle_id: str 
    license_palce: str 
    info: VehicleModelInfo 
    
    def __str__(self) -> str:
        return f"Id: {self.vehicle_id}. License place: {self.license_palce}. Info: {self.info}"


@dataclass 
class VehicleRegistry:
    vehicle_models: dict[Tuple[str, str], VehicleModelInfo] = field(default_factory = dict)
    online: bool = field(default = True)

    def add_vehicle_model_info(self, model_info: VehicleModelInfo) -> None:
        """Helper method for adding a VehicleModelInfo object to a list"""
        self.vehicle_models[(model_info.brand, model_info.model)] = model_info
    
    @staticmethod
    def generate_vehicle_id(length: int) -> str:
        "Helper method for generating a random vehicle id"
        
        return "".join(random.choices(string.ascii_uppercase, k=length))
    
    @staticmethod
    def generate_vehicle_license(_id: str) -> str:
        "Helper method for generating a vehicle license number"
        digit_part = ''.join(random.choices(string.digits, k=2))
        letter_part = ''.join(random.choices(string.ascii_uppercase, k=2))
        return f"{_id[:2]}-{digit_part}-{letter_part}"
    
    def find_model_info(self, brand: str, model: str) -> Optional[VehicleModelInfo]:
        """Finds vehicle model info for a brand and model. If no info can be found, None is returned"""
        return self.vehicle_models.get((brand, model))

    def register_vehicle(self, brand: str, model: str) -> Vehicle:
        """Create a new vehicle and generate an id and a license plate"""
    
        if not (vehicle_model := self.find_model_info(brand, model)):    
            raise VehicleInfoError(brand, model)
        
        vehicle_id = self.generate_vehicle_id(12)
        license_place = self.generate_vehicle_license(vehicle_id)
        return Vehicle(vehicle_id, license_place, vehicle_model)
    

    def online_status(self) -> RegistryStatus:
        """Report whether the registry system is online"""
        
        if not self.online:
            return RegistryStatus.OFFLINE
        else:
            return (
                RegistryStatus.CONNECTION_ERROR
                if len(self.vehicle_models) == 0 
                else RegistryStatus.ONLINE
                )
        
def main() -> None:
     #create a registry instance 
    registry = VehicleRegistry()
        
    registry.add_vehicle_model_info(VehicleModelInfo("Tesla", "Model 3", 50000))
    registry.add_vehicle_model_info(VehicleModelInfo("VW", "ID3", 35000))
    registry.add_vehicle_model_info(VehicleModelInfo("BMW", "520e", 60000, FuelType.PETROL))
    registry.add_vehicle_model_info(VehicleModelInfo("Tesla", "Model Y", 55000))

    print(f"Registry status {registry.online_status()}")

    vehicle = registry.register_vehicle("VW", "ID3")

    print(vehicle)

if __name__ == "__main__":
    main()







    













