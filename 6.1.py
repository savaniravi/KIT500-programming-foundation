"""
Vehicle Registration Program

This program allows users to input vehicle details and display a string representation of the vehicle.
It includes functionality to specify the vehicle type, number of drive wheels, and number of seats.

__author__ = "Ravikumar Savani"
"""

from enum import Enum
from dataclasses import dataclass

class VehicleType(Enum):
    """
    Enumeration for Vehicle Types
    """
    PETROL = "Petrol Engine"
    HYBRID = "Hybrid Engine"
    PLUG_IN_HYBRID = "Plug-in Hybrid Engine"
    ELECTRIC = "Electric Engine"

@dataclass
class Vehicle:
    """
    Data class for Vehicle
    """
    registration: str  # Vehicle registration number
    num_drive_wheels: int  # Number of drive wheels
    num_seats: int  # Number of seats
    vehicle_type: VehicleType  # Type of the vehicle

    def __str__(self):
        """
        Returns a string representation of the vehicle.
        """
        vehicle_type = self.vehicle_type.name
        vehicle_description = f"{self.registration}: {self.num_seats}-seat {self.num_drive_wheels} wheel drive {vehicle_type}"
        if self.num_seats < 3:
            vehicle_description += " coupe"
        elif self.num_seats > 7:
            vehicle_description += " people mover"
        elif self.num_seats <= 2: 
            vehicle_description += " compact vehicle"
        elif self.num_seats <= 5: 
            vehicle_description += " family vehicle"
        elif self.num_seats <= 8: 
            vehicle_description += " SUV"
        return vehicle_description

def input_vehicle_type():
    """
    Function to get vehicle type from user
    """
    while True:
        print("Choose a vehicle type:")
        for i, vehicle_type in enumerate(VehicleType, start=1):
            print(f"{i}. {vehicle_type.value}")
        choice = int(input("Enter your choice: "))
        if 1 <= choice <= len(VehicleType):
            return list(VehicleType)[choice - 1]  # Correct indexing here
        else:
            print("Invalid choice. Please try again.")

def input_vehicle():
    """
    Function to get vehicle details from user
    """
    registration = input("Enter registration: ")
    num_drive_wheels = int(input("Enter number of drive wheels: "))
    while True:
        num_seats = int(input("Enter number of seats: "))
        if num_seats >= 1:
            break
        else:
            print("Invalid number of seats. Please enter a value greater than or equal to 1.")
    vehicle_type = input_vehicle_type()
    return Vehicle(registration, num_drive_wheels, num_seats, vehicle_type)

def main():
    """
    Main function
    """
    print("Enter vehicle registration details")
    vehicle = input_vehicle()
    print("You entered:", vehicle)

if __name__ == "__main__":
    main()
