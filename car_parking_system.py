import heapq
from collections import defaultdict, OrderedDict

class Car:
    def __init__(self, registration_number, age):
        self.registration_number = registration_number
        self.age = age

class Parking:
    def __init__(self):
        self.parking_slots_left = []
        self.slot_registration_number = dict()
        self.car_and_slot_number = OrderedDict()
        self.registration_number_and_age = defaultdict(list)

#function to create parking lot with N slots
    def create_parking_lot(self, total_slots):
        print("Created a parking lot with {} slots".format(total_slots))
        for i in range(1, total_slots + 1):
            heapq.heappush(self.parking_slots_left, i)
        return True

#to find a nearest slot for a car 
    def find_nearest_slot(self):
        if self.parking_slots_left:
          return heapq.heappop(self.parking_slots_left)
        else:
            None        

#function to park a car if slot is available
    def park_a_car(self, car):
        slot_number = self.find_nearest_slot()
        if slot_number is None:
            print(" Parking lot is full")
            return
        print("Car with registration-number: {} has been parked at slot number: {}".format(car.registration_number,slot_number))
        
        self.car_and_slot_number[slot_number] = car
        self.slot_registration_number[car.registration_number] = slot_number
        self.registration_number_and_age[car.age].append(car.registration_number)
        return slot_number

#function to make the slot available if a car leaves
    def leave(self, free_the_slot):
        car_to_leave = None
        for registration_no, slot in self.slot_registration_number.items():
            if slot == free_the_slot:
                car_to_leave = registration_no

        if car_to_leave:
            heapq.heappush(self.parking_slots_left, free_the_slot)
            del self.slot_registration_number[car_to_leave]
            car_left = self.car_and_slot_number[free_the_slot]
            self.registration_number_and_age[car_left.age].remove(car_to_leave)
            del self.car_and_slot_number[free_the_slot]
            print("Slot number {} is free".format(free_the_slot))
            return True

        else:
            print("slot not in use")
            return False

#function to return the slot number for a particular registration number
    def slot_number_for_registration_number(self, registration_number):
        slot_number = None
        if registration_number in self.slot_registration_number:
            slot_number = self.slot_registration_number[registration_number]
            print(slot_number)
            return slot_number
        else:
            print("Not found")
            return slot_number

# Slot numbers of all cars parked of a givem driver's age
    def slot_numbers_for_cars_with_driver_age(self, age):
        registration_numbers = self.registration_number_and_age[age]
        slots = [self.slot_registration_number[reg_nos] for reg_nos in registration_numbers]

        print("Slot numbers for cars having driver age {} :".format(age))
        print(", ".join(map(str, slots)))
        return slots

# Registration numbers of all cars of a given driver's age
    def registration_numbers_for_cars_with_driver_age(self, age):
        registration_numbers = self.registration_number_and_age[age]
        print(", ".join(registration_numbers))
        return self.registration_number_and_age[age]       

#function to display all the cars parked
    def display_all(self):
        print("Slot No.  Registration No     Age")
        for slot, car in self.car_and_slot_number.items():
            print("{}         {}       {}".format(slot, car.registration_number, car.age))
        return True  
