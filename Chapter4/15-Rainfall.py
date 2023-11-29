# Rainfall
#  - Create a function get_rainfall() to track rainfall for cities
#    - Should ask user for city name
#      - In dict? Cool, add the rainfall amount reported to the entry
#      - Not in dict? Add city and rainfall amount to the dict
#    - On entering a blank line, spit out report of all cities and exit

def get_rainfall():
    rainfall_totals = {}
    while True:
        city_name = input("City Name: ").strip()
        if not city_name:
            break
        
        if city_name not in rainfall_totals:
            rainfall_totals[city_name] = 0
        
        rainfall_amount = int(input("Rainfall in mm: ").strip())
        rainfall_totals[city_name] += rainfall_amount
    
    for k, v in rainfall_totals.items():
        print(f"{k}: {v}")

if __name__ == '__main__':
    get_rainfall()