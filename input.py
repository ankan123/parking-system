import fileinput
import sys

from car_parking_system import Parking, Car
parking_system = Parking()

def process(input_text):
    params = input_text.strip().split(' ')
    instruction = params[0]

# to create parking lot of N slots
    if instruction == 'create_parking_lot':
         if len(params) == 2 and params[1].isdigit():
            parking_system.create_parking_lot(int(params[1]))
         else:
            print("no. of slots is needed to build a parking lot and it must be an integer")

# park a car with a registration number and driver's age
    elif instruction == 'park':
        if len(params) == 3:
            car = Car(params[1], params[2])
            parking_system.park_a_car(car)
        else:
            print("parking a car needs registration number and age as well")

# display all the cars parked with their slot number and reg. number in a table
    elif instruction == 'display_all':
        parking_system.display_all()

#output's slot number for a given registration number of a car
    elif instruction == 'slot_number_for_car_with_number':
        if len(params) == 2:
            parking_system.slot_number_for_registration_number(params[1])
        else:
            print("slot_number_for_registration_number needs registration_number to proceed") 

#output's all slot numbers of a given driver's age
    elif instruction == 'slot_numbers_for_cars_with_age':
        if len(params) == 2:
            parking_system.slot_numbers_for_cars_with_driver_age(params[1])
        else:
            print("slot_numbers_for_cars_with_age needs age to proceed")       

#output's registration numbers of a particular driver's age        
    elif instruction == 'registration_numbers_for_cars_with_age':
        if len(params) == 2:
            parking_system.registration_numbers_for_cars_with_driver_age(params[1])
        else:
            print("registration_numbers_for_cars_with_age needs age to proceed")

#when a car leaves the parking lot
    elif instruction == 'leave':
        #assert len(params) == 2, "leave needs slot number to proceed"
        if len(params) == 2 and params[1].isdigit():
            parking_system.leave(int(params[1]))
        else:
            print("it needs slot number for the car to leave or slot number must be a number")
        

#if any worng instructions is given       
    else:
        print("Instruction is wrong!!!!!!")


for line in fileinput.input():
    process(line)