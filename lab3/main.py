import random
import temple


def main():
    print("Здравствуй, искатель приключений. Я помогу тебе выбраться.")
    print("Собери три части амулета и открой потайной ход.")
    temple.show_help()

    room = temple.START_ROOM
    parts = {1: True, 2: True, 3: True}  # какие части ещё лежат в залах
    inventory = 0
    amulet_used = False
    final = False

    temple.describe(room)

    while not final:
        now = input("\nЧто будете делать? ").strip().lower()

        if now == "exit":
            print("Вы покидаете храм. До встречи!")
            break

        elif now == "help":
            temple.show_help()

        elif now == "look":
            temple.describe(room)
            if room in ("frescoes", "treasury", "trap") and parts[temple.ROOMS[room]["part"]]:
                print("Кажется, здесь что-то блестит...")

        elif now.startswith("go "):
            direction = now[3:].strip()
            new_room, message = temple.move(room, direction)

            if new_room == "secret":
                if amulet_used:
                    print("Вы смогли выбраться!")
                    print("Победа!")
                    final = True
                    break
                else:
                    print("Проход закрыт. Сначала используйте амулет на алтаре.")
                    continue

            room = new_room
            print(message)
            temple.describe(room, short=True)

        elif now == "take":
            room_info = temple.ROOMS[room]
            part_id = room_info.get("part")

            if part_id and parts[part_id]:
                parts[part_id] = False
                inventory += 1
                print(f"Поздравляю! Вы нашли часть амулета ({inventory}/3).")
            else:
                print("Кажется, здесь больше ничего нет.")

        elif now == "use":
            if room == "altar":
                if temple.check_amulet(not parts[1], not parts[2], not parts[3]):
                    print("Поздравляю! Вы открыли тайный ход!")
                    amulet_used = True
                else:
                    print("У вас недостаточно частей амулета.")
            else:
                print("В этой комнате нельзя использовать амулет.")

        else:
            print("Прошу прощения, я не поняла, что вы хотите сделать.")

        # Случайное событие после каждого хода
        event = temple.random_event(room)
        if event:
            print(f"\n[Событие] {event}")

if __name__ == "__main__":
    main()
