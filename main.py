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
    print(f"Нашли новый МЕЧ с атакой {rapier}")
    input_number = input("1 - Взять МЕЧ\n2 - Пройти мимо\n")
    input_number = valid_number(input_number)
    if input_number == "1":
        attack = rapier
        print(f"У Вас новый меч с атакой {attack}\n")
        return True
    else:
        return False


def heal_plus(heal: int) -> bool:
    """Событие выполнения хилла."""
    global hp
    print(f"Вы нашли ЯБЛОКО + {heal} к здоровью")
    hp += heal
    return True


def battle(monster_attack: int, monster_hp: int) -> bool:
    """Событие идет сражение."""
    global hp
    global attack
    global monster_counter
    print(f"БОЙ! Вы встрели монстра {monster_hp} хп {monster_attack} дамаг")
    input_number = input("1 - Начать бой\n2 - Убежать\n")
    input_number = valid_number(input_number)
    if input_number == "2":
        return True
    else:
        hp -= monster_attack
        if hp != 0 and hp > 0:
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
    event = ["БОЙ", "МЕЧ", "ЯБЛОКО", "ЯБЛОКО", "БОЙ"]
    action = random.randint(0, 4)
    event_action = event[action]

    if event_action == "БОЙ":
        monster_attack = random.randint(4, 6)
        monster_hp = random.randint(4, 6)
        battle(monster_attack, monster_hp)
        return None

    elif event_action == "МЕЧ":
        rapier = random.randint(11, 15)
        weapon(rapier)
        return None

    elif event_action == "ЯБЛОКО":
        heal = random.randint(4, 7)
        heal_plus(heal)
        return None


if __name__ == "__main__":
    while True:
        if monster_counter < 10 and hp > 0:
            game()
        if hp <= 0:
            print("ПОРАЖЕНИЕ!")
            sys.exit()
        if monster_counter == 10:
            print("ПОБЕДА! Вы убили 10 монстров\n")
            sys.exit()
