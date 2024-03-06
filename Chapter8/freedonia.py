# Created for exercise 36 - Sales Tax
#  - Should provide a function calculate_tax()
#    - Takes 3 arguments:
#      - Purchase amount
#      - Province (Chico 50%, Groucho 70%, Harpo 50%, Zeppo 40%)
#      - Time of day (0-24, should be the percentage of tax amount)
#    - Should return final price as a float

class HourNotValidError(Exception): pass
class ProvinceNotValidError(Exception): pass

def calculate_tax(item_price, province, hour):
    provinces = {
        "Chico": .50,
        "Groucho": .70,
        "Harpo": .50,
        "Zeppo": .40
    }

    if province not in provinces:
        raise ProvinceNotValidError(f"Province {province} does not exist!")
    elif hour < 0 or hour > 24:
        raise HourNotValidError(f"Hour {hour} is not valid, its value must be between 0-24!")
    
    return f'{item_price + (item_price * (provinces[province] * (hour / 24))):.2f}'