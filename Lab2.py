print("Здравствуй, искатель приключений. Я помогу тебе выбраться")
print("Собери три части амулета и открой потайной ход")
print("доступные команды:")
print("help, look, go, take, use, exit.")
room = "entrance"
inventar = 0
useam = 0
part1 = 1
part2 = 1
part3 = 1
final = 0
now = input(f'Вы находитесь в {room}, что будете делать? ')
while now != 'exit' and final ==0:
    if now[:3] == 'use':
        if room == 'altar' and inventar == 3:
            print('Поздравляю! Вы открыли secret! ')
            useam = 1
        elif inventar < 3:
            print('У вас недостаточно частей амулета ')
        else:
            print('В этой комнате нельзя использовать амулет')
    elif now[:2] == 'go':
        rm = room
        room = now[3:]
        if room == 'secret' and useam == 1:
            print('Вы смогли выбраться!')
            print("Победа! ")
            final = 1
            break
        elif room == 'secret' and useam == 0:
            print('Проход закрыт, нужно сначала использовать амулет ')
        elif room != 'entrance' and room != 'frescoes' and room != 'treasury' and room != 'trap' and room != 'altar':
            print('Такой комнаты нет')
            room = rm
        print(f'Вы находитесь в {room}')
    elif now[0:4] == 'help':
        print("доступные команды:")
        print("help, look, go, take, use, exit. ")
    elif now[0:4] == 'look':
        if room == 'entrance':
            print('Длинный пустой коридор, пыль летает в воздухе. Каменные стены уходят вдаль, оставляя лишь несколько проходов.')
            print('Вы можете пойти в frescoes, treasury, trap, altar')
        elif room == 'frescoes':
            print('В этой комнате не так много предметов, один стол, одна полка. Зато стены украшены большим количеством разных фресок. Интересно, кто их рисовал?')
            if part1 == 1:
                print("Кажется на столе что-то блестит")
            print('Вы можете пойти в entrance, treasury, trap, altar')
        elif room == 'treasury':
            print('Самая заполненная комната. Много сундоков, полок, но они пустые. Ни единой золотой монетки или драгоценного камня. Кажется кто-то успел все обчистить до вас.')
            if part2 == 1:
                print("Кажется в том сундуке что-то блестит")
            print('Вы можете пойти в entrance, frescoes, trap, altar')
        elif room == 'trap':
            print('Пустая комната? Если не считать маленьких отверстий в стенах. Это похоже на ловушку со стрелами. Нужно быть осторожнее')
            if part3 == 1:
                print("Кажется на полу что-то блестит")
            print('Вы можете пойти в entrance, frescoes, treasury, altar')
        elif room == 'altar':
            print('По центру комнаты стоит большая статуя. Кажется это алтарь, на шее статуи отлично бы подошел амулет')
            print('Вы можете пойти в entrance, frescoes, treasury, trap')
    elif now[0:4] == 'take':
        if room == 'entrance':
            print('Кажется, здесь ничего нет ')
        elif room == 'frescoes':
            if part1 == 1:
                print('Поздравляю! Ты нашел часть амулета! ')
                inventar +=1
                part1 -=1
            else:
                print('Кажется, здесь больше ничего нет ')
        elif room == 'treasury':
            if part2 == 1:
                print('Поздравляю! Ты нашел часть амулета! ')
                inventar +=1
                part2 -=1
            else:
                print('Кажется, здесь больше ничего нет ')
        elif room == 'trap':
            if part3 == 1:
                print('Поздравляю! Ты нашел часть амулета! ')
                inventar +=1
                part3 -=1
            else:
                print('Кажется, здесь больше ничего нет ')
        elif room == 'altar':
            print('Кажется, здесь ничего нет ')
    else:
        print('Прошу прощения, я не поняла, что вы хотите сделать?')

    now = input()