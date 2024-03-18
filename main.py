import random
import sys
import pygame
from Tools import Background, text_speech, Text


def pesn(naz):
    pygame.mixer.music.load(f"{naz}.mp3")
    pygame.mixer.music.play(-1)


WIDTH = 600
HEIGHT = 600
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
all_sprites = pygame.sprite.Group()
pygame.display.set_caption("Юлия Викторовна, мы вас очень очень любим")
running = True
BackGround = Background('img.png', [0, 0])
m = 'Добрый день!!! Приветствуем вас в межгалактическом центре приема писем имени Юлии Викторовны!!!' \
    'Вы Юлия Викторовна?????'
rect0, text0 = text_speech(
    pygame.font.Font('k.ttf', 20), m, (255, 255, 255),
    200, 100, False)
la = 1201
color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
sprite1 = Text('Да', 40, (255, 255, 40), 50, 50, 300, 300)
all_sprites.add(sprite1)
sprite2 = Text('Поддержка', 40, (255, 0, 0), 200, 50, 400, 550)
all_sprites.add(sprite2)
n = 0
ch = 0
p = 0
g = 0
love = 0
pesn('nach')


def randcol():
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)


def e():
    for i in range(1000):
        print('ВЫ НЕ ЮЛИЯ ВИКТОРОВНА!! ВОН!')


def a(r, t, color):
    global rect0, text0, m
    rect0, text0 = text_speech(
        pygame.font.Font('k.ttf', 40), m, color,
        r, t, False
    )


while running:
    screen.fill((225, 225, 225))
    screen.blit(BackGround.image, BackGround.rect)
    events = pygame.event.get()
    la -= 0.5
    if la % 500 == 0 and m[-1] == '?':
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    a(la, 100, color)
    if n >= 1:
        n += 1
        screen.fill((0, 0, 0))
    if n == 6000:
        pesn('n')
        n = -1
        m = "Что мы с Чулпан рисовали на руках маркером?"
        sprite1 = Text('Котиков', 40, randcol(), 200, 50, 100, 300)
        all_sprites.add(sprite1)
        sprite2 = Text('Цветочки', 40, randcol(), 200, 50, 300, 400)
        all_sprites.add(sprite2)
        sprite3 = Text('Пай кутэ', 40, randcol(), 200, 50, 400, 500)
        all_sprites.add(sprite3)
        BackGround = Background('img_1.png', [0, 0])
    if ch == 1:
        pesn('ch')
        ch = -1
        m = "что мы ели, когда вы опаздывали на родительское собрание?"
        sprite1 = Text('Пахлаву', 40, randcol(), 200, 50, 100, 300)
        all_sprites.add(sprite1)
        sprite2 = Text('Халву', 40, randcol(), 200, 50, 300, 400)
        all_sprites.add(sprite2)
        sprite3 = Text('Тортик', 40, randcol(), 200, 50, 400, 500)
        all_sprites.add(sprite3)
        BackGround = Background('ch.jpg', [0, 0])
    if p == 1:
        pesn('p')
        p = -1
        m = "Как можно назвать гошу используя две буквы?"
        sprite1 = Text('Ми', 40, randcol(), 200, 50, 100, 300)
        all_sprites.add(sprite1)
        sprite2 = Text('Хе', 40, randcol(), 200, 50, 300, 400)
        all_sprites.add(sprite2)
        sprite3 = Text('че', 40, randcol(), 200, 50, 400, 500)
        all_sprites.add(sprite3)
        BackGround = Background('p.jpg', [0, 0])
    if g == 1:
        pesn('g')
        g = -1
        m = "Любимое блюдо Гоши?"
        sprite1 = Text('Пельмени', 40, randcol(), 200, 50, 100, 300)
        all_sprites.add(sprite1)
        sprite2 = Text('Пастила', 40, randcol(), 200, 50, 300, 400)
        all_sprites.add(sprite2)
        sprite3 = Text('Роллы', 40, randcol(), 200, 50, 400, 500)
        all_sprites.add(sprite3)
        BackGround = Background('g.jpg', [0, 0])
    if love == 1:
        for i in all_sprites:
            all_sprites.remove(i)
        pesn('love')
        love = -1
        m = 'Юлия Викторовна, мы просто хотели сказать, что бы очень вас любим) Вот решили немного повспоминать, ' \
            'что у нас было)) Мы никогда вас не забудем. Спасибо вам за все, вечно ваши Гоша, ' \
            'Наташа, Полина и Чулпан.'
        BackGround = Background('love.jpg', [0, 0])
    if la == -1700:
        la = 1700
    for event in events:
        pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and sprite2.rect.collidepoint(pygame.mouse.get_pos()) and n == 0:
            m = "ВНИМАНИЕ!!!!! ПОПЫТКА ВЗЛОМА, ВЫЗЫВАЕМ ГРУППУ ПОДДЕРЖКИ"
            pesn('si')
            color = (255, 0, 0)
            all_sprites.remove(sprite2)
            all_sprites.remove(sprite1)
            n = 1
        if event.type == pygame.MOUSEBUTTONDOWN and n == -1:
            if sprite1.rect.collidepoint(pygame.mouse.get_pos()) or sprite3.rect.collidepoint(pygame.mouse.get_pos()):
                e()
                pygame.quit()
                sys.exit()
            if sprite2.rect.collidepoint(pygame.mouse.get_pos()):
                ch = 1
            n = -2
        if event.type == pygame.MOUSEBUTTONDOWN and ch == -1:
            if sprite2.rect.collidepoint(pygame.mouse.get_pos()) or sprite3.rect.collidepoint(pygame.mouse.get_pos()):
                e()
                pygame.quit()
                sys.exit()
            if sprite1.rect.collidepoint(pygame.mouse.get_pos()):
                p = 1
            ch = -2
        if event.type == pygame.MOUSEBUTTONDOWN and p == -1:
            if sprite2.rect.collidepoint(pygame.mouse.get_pos()) or sprite3.rect.collidepoint(pygame.mouse.get_pos()):
                e()
                pygame.quit()
                sys.exit()
            if sprite1.rect.collidepoint(pygame.mouse.get_pos()):
                g = 1
            p = -2
        if event.type == pygame.MOUSEBUTTONDOWN and g == -1:
            if sprite1.rect.collidepoint(pygame.mouse.get_pos()) or sprite3.rect.collidepoint(pygame.mouse.get_pos()):
                e()
                pygame.quit()
                sys.exit()
            if sprite2.rect.collidepoint(pygame.mouse.get_pos()):
                love = 1
            g = -2
    if sprite1.rect.collidepoint(pygame.mouse.get_pos()) and n == 0:
        sprite1.rect.x = random.randint(100, 500)
        sprite1.rect.y = random.randint(250, 500)
    screen.blit(text0, rect0)
    all_sprites.update()
    all_sprites.draw(screen)
    pygame.display.update()
