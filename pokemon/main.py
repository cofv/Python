"""
fire > grass
fire < water
fire = electric
water < grass
water < electric
grass = electric

> 2x
= 1
>0,5x
"""
import random
class pokemon:
    def __init__(self, name, element, attack, defence, health):
        self.name = name
        self.element = element
        self.attack = attack
        self.defence = defence
        self.health = health
        
def calculate_damage(atk_type, def_type, attack, defence):
    effect = 1

    if atk_type == "fire" and def_type == "water":
        effect = 0.5
    if atk_type == "water" and def_type == "fire":
        effect = 2
    if atk_type == "grass" and def_type == "fire":
        effect = 0.5
    if atk_type == "fire" and def_type == "grass":
        effect = 2
    if atk_type == "water" and def_type == "grass":
        effect = 0.5
    if atk_type == "grass" and def_type == "water":
        effect = 2
    if atk_type == "water" and def_type == "electric":
        effect = 0.5
    if atk_type == "electric" and def_type == "water":
        effect = 2


    dmg = 50 * (attack/defence) * effect
    return dmg

pikachu = pokemon("pikachu", "electric", 100, 20, 200)
squirtle = pokemon("Squirtle", "water", 75, 100, 100)

choice = []
choice.append(pikachu)
choice.append(squirtle)

print("välj din pokemon!")

for i in range(len(choice)):
    print(i, choice[i].name)

player_choice = int(input())

player_pokemon = choice[player_choice]

computer_pokemon = random.choice(choice)

print(computer_pokemon.name)

damage_taken = calculate_damage(player_pokemon.element, computer_pokemon.element, player_pokemon.attack, computer_pokemon.defence)

print(player_pokemon.name, "dealt", round(damage_taken, 2), "to", computer_pokemon.name)
