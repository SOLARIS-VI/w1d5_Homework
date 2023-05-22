# WRITE YOUR FUNCTIONS HERE


# FIRST PASS TEST
def get_pet_shop_name(pet_shop):
    return pet_shop["name"]


# SECOND PASS TEST
def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]


# THIRD PASS TEST
def add_or_remove_cash(pet_shop, amount):
    pet_shop["admin"]["total_cash"] += amount


# FOURTH PASS TEST
def test_add_or_remove_cash_add(pet_shop, total_cash):
    pet_shop["admin"]["total_cash"] += 10
    pet_shop["admin"]["total_cash"] -= -10


# SOLUTION
# def add_or_remove_cash(pet_shop, amount):
#     pet_shop["admin"]["total_cash"] += amount


# FIFTH PASS TEST
def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]


# SIXTH PASS TEST
def increase_pets_sold(pet_shop, sold):
    pet_shop["admin"]["pets_sold"] += sold


# SOLUTION
# def get_pets_sold(pet_shop):
#     return pet_shop["admin"]["pets_sold"]


# SEVENTH PASS TEST
def get_stock_count(pet_shop):
    return len(pet_shop["pets"])


# SOLUTION
# def get_stock_count(pet_shop):
#     return len(pet_shop["pets"])


# EIGHTH & NINTH PASS TEST
def get_pets_by_breed(pet_shop, pet_name):
    pets = []
    for pet in pet_shop["pets"]:
        if pet["breed"] == pet_name:
            pets.append(pet)

    return pets


# SOLUTION
# def get_pets_by_breed(pet_shop, breed):
#     found_pets = []
#     for pet in pet_shop["pets"]:
#         if pet["breed"] == breed:
#             found_pets.append(pet)

#     return found_pets


# TENTH & ELEVENTH PASS TEST
def find_pet_by_name(pet_shop, pet_name):
    pets = pet_shop["pets"]
    for pet in pets:
        if pet["name"] == pet_name:
            return pet
    return None


# TWELFTH PASS TEST
def remove_pet_by_name(pet_shop, pet_name):
    for pet in pet_shop["pets"]:
        if pet["name"] == pet_name:
            pet_shop["pets"].remove(pet)


# THIRTEENTH PASS TEST
def add_pet_to_stock(pet_shop, new_pet):
     pet_shop["pets"].append(new_pet)















