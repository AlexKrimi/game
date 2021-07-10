import random
from typing import Any

MONSTER_COUNTER = 0
HP = 15
ATTACK = 10


def generate_items(item: str) -> dict:
    '''
    Функция генерит случайные рандомные статы мечя, хилла яблока,
    статы монстра здоровье и атаку
    Args:
         Строка item, которая может содержит 3 актвинности
         'МЕЧ' - нужно создать меч
         'БОЙ' - нужно создать монстра
         'ЯБЛОКО' - нужно создать хилл
    Return:
        Словарь который может содержать информацию о
        Здоровье и атаке монстра (monster_hp, monster_attack),
        о атаке мечя (rapier),
        о здоровье хилла (heal)
    '''
    if item == 'БОЙ':
        monster_attack = random.randint(5, 10)
        monster_hp = random.randint(10, 15)
        return {'monster_attack': f'{monster_attack}',
                'monster_hp': f'{monster_hp}'}
    elif item == 'МЕЧ':
        rapier = random.randint(10, 25)
        return {'rapier': f'{rapier}'}
    else:
        heal = random.randint(7, 15)
        return {'heal': f'{heal}'}


def game()-> Any:
    '''
       Управляющая функция, которая запускает все остальные фунцкции
       Args:
           На вход ничего не подается
           action рандомное число для того выбирать случайно событие event
           Если event_action вернул heal тогда меняется здоровье рыцеря
           Если event_action вернул rapier тогда меняется атака рыцеря
           Если event_action вернул monster_attack и monster_hp тогда
            запускается фунция battle()
       Return:
           Возращает None если отработала часть с хиллом,заменной меча.
           Возращает True после победы над монстром и
           в случае смерти рыцеря возвращает false.
       '''
    global HP
    global ATTACK
    event = ['БОЙ', 'МЕЧ', 'ЯБЛОКО']
    action = random.randint(0, 2)
    event_action = generate_items(event[action])
    if 'heal' in event_action.keys():
        print(f'ЯБЛОКО, вы нашли лечение на {event_action["heal"]} HP\n')
        if int(event_action["heal"]) + HP >= 15:
            HP = 15
            return None
        else:
            diff_HP = int(event_action["heal"]) - 15
            return None

    elif 'rapier' in event_action.keys():
        print(f'Вы нашли МЕЧ с {event_action["rapier"]} ATTACK')
        if choice_rapier() == 1:
            ATTACK = int(event_action['rapier'])
            return None
        else:
            return None

    elif 'monster_attack' and 'monster_hp' in event_action.keys():
        print(f'БОЙ, вы встретили монстра. СТАТЫ: '
              f'{event_action["monster_hp"]} HP, '
              f'{event_action["monster_attack"]} ATTACK')
        # print(f'Ваше здоровье {HP} HP, ваша атака {ATTACK} ATTACK')
        if choice_monster() == 1:
            return battle(event_action)
    else:
        print('Ошибка')


def choice_rapier() -> int:
    '''
    Функция позволяет выбрать взять меч или пройти мимо
    Args:
        На вход ничего не подается
        take число с консоли 1 или 2
    Return:
        число 1 или 2
    '''
    while True:
        try:
            take = int(input('Введите число, чтобы начать действие: '
                             '\n1 - взять меч \n2 - пройти мимо\n').strip())
            if int(take) == 1 or int(take) == 2:
                return take
            else:
                print('Введите пожалуйста число 1 для того чтобы пропустить,'
                      '  2 для того чтобы взять предмет\n ')
        except ValueError:
            print('Попробуйте еще раз!\n')


def battle(event_action: dict) -> bool:
    '''
    Функция иметирует бой и определяет победил ли рыцарь или нет
    в случае если атака монстра > здоровья рыцеря и
    здоровье монстра < атака рыцеря - победа

     в случае если атака монстра == здоровью рыцеря и
    здоровье монстра < атака рыцеря - победа
    Args:
        Словарь event_action который содержит инф-ю
        о здоровье и атаке монстра, атаке меча, хилла яблока
        MONSTER_COUNTER глобальная переменная с кол-вом убитых монстров
        HP Здоровье рыцеря
        ATTACK атака рыцеря
    Return:
        Возвращает True в случае победы рыцеря и
        возвращает False в случае смерти рыцеря
        '''
    global ATTACK
    global HP
    global MONSTER_COUNTER
    if (int(event_action['monster_attack']) < HP) and \
            (int(event_action['monster_hp']) < ATTACK):
        MONSTER_COUNTER += 1
        HP -= int(event_action['monster_attack'])
        print(f'Поздравляю Вы убили {MONSTER_COUNTER}-го монстра')
        return True

    elif (int(event_action['monster_attack']) == HP) and \
            (int(event_action['monster_hp']) < ATTACK):
        MONSTER_COUNTER += 1
        HP -= int(event_action['monster_attack'])
        print(f'Поздравляю Вы убили {MONSTER_COUNTER}-го монстра')
        return True
    else:
        return False


def choice_monster() -> int:
    '''
       Функция позволяет выбрать атаковать чудовище или убежать с поля боя
       Args:
           На вход ничего не подается.
           take число с консоли 1 или 2
       Return:
           число 1 или 2
       '''
    while True:
        try:
            take = int(input('Введите число, чтобы начать действие: '
                             '\n1 - атаковать чудовище '
                             '\n2 - убежать\n').strip())
            if int(take) == 1 or int(take) == 2:
                return take
            else:
                print('Введите пожалуйста число 1 для того чтобы атаковать,'
                      '  2 для того чтобы убежать\n ')
        except ValueError:
            print('Попробуйте еще раз!\n')

while True:
    final = game()
    if final is None:
        continue
    elif final is False:
        print('ПОРАЖЕНИЕ! Вас убили')
        break
    elif final is True:
        if MONSTER_COUNTER < 10:
            continue
        elif MONSTER_COUNTER == 10:
            print('ПОБЕДА! Вы прошли игру')
            break
    else:
        print('ловим ошибки')


















