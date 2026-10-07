def menu_option():
    option = int(input("Select Services: "))

    while option < 1 or option > 8 :
        print("Error - Select a service from 1 to 8.")
        option = int(input("Select Services: "))
                     
    return option

#choice = menu_option()
#print(choice) 

def positive_number(prompt):
    number = float(input(prompt))

    while number <= 0 :
        print("Error - Value must be greater than 0. ")
        number = float(input(prompt))

    return number

#distance = positive_number("Distance (km): ")
#weight = positive_number("Weight (kg): ")
#capacity = positive_number("Van Capacity (kg): ")
#print(distance)
#print(weight)
#print(capacity)

def service_code():
    code = input("Service code: ").upper()

    while code not in ["S", "X", "P"]:
        print("Error - Service code must be S, X or P.")
        code = input("Service code: ").upper()

    return code    

#service = service_code()
#print(service)

def non_negative_number(prompt):
    digit =float(input(prompt))

    while digit < 0 :
        print("Error - Value must be greater than or equal to 0. ")
        digit = float(input(prompt))

    return digit
#promised_minutes = non_negative_number("Promised Minutes: ")
#actual_minutes = non_negative_number("Actual Minutes: ")
#damaged_parcels = non_negative_number("Damaged Parcels: ")  
#print(promised_minutes)
#print(actual_minutes)
#print(damaged_parcels)

def delivery_counts():
    counts = input("Completed Deliveries: ").split(",")

    while len(counts) != 7:
        print("Error - Weekly report requires 7 delivery counts.")
        counts = input("Completed Deliveries: ").split(",")

        for value in counts:
            while int(value) < 0:
                 print("Error - Value must be greater or equal to 0.")
                 counts = input("Completed Deliveries: ").split(",")
                
              
    return counts
delivery = delivery_counts()    
print(delivery)







    
 