import random

ROOMS = {
    "entrance": {
        "name": "Вход",
        "description": "Длинный пустой коридор, пыль летает в воздухе. "
                       "Каменные стены уходят вдаль, оставляя лишь несколько проходов.",
        "exits": ["frescoes", "treasury", "trap", "altar"],
    },
    "frescoes": {
        "name": "Зал фресок",
        "description": "В этой комнате не так много предметов: один стол, одна полка. "
                       "Зато стены украшены большим количеством разных фресок. "
                       "Интересно, кто их рисовал?",
        "exits": ["entrance", "treasury", "trap", "altar"],
        "part": 1,
    },
    "treasury": {
        "name": "Сокровищница",
        "description": "Самая заполненная комната. Много сундуков и полок, но они пустые. "
                       "Ни единой золотой монетки или драгоценного камня. "
                       "Кажется, кто-то успел всё обчистить до вас.",
        "exits": ["entrance", "frescoes", "trap", "altar"],
        "part": 2,
    },
    "trap": {
        "name": "Ловушка",
        "description": "Пустая комната? Если не считать маленьких отверстий в стенах. "
                       "Это похоже на ловушку со стрелами. Нужно быть осторожнее.",
        "exits": ["entrance", "frescoes", "treasury", "altar"],
        "part": 3,
    },
    "altar": {
        "name": "Алтарь",
        "description": "По центру комнаты стоит большая статуя. "
                       "Кажется, это алтарь — на шее статуи отлично бы подошёл амулет.",
        "exits": ["entrance", "frescoes", "treasury", "trap"],
    },
    "secret": {
        "name": "Тайный ход",
        "description": "Узкий проход, ведущий к выходу из храма.",
        "exits": [],
    },
}

START_ROOM = "entrance"
AMULET_PARTS_NEEDED = 3


def show_help():
    print("Доступные команды:")
    print("help, look, go, take, use, exit.")


def describe(room, short=False):
    info = ROOMS[room]
    print(f"Вы находитесь в: {info['name']} ({room})")
    if not short:
        print(info["description"])
    exits = ", ".join(info["exits"]) if info["exits"] else "выходов нет"
    print(f"Доступные переходы: {exits}")


def move(room, direction):
    exits = ROOMS[room]["exits"]
    if direction == "secret":
        return direction, f"Вы переходите в: {ROOMS[direction]['name']}"
    elif direction not in exits:
        return room, "Такого перехода нет из этого зала."
    return direction, f"Вы переходите в: {ROOMS[direction]['name']}"


def check_amulet(p1, p2, p3):
    return p1 and p2 and p3


def random_event(room):
    chance = random.random()

    if room == "trap" and chance < 0.3:
        return "Ловушка сработала! Стрелы свистят мимо вас — вы едва увернулись!"

    if chance < 0.1:
        return "Произошёл обвал! Часть потолка рухнула, но вы успели отскочить."

    if chance < 0.2:
        return "Вы нашли подсказку, нацарапанную на стене: «Три части — один путь»."

    return None