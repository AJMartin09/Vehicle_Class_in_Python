# Main,py

from vehiclePackage.vehicleClass import *

if __name__ == "__main__":
    # Let's instantiate an object of type Vehicle
    myCorvette = Vehicle("Car", 120) # Trigger a call to the constructor
    myCorvette.printType()      # Invoke the method on the object
    
    #Invoke the "getter" for Maximum speed, store the return value in a variable. Print that to the console.
    maximum_speed = myCorvette.getSpeed()
    print("Maximum Speed:", maximum_speed)
    
    # Instantiate another Vehicle object. You can name it
    myMini = Vehicle("Car", 80)   #myMini is an object of type vehicle
    
    #Give a list of 3 vehicles: Truck, Bus, Scooter
    # You can pick the names and properties
    # Give some friendly output to demo your work
    myVehicles = [Vehicle("Ford", 120),
                  Vehicle("Greyhound", 60),
                  Vehicle("Lime", 25)]
    for vehicle in myVehicles:
        vehicle.printType()
        print(vehicle.getSpeed())