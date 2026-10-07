def compare_services():
    distance = positive_number("Distance (km): ")
    weight = positive_number("Weight (kg): ")
    standard = calculate_quote(distance, weight, "S")
    express = calculate_quote(distance, weight, "X")
    priority = calculate_quote(distance, weight, "P")

    print("Sevice comparison")
    print(f"Standard: {standard:.2f} SEK")
    print(f"Express: {express:.2f} SEK")
    print(f"Priority: {priority:.2f} SEK")

    cheapest = standard
    cheapest_name = "Standard"

    if express < cheapest:
        cheapest = express
        cheapest_name = "Express"

    if priority < cheapest:
        cheapest = priority
        cheapest_name = "Priority"

    most_expensive = standard
    most_expensive_name = "Standard"        

    if express > most_expensive:
        most_expensive = express
        most_expensive_name = "Express"

    if priority > most_expensive:
        most_expensive = priority 
        most_expensive_name = "Priority" 

    print(f"Cheapest service: {cheapest_name}") 
    print(f"Most expensive service: {most_expensive_name}")   

          