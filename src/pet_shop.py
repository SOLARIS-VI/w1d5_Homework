# WRITE YOUR FUNCTIONS HERE

def get_pet_shop_name(pet_shop):
    # return "Camelot of Pets"
    return pet_shop["name"]

def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

def add_or_remove_cash(pet_shop, amount):
    pet_shop["admin"]["total_cash"] += amount

def test_add_or_remove_cash_add(pet_shop, total_cash):
    pet_shop["admin"]["total_cash"] += 10
    pet_shop["admin"]["total_cash"] -= -10

def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]

def increase_pets_sold(pet_shop, sold):
    pet_shop["admin"]["pets_sold"] += sold













