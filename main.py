import random

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = 10
        self.inventory = []

    def is_alive(self):
        return self.health > 0

    def attack(self, monster):
        damage = random.randint(5, self.attack_power)
        monster.health -= damage
        print(f"{self.name} атакует {monster.name} и наносит {damage} урона!")

    def player_characteristic(self):
        print(f" Имя - {self.name}")
        print(f" Здоровье - {self.health}")
        print(f" Сила атаки - {self.attack_power}")

    def regeneration (self):
        self.health += 15

    def power (self):
        self.attack_power += 5

    def timobruh (self):
        self.health -= 10


class Monster:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power


    def is_alive(self):
        return self.health > 0

    def attack(self, player):
        damage = random.randint(1, self.attack_power)
        player.health -= damage
        print(f"{self.name} атакует {player.name} и наносит {damage} урона!")

class Treasure:
    def __init__(self, name, value):
        self.name = name
        self.value = value

def create_monsters():
    return [
        Monster("Злого лолера", 30, 5),
        Monster("Люкс", 50, 7),
        Monster("Огненного дракона", 100, 15)
    ]

def create_treasures():
    return [
        Treasure("Поро", "Он бесценен"),
        Treasure( "Гриб Тимо","Ваши нервы",),
        Treasure("Кинжал", "300 золота"),
        Treasure("Тотальная печенька вечной воли", "... бесплатно!?!? это мне!?!?")
    ]


def main():
    print("Добро пожаловать в дешёвую пародию League of Legends! (Совет: удалите LOL со своего пк :)")
    player_name = input("Введите ваше имя: ")
    player = Player(player_name)

    monsters = create_monsters()
    treasures = create_treasures()

    while player.is_alive():
        action = input("Что вы хотите сделать? (фармить/унижать противников/инвентарь/состояние): ")

        if action == "состояние":
            print (player.player_characteristic())

        elif action == "фармить":
            treasure = random.choice(treasures)
            player.inventory.append(treasure)
            print(f"Вы нашли {treasure.name}! Стоимость: {treasure.value}!")

            if treasure.name == "Тотальная печенька вечной воли":
                print("Ваше здоровье увеличилось на 15 единиц!")
                player.regeneration()

            if treasure.name == "Кинжал":
                print("Ваша сила атаки увеличилась на 5 единиц!")
                player.power()

            if treasure.name == "Гриб Тимо":
                print("Походу вы  во что-то вляпались... Вы потеряли 10 единиц здоровья!")
                player.timobruh()

            if treasure.name == "Поро":
                print("Это же Поро! Он бесполезен, зато очень милый! Берём с собой!")


        elif action == "унижать противников":
            monster = random.choice(monsters)
            print(f"Вы встретили {monster.name}!")

            while monster.is_alive() and player.is_alive():
                player.attack(monster)
                if monster.is_alive():
                    monster.attack(player)

            if player.is_alive():
                print(f"Вы победили {monster.name}! (Вас вычислят по айпи)")
            else:
                print("Вы погибли... Ваша мама запретила вам играть в пк неделю.")

        elif action == "инвентарь":
            if player.inventory:
                print("Ваш инвентарь:")
                for item in player.inventory:
                    print( f" - Использованный(ая) {item.name}")
            else:
                print("Ваш инвентарь пуст.")

        else:
            print("Неверное действие. Попробуйте снова.")

    print("Спасибо за игру!")

if __name__ == "__main__":
    main()