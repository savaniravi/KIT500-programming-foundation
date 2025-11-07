"""
Vehicle Registration Program

This program allows users to input vehicle details and display various details about the vehicles.
It includes functionality to specify the vehicle type, number of drive wheels, and number of seats.
The program also gives the option to the user to add another car.
"""

__author__ = "Ravikumar Savani"

from enum import Enum
from dataclasses import dataclass
from typing import List, Optional

class CarType(Enum):
    """
    Enumeration for Car Types
    """
    ICE = "International combustion Engine (ICE)"
    HEV = "Hybrid BEVal Engine (HEV)"
    PHEV = "Plug-in hybrid BEV vehicle (PHEV)"
    BEV = "Battery electric Engine (BEV)"

@dataclass
class Car:
    """
    Data class for Car
    """
    registration: str
    num_drive_wheels: int
    num_seats: int
    vehicle_type: CarType

    def __str__(self):
        """
        Returns a string representation of the car.
        """
        vehicle_type = self.vehicle_type.value
        car_description = f"{self.registration}: {self.num_seats}-seat {self.num_drive_wheels} wheel drive {vehicle_type}"
        if self.num_seats <= 2:
            car_description += " coupe" 
        elif self.num_seats > 7:
            car_description += " people mover"
        return car_description

def input_vehicle_type() -> CarType:
    """
    Function to get car type from user
    """
    while True:
        print("Choose a car type:")
        for i, vehicle_type in enumerate(CarType, start=1):
            print(f"{i}. {vehicle_type.value}")
        choice = int(input("Enter your choice: "))
        if 1 <= choice <= len(CarType):
            return list(CarType)[choice - 1]  # Correct indexing here
        else:
            print("Invalid choice. Please try again.")

def input_car() -> Car:
    """
    Function to get car details from user
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
    return Car(registration, num_drive_wheels, num_seats, vehicle_type)

def add_many() -> List[Car]:
    """
    Function to get multiple records
    """
    num_records = int(input("Enter number of records to add: "))
    vehicles = []
    
    for i in range(num_records):
        print(f"Vehicle {i+1}:")
        vehicles.append(input_car())

    print("Your multiple inserted details are:")
    for vehicle in vehicles:
        print(vehicle)

    return vehicles

def most_seats(cars: List[Car], type: CarType) -> Optional[Car]:
    """
    Function to find the car of a particular type with the most seats.
    """
    has_most = None
    for car in cars:
        if car.vehicle_type == type:
            if has_most is None or car.num_seats > has_most.num_seats:
                has_most = car
    return has_most

def average_seats(cars: List[Car], type: CarType) -> float:
    """
    Function to calculate the average number of seats across cars of a particular type.
    """
    filtered_cars = [car for car in cars if car.vehicle_type == type]
    if not filtered_cars:
        return 0.0
    total_seats = sum(car.num_seats for car in filtered_cars)
    return total_seats / len(filtered_cars)

def display_all_cars(cars: List[Car]):
    """
    Display all cars, one per line
    """
    for car in cars:
        print(car)

def display_car_with_most_seats(cars: List[Car]):
    """
    Display the car (of a particular type) with the most seats
    """
    vehicle_type = input_vehicle_type()
    car = most_seats(cars, vehicle_type)
    if car:
        print(f"The {vehicle_type.value} car with the most seats is: {car}")
    else:
        print(f"No cars of type {vehicle_type.value} found.")

def display_average_seats(cars: List[Car]):
    """
    Display the average number of seats in cars of a particular type
    """
    vehicle_type = input_vehicle_type()
    average = average_seats(cars, vehicle_type)
    if average > 0:
        print(f"The average number of seats in {vehicle_type.value} cars is: {average:.2f}")
    else:
        print(f"No cars of type {vehicle_type.value} found.")

def main():
    """
    Main function
    """
    cars = add_many()  # Using add_many to get initial records

    while True:
        print("\nSelect an option:")
        print("1. Add another car.")
        print("2. Display all cars, one per line.")
        print("3. Display the car (of a particular type) with the most seats.")
        print("4. Display the average number of seats in cars of a particular type.")
        print("5. Quit.")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            car = input_car()
            cars.append(car)
            print("You entered:", car)
        elif choice == 2:
            display_all_cars(cars)
        elif choice == 3:
            display_car_with_most_seats(cars)
        elif choice == 4:
            display_average_seats(cars)
        elif choice == 5:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
