
def rolldie(dice, mod=None):
    import random

    dice_lst = list(range(1, int(dice) + 1))

    if dice == None:
        print('No valid die was chosen... Defaulting to d6') 
        dice = 6
        dice_lst = list(range(1, dice + 1))
        print(f'You rolled a {random.choice(dice_lst)}!')
    
    else:
        print(f'You rolled a {random.choice(dice_lst)}!')
