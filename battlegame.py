wizard ="Wizard"
elf = "Elf"
human = "Human"

wizard_hp = 70
elf_hp = 100
human_hp = 150

wizard_damage = 150
elf_damage = 100
human_damage = 20

dragon_hp = 300
dragon_damage = 50

while True:
    print("1) Wizard")
    print("2) Elf")
    print("3) Human")
    print("4) Kalisi")
    print("5) Exit")

    character_choice = input("Choose your character: ").lower()
    if character_choice == "wizard":
        my_hp = wizard_hp
        my_damage = wizard_damage
        break
    elif character_choice == "elf":
        my_hp = elf_hp
        my_damage = elf_damage
        break
    elif character_choice == "human":
        my_hp = human_hp
        my_damage = human_damage
        break
    elif character_choice == "kalisi":
        my_hp = kalisi_hp
        my_damage = kalisi_damage
        break
    else:
        print("Not a Valid character")

  
while True:
    dragon_hp = dragon_hp - my_damage
    print(f"The {character_choice}, damaged the Dragon! hp left is {dragon_hp}")
    if dragon_hp <= 0:
        print("The dragon has lost the battle")
        break
    my_hp = my_hp - dragon_damage
    print(f"The dragon damaged the {character_choice}! hp left is {my_hp}")
    if my_hp <= 0:
        print(f"{character_choice} has lost the battle")
        break