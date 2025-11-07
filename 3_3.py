"""
    3.3PP Functions
"""

__author__ = "Ravi Savani"

import math

def fun_greet(greet:str):                                       
    """
    function for greet to user
    """
    print(greet)

def fun_calc(tor: float, RPM: int) -> float:                    
    """
    function for calculate the power
    """
    return (tor * RPM * 2 * math.pi) / (60 * 1000)


def main():
   tor: float                                                   #Torque of the motor
   RPM: int                                                     #RPM of the motor
   pwd: float                                                   #Power of the motor
   
   fun_greet("Here you can calculate the power of motor.")      #Print for detail of the program
   print()                  
   fun_greet("Electric Motor Power Output.")
   
   print()
   
   print (f"GWM Ora : {fun_calc(250,5000)} kW")
   print (f"Polester 2 single motor : {fun_calc(490,4500)} kW")
   print()
   
   tor= float(input("Enter the value of Torque : "))
   RPM= int(input("Enter the value of RPM : "))
   print()
   
   pwd= fun_calc
   print (f"The power of the Electric motor is {fun_calc(tor, RPM)} kW")
   print()
   
if __name__ == "__main__":
    main()
