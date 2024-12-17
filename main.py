import pygame
import random
import Fractions

def create_stalker():
    print("\nДля створення нового NPC оберіть чи введіть необхідні дані.")
    name = input("Введіть ім\'я NPC: ")
    while True:
        rank = input("Введіть ранг NPC: ")
        try:
            rank = float(rank)
            if rank > 0:
                break
        except:
            print("Помилка: потрібно ввести число!\n")
    while True:
        print("Оберіть фракцію.")
        print("1. Чисте Небо")
        print("2. Нейтрали")
        print("3. Бандити")
        print("4. Військові")
        print("5. Долг")
        print("6. Свобода")
        print("7. Найманці")
        print("8. Моноліт")
        frac = input("> ")
        match frac:
            case '1':
                stalk = Fractions.ClearSky(rank, name)
                stalk.set_position(random.choice(range(button_width, screen_width - stalk.get_size())),
                                   random.choice(range(button_height, screen_height - stalk.get_size())))
                break
            case '2':
                stalk = Fractions.Neutral(rank, name)
                stalk.set_position(random.choice(range(button_width, screen_width - stalk.get_size())),
                                   random.choice(range(button_height, screen_height - stalk.get_size())))
                break
            case '3':
                stalk = Fractions.Bandit(rank, name)
                stalk.set_position(random.choice(range(button_width, screen_width - stalk.get_size())),
                                   random.choice(range(button_height, screen_height - stalk.get_size())))
                break
            case '4':
                stalk = Fractions.Military(rank, name)
                stalk.set_position(random.choice(range(button_width, screen_width - stalk.get_size())),
                                   random.choice(range(button_height, screen_height - stalk.get_size())))
                break
            case '5':
                stalk = Fractions.Dolg(rank, name)
                stalk.set_position(random.choice(range(button_width, screen_width - stalk.get_size())),
                                   random.choice(range(button_height, screen_height - stalk.get_size())))
                break
            case '6':
                stalk = Fractions.Swoboda(rank, name)
                stalk.set_position(random.choice(range(button_width, screen_width - stalk.get_size())),
                                   random.choice(range(button_height, screen_height - stalk.get_size())))
                break
            case '7':
                stalk = Fractions.Merc(rank, name)
                stalk.set_position(random.choice(range(button_width, screen_width - stalk.get_size())),
                                   random.choice(range(button_height, screen_height - stalk.get_size())))
                break
            case '8':
                stalk = Fractions.Monolit(rank, name)
                stalk.set_position(random.choice(range(button_width, screen_width - stalk.get_size())),
                                   random.choice(range(button_height, screen_height - stalk.get_size())))
                break
            case _:
                print("Некоректний вибір!\n")
    return stalk

if __name__ == '__main__':
    pygame.init()
    screen_width = 1024
    screen_height = 768
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Stalkers')

    clock = pygame.time.Clock()

    finish = False
    stalkers = []

    #button data
    color = (255, 255, 255)
    color_light = (170, 170, 170)
    color_dark = (100, 100, 100)
    smallfont = pygame.font.SysFont('Corbel', 35)
    button_x = 0
    button_y = 0
    button_width = 100
    button_height = 40
    text = smallfont.render('Create', True, color)
    ############
    black = (0, 0, 0)
    count = 0
    while not finish:
        screen.fill(black)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finish = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if button_x <= mouse[0] <= button_x + button_width and button_y <= mouse[1] <= button_y + button_height:
                    pygame.draw.rect(screen, color_light, [button_x, button_y, button_width, button_height])
                    stalk = create_stalker()
                    print("Інформація про утвореного NPC.")
                    print(stalk)
                    stalkers.append(stalk)

        if count == 100:
            params = []
            for i in stalkers:
                params.append(i.get_damage())
            for i in range(len(stalkers)):
                for j in range(i, len(stalkers)):
                    if i != j:
                        rep = stalkers[i].get_reputation(stalkers[j].get_fraction())
                        if rep >= 4500:
                            params[i] += 1.5 * stalkers[j].get_damage()
                            params[j] += 1.5 * stalkers[i].get_damage()
                        elif 2000 <= rep <= 4500:
                            params[i] += 0.75 * stalkers[j].get_damage()
                            params[j] += 0.75 * stalkers[i].get_damage()
                        elif rep <= -4500:
                            params[i] -= stalkers[j].get_damage()
                            params[j] -= stalkers[i].get_damage()
            for i in range(len(stalkers)):
                stalkers[i].change_life_params(params[i])
            i = 0
            while i < len(stalkers):
                if stalkers[i].get_health() == float(0):
                    stalkers.remove(stalkers[i])
                else:
                    i += 1
            count = 0
        else:
            count += 1
        mouse = pygame.mouse.get_pos()
        if button_x <= mouse[0] <= button_x + button_width and button_x <= mouse[1] <= button_y + button_height:
            pygame.draw.rect(screen, color_light, [button_x, button_y, button_width, button_height])
        else:
            pygame.draw.rect(screen, color_dark, [button_x, button_y, button_width, button_height])
        screen.blit(text, (0, 0))

        for stalker in stalkers:
            stalker.render(screen)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
