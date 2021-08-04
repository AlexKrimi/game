import random
from typing import Any
import sys

monster_counter = 0
hp = 10
attack = 10


def valid_number(number: str) -> str:
    """Проверка на ввод корректного числа."""
    while True:
        if number == "1" or number == "2":
            return number
        else:
            number = input("Для корректного ввода введите 1 или 2")


def weapon(rapier: int) -> bool:
    """Событие нахождение меча."""
    global attack
    print(f"Вы нашли новый МЕЧ {rapier} с атакой ")
    input_number = input(f"1 - Взять меч c атакой {rapier}\n2 - Пройти мимо\n")
    input_number = valid_number(input_number)
    if input_number == "1":
        attack = rapier
        print(f"Вы взяли меч с атакой {rapier}")
        return True
    else:
        return False


def heal_plus(heal: int) -> bool:
    """Событие выполнения хилла."""
    global hp
    print(f"Вы нашли хилл + {heal} к здоровью")
    hp += heal
    return True


def battle(monster_attack: int, monster_hp: int) -> bool:
    """Событие идет сражение."""
    global hp
    global attack
    global monster_counter
    print(f"БОЙ! Вы встрели монстра {monster_hp} хп {monster_attack} дамаг")
    input_number = input("1 - Начать бой 2 - Убежать")
    input_number = valid_number(input_number)
    if input_number == "2":
        return True
    else:
        hp -= monster_attack
        if hp > 0:
            if attack > monster_hp:
                monster_counter += 1
                print(f"Убито {monster_counter} монстров")
                return True
            else:
                return False
        else:
            hp = 0
            return False


def game() -> Any:
    """Основаня фунция запускает все события."""
    global monster_counter
    event = ["БОЙ", "МЕЧ", "ЯБЛОКО"]

    while monster_counter < 10 and hp > 0:
        action = random.randint(0, 2)
        if event[action] == "БОЙ":
            monster_attack = random.randint(2, 3)
            monster_hp = random.randint(2, 3)
            battle(monster_attack, monster_hp)

        elif event[action] == "МЕЧ":
            rapier = random.randint(11, 15)
            weapon(rapier)

        elif event[action] == "ЯБЛОКО":
            heal = random.randint(6, 8)
            heal_plus(heal)

    if hp <= 0:
        print("ПОРАЖЕНИЕ!")
    if monster_counter == 10:
        print("ПОБЕДА! Вы убили 10 монстров\n")
    sys.exit()
