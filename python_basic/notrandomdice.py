import random

r#andom_number = random.randint(1,6) 
#-> if put it here, but return is "return random_number", the function is not call. it will return pre-gen number

def get_random_dice_roll():
    random_number = random.randint(1,6)
    return random_number

print(get_random_dice_roll())
print(get_random_dice_roll())
print(get_random_dice_roll())
print(get_random_dice_roll())