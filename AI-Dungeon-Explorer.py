import random

class DungeonRoom:
    def __init__(self, description, monster, treasure):
        self.description = description
        self.monster = monster
        self.treasure = treasure

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack = 10
        self.defense = 5
        self.inventory = []

    def attack_monster(self, monster):
        damage = max(0, self.attack - monster.defense)
        monster.health -= damage
        return damage

class Monster:
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense

    def attack_player(self, player):
        damage = max(0, self.attack - player.defense)
        player.health -= damage
        return damage

def generate_dungeon():
    descriptions = [
        "a dark and musty room",
        "a brightly lit room with strange symbols on the walls",
        "a damp room with the sound of dripping water",
        "a room filled with ancient artifacts"
    ]
    monsters = [
        Monster("Goblin", 30, 5, 2),
        Monster("Skeleton", 25, 7, 3),
        Monster("Orc", 40, 10, 4),
        Monster("Dragon", 100, 15, 10)
    ]
    treasures = [
        "a shiny gold coin",
        "an ancient relic",
        "a magical potion",
        "a piece of rare jewelry"
    ]

    rooms = []
    for i in range(10):  # 10 rooms in the dungeon
        description = random.choice(descriptions)
        monster = random.choice(monsters)
        treasure = random.choice(treasures)
        rooms.append(DungeonRoom(description, monster, treasure))

    return rooms

def play_game(player):
    dungeon = generate_dungeon()

    for i, room in enumerate(dungeon):
        print(f"\nYou enter {room.description}.")
        
        if room.monster:
            print(f"A {room.monster.name} appears!")
            while room.monster.health > 0 and player.health > 0:
                action = input("Do you want to [a]ttack or [r]un? ").lower()
                if action == 'a':
                    damage = player.attack_monster(room.monster)
                    print(f"You deal {damage} damage to the {room.monster.name}.")
                    if room.monster.health > 0:
                        damage = room.monster.attack_player(player)
                        print(f"The {room.monster.name} deals {damage} damage to you.")
                elif action == 'r':
                    print("You run away to the previous room.")
                    break
            if player.health <= 0:
                print("You have been defeated!")
                break
            elif room.monster.health <= 0:
                print(f"You have defeated the {room.monster.name}!")

        if player.health > 0:
            print(f"You find {room.treasure} in the room.")
            player.inventory.append(room.treasure)
            print(f"Current Inventory: {player.inventory}")

    if player.health > 0:
        print("Congratulations, you have successfully explored the dungeon!")

# Main Game Loop
player_name = input("Enter your character's name: ")
player = Player(player_name)
play_game(player)
