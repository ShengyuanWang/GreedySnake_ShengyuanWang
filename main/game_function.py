"""
Course: CS123
Professor: Susan Fox
Editor: Shengyuan Wang
This file includes all helpers for the main files.
"""
import pygame
import sys
import random
from pygame.locals import *


# check the keyboard operation in the start interface
def check_events(ai_settings):
    """
    to change the state of game according to the keyboard actions
    :param ai_settings: the setting of ai
    :return: return nothing, just change the variable of game state
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            elif event.key == pygame.K_1:
                ai_settings.game_stats = 5
            elif event.key == pygame.K_2:
                ai_settings.game_stats = 22
            elif event.key == pygame.K_F2:
                ai_settings.game_stats = 4


# draw the start interface
def show_start_interface(ai_settings, screen):
    """
    this function aims to draw the start interface
    :param ai_settings: the setting of ai
    :param screen: the screen input which we gonna draw
    :return: no return just draw the screen
    """
    title_Font = pygame.font.Font("../font/STXINGKA.TTF", 80)  # set the title font
    title_image = title_Font.render("Greedy Snake", True, (0, 0, 0))  #
    background = pygame.image.load(r"../image/background2.jpg")
    author_font = pygame.font.Font("../font/STXINGKA.TTF", 40)
    author_image = author_font.render(u"made by : Shengyuan Wang", True, (0, 0, 0))

    presskey_font = pygame.font.Font("../font/STKAITI.TTF", 35)  # set the description font
    presskey_image = presskey_font.render('press 1 to begin, press Esc to quit', True, (0, 0, 0))
    presskey_ai = presskey_font.render('press 2 to AI mode', True, (0, 0, 0))
    list_font = pygame.font.Font("../font/STKAITI.TTF", 35)  # set the rank description font
    list_image = list_font.render('press F2 to rank', True, (0, 0, 0))

    while True:

        screen.fill(ai_settings.bg_color)  # draw the screen
        screen.blit(background, (0, 0))  # put the background picture
        screen.blit(presskey_ai, (525, 250))
        screen.blit(title_image, (400, 50))  # draw the title
        screen.blit(presskey_image, (300, 160))  # draw the description words
        screen.blit(author_image, (400, 550))  # the author
        screen.blit(list_image, (525, 326))  # the rank image
        check_events(ai_settings)  # test keyboard
        if ai_settings.game_stats != 0:  # means someone press keyboard
            pygame.mixer.music.stop()
            break
        pygame.display.flip()


# check difficult level
def check_choose_events(ai_settings):
    """
    this function aims to check the difficult level chosen
    :param ai_settings: the setting of ai
    :return: to change the setting ai according to the keyboard action
    """
    for event in pygame.event.get():
        # press close or press ESC
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            # press 1 to choose difficult level1
            elif event.key == pygame.K_1:
                ai_settings.game_stats = 1
            # press 2 to choose difficult level2
            elif event.key == pygame.K_2:
                ai_settings.game_stats = 2
            # press 3 to choose difficult level3
            elif event.key == pygame.K_3:
                ai_settings.game_stats = 3
            elif event.key == pygame.K_F1:
                ai_settings.game_stats = 0


# draw difficult level choosing interface
def show_choose_level(ai_settings, screen):
    """
    this function aims to draw the difficult level choosing interface
    :param ai_settings: the setting of ai
    :param screen: the screen input we gonna draw
    :return: return nothing just change the drawing of the interface
    """
    background1 = pygame.image.load(r"../image/difficultlevel.jpg")
    level_font = pygame.font.Font("../font/STKAITI.TTF", 40)  # set difficulty choosing title
    level_image = level_font.render('↓ choose the difficult level ↓', True, (255, 255, 240))

    key1_font = pygame.font.Font("../font/STKAITI.TTF", 20)  # set description title
    key1_image = key1_font.render('press 1 to choose level1', True, (0, 0, 0))

    key2_font = pygame.font.Font("../font/STKAITI.TTF", 20)
    key2_image = key2_font.render('press 2 to choose level2', True, (0, 0, 0))

    key3_font = pygame.font.Font("../font/STKAITI.TTF", 20)
    key3_image = key3_font.render('press 3 to choose level3', True, (0, 0, 0))

    key4_font = pygame.font.Font("../font/STKAITI.TTF", 25)
    key4_image = key4_font.render('press F1 to return to main interface', True, (0, 0, 0))

    while True:
        screen.fill(ai_settings.bg_color)  # draw the screen
        screen.blit(background1, (0, 0))  # bg pic
        screen.blit(level_image, (100, 200))  # draw difficulty level chossing title
        screen.blit(key1_image, (150, 300))
        screen.blit(key2_image, (150, 400))
        screen.blit(key3_image, (150, 500))
        screen.blit(key4_image, (250, 550))

        check_choose_events(ai_settings)  # check keyboard
        if ai_settings.game_stats == 1 or ai_settings.game_stats == 2 or ai_settings.game_stats == 3 or ai_settings.game_stats == 0:
            break
        pygame.display.flip()


# drawing end interface, with game over in the center of the screen
def show_end_interface(ai_settings, screen):
    """
    this function aims to draw the end interface with game over int eh center of the screen
    :param ai_settings: the setting of ai
    :param screen: the screen input we gonna make some change to it
    :return: nothing return
    """
    title_font = pygame.font.SysFont('calibri', 80)
    game_image = title_font.render('G a m e', True, (0, 51, 51))
    over_image = title_font.render('O v e r', True, (0, 51, 51))
    game_rect = game_image.get_rect()
    over_rect = over_image.get_rect()
    screen_rect = screen.get_rect()
    game_rect.midtop = (ai_settings.screen_width / 2, screen_rect.top + 70)
    over_rect.midtop = (ai_settings.screen_width / 2, game_rect.bottom + 50)
    screen.blit(game_image, game_rect)
    screen.blit(over_image, over_rect)
    pygame.display.flip()
    # write the score into txt
    if ai_settings.score != 0 and ai_settings.length != 0:
        with open('scores.txt', 'a', encoding='utf-8-sig') as f:
            f.write('%d %d' % (ai_settings.score, ai_settings.length))
            if ai_settings.score / ai_settings.length == 5:
                f.write(' 1\n')
            elif ai_settings.score / ai_settings.length == 50:
                f.write(' 3\n')
            else:
                f.write(' 2\n')
    # the ending interface hold for a period of time, then return to the start interface
    pygame.time.wait(2000)
    ai_settings.game_stats = 0


# draw grid on the screen
def draw_grid(ai_settings, screen):
    """
    this function aims to draw a grid on the screen
    :param ai_settings: the setting of ai
    :param screen: the screen we draw the grid on
    :return: nothing return just change the screen
    """
    # draw horizon lines
    for x in range(0, ai_settings.screen_width, ai_settings.cell_size):
        pygame.draw.line(screen, (255, 204, 204), (x, 0), (x, ai_settings.screen_height))
    # draw vertical lines
    for y in range(0, ai_settings.screen_height, ai_settings.cell_size):
        pygame.draw.line(screen, (255, 204, 204), (0, y), (ai_settings.screen_width, y))


def update_screen(ai_settings, screen):
    """
    this function aims to change the screen according to the ai-setting
    :param ai_settings: the setting of ai
    :param screen: the screen we will make change on
    :return: nothing
    """
    screen.fill(ai_settings.bg_color)
    draw_grid(ai_settings, screen)


# draw the snake
def draw_snake(ai_settings, screen, snake):
    """
    the function aims to draw the snake
    :param ai_settings: the setting of ai
    :param screen: the screen we will make change on
    :param snake: the snake we will draw on the screen
    :return: nothing
    """
    # use blue for head
    x = snake.coords[0]['x'] * ai_settings.cell_size
    y = snake.coords[0]['y'] * ai_settings.cell_size
    snake_head_rect = pygame.Rect(x, y, ai_settings.cell_size, ai_settings.cell_size)
    pygame.draw.rect(screen, (0, 0, 255), snake_head_rect)
    # snake body use light green, the out part use dark green
    for coord in snake.coords[1: -1]:
        x = coord['x'] * ai_settings.cell_size
        y = coord['y'] * ai_settings.cell_size
        snake_part_rect = pygame.Rect(x, y, ai_settings.cell_size, ai_settings.cell_size)
        pygame.draw.rect(screen, (0, 155, 0), snake_part_rect)
        snake_part_inner_rect = pygame.Rect(x + 4, y + 4, ai_settings.cell_size - 8, ai_settings.cell_size - 8)
        pygame.draw.rect(screen, (0, 255, 0), snake_part_inner_rect)
    # use light green for snake tail
    coord = snake.coords[-1]
    x = coord['x'] * ai_settings.cell_size
    y = coord['y'] * ai_settings.cell_size
    snake_tail_rect = pygame.Rect(x, y, ai_settings.cell_size, ai_settings.cell_size)
    pygame.draw.rect(screen, (0, 255, 0), snake_tail_rect)


# draw game screen
def update_screen(ai_settings, screen, snake):
    """
    the function aims to draw the game screen
    :param ai_settings: the setting of ai
    :param screen: the screen we will make change on
    :param snake: the snake we will draw on the screen
    :return: nothing
    """
    screen.fill(ai_settings.bg_color)

    draw_grid(ai_settings, screen)
    draw_snake(ai_settings, screen, snake)

    # draw snake
    del snake.coords[-1]  # add snake head
    snake.update()  # remove snake tail
    pygame.display.flip()

    # pause
    ai_settings.my_clock.tick(ai_settings.clock_frq)


# test the key during the game
def check_play_events(snake):
    """
    this function aims to check the keyboard action during the game
    :param snake: the snake input
    :return: nothing
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            elif event.key == pygame.K_LEFT and not snake.direction == 'right':
                snake.direction = 'left'
            elif event.key == pygame.K_RIGHT and not snake.direction == 'left':
                snake.direction = 'right'
            elif event.key == pygame.K_UP and not snake.direction == 'down':
                snake.direction = 'up'
            elif event.key == pygame.K_DOWN and not snake.direction == 'up':
                snake.direction = 'down'





def is_game_over(ai_settings, snake):
    """
    check whether the game is over
    return: True or False
    """
    # touch the left or right wall
    if (snake.coords[snake.head_index]['x'] == -1 or snake.coords[snake.head_index]['x'] == ai_settings.cell_w):
        return False
    # touch the head or bottom wall
    if (snake.coords[snake.head_index]['y'] == -1 or snake.coords[snake.head_index]['y'] == ai_settings.cell_h):
        return False
    # touch itself
    if (snake.coords[snake.head_index] in snake.coords[1:]):
        return False
    return True


# draw food
def draw_food(ai_settings, screen, food):
    """
    draw food on the screen
    :param ai_settings: the setting of ai
    :param screen: the screen we will make change on
    :param food: the food we will draw on the screen
    :return: nothing
    """
    x = food.coord['x'] * ai_settings.cell_size
    y = food.coord['y'] * ai_settings.cell_size
    food_rect = pygame.Rect(x, y, ai_settings.cell_size, ai_settings.cell_size)
    # color the position of food as red
    pygame.draw.rect(screen, (255, 0, 0), food_rect)


# can eat food or not
def is_eat_food(ai_settings, snake, food):
    """
    check whether the food is eaten
    return: True or False
    """
    # if the position of snake head is food, thus eating food, update the position of food
    if snake.coords[snake.head_index] == food.coord:
        food.update(ai_settings, snake)
        ai_settings.length += 1
        if ai_settings.game_stats == 1:
            ai_settings.score += 5
        elif ai_settings.game_stats == 2:
            ai_settings.score += 10
        elif ai_settings.game_stats == 3:
            ai_settings.score += 50
        else:
            ai_settings.score += 1
        return True
    return False


# draw the game interface
def update_screen(ai_settings, screen, snake, food):
    """
    draw the game interface
    """
    scores_font = pygame.font.Font("../font/STKAITI.TTF", 30)
    scores_image = scores_font.render(u"Score: %d " % ai_settings.score, True, (0, 51, 51))
    length_font = pygame.font.Font("../font/STKAITI.TTF", 30)
    length_image = length_font.render(u"Snake Length: %d " % ai_settings.length, True, (0, 51, 51))
    screen.fill(ai_settings.bg_color)
    draw_grid(ai_settings, screen)
    screen.blit(scores_image, (10, 10))
    screen.blit(length_image, (600, 10))
    # move the snake
    flag = is_eat_food(ai_settings, snake, food)
    if not flag:
        del snake.coords[-1]
    snake.update()
    if not is_game_over(ai_settings, snake):
        ai_settings.game_stats = -1
    else:
        draw_snake(ai_settings, screen, snake)
        draw_food(ai_settings, screen, food)
        pygame.display.flip()
        # pause
        ai_settings.my_clock.tick(ai_settings.clock_frq)


# check the keyboard operation in rank board
def check_list_events(ai_settings):
    """
    check the keyboard operation in the rank board
    :param ai_settings: the setting of ai
    :return: nothing
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            elif event.key == pygame.K_1:
                ai_settings.game_stats = 0


# read data from txt document
def read_list_txt(file_name, list_mode1, list_mode2, list_mode3):
    """
    file_name: txt name we later read
    list_mode1: ranks for difficult level 1
    list_mode2: ranks for difficult level 2
    list_mode3: ranks for difficult level 3
    :return: list_mode1, list_mode2, list_mode3

    """
    # 读取原始数据
    with open(file_name, 'r', encoding='utf-8-sig') as f:
        content = f.readlines()[1:]
    list_data = []
    game_mode1 = []
    game_mode2 = []
    game_mode3 = []
    for line in content:
        list_data.append(line.strip('\n').split(' '))
    for i in range(len(list_data)):
        if list_data[i][-1] == '1':
            for j in range(3):
                list_data[i][j] = int(list_data[i][j])
            game_mode1.append(list_data[i])
        elif list_data[i][-1] == '2':
            for j in range(3):
                list_data[i][j] = int(list_data[i][j])
            game_mode2.append(list_data[i])
        else:
            for j in range(3):
                list_data[i][j] = int(list_data[i][j])
            game_mode3.append(list_data[i])
    # remove same data
    game_mode1 = list(set(tuple(i) for i in game_mode1))
    game_mode2 = list(set(tuple(i) for i in game_mode2))
    game_mode3 = list(set(tuple(i) for i in game_mode3))
    # sort
    game_mode1.sort()
    game_mode2.sort()
    game_mode3.sort()
    # put the ranking data into the list
    for i in range(5):
        list_mode1[i] = ("NO.%d     %d" % (i + 1, game_mode1[-i - 1][0]))
        list_mode2[i] = ("NO.%d     %d" % (i + 1, game_mode2[-i - 1][0]))
        list_mode3[i] = ("NO.%d     %d" % (i + 1, game_mode3[-i - 1][0]))

    return list_mode1, list_mode2, list_mode3


# draw the ranking
def show_list(ai_settings, screen):
    """
    draw the ranking on the screen
    :param ai_settings: the setting of ai
    :param screen: the screen input
    :return: nothing
    """
    background = pygame.image.load(r"../image/rank.jpg")
    font1 = pygame.font.Font("../font/STKAITI.TTF", 35)
    image1 = font1.render('press 1 return to main interface', True, (0, 0, 0))

    # read data from ranking
    l1 = [0] * 5
    l2 = [0] * 5
    l3 = [0] * 5
    read_list_txt('scores.txt', l1, l2, l3)

    while True:
        screen.fill(ai_settings.bg_color)  # draw the screen
        screen.blit(background, (0, 0))  # bg pic
        # screen.blit(排, (50, 30))
        #
        # screen.blit(榜, (590, 30))
        presskey_font = pygame.font.Font("../font/STKAITI.TTF", 35)  # set the description font
        presskey_image = presskey_font.render('Ranking Info', True, (0, 0, 0))
        screen.blit(presskey_image, (310, 30))
        screen.blit(image1, (400, 500))
        screen.blit(pygame.font.Font('../font/STKAITI.TTF', 35).render(' Difficult Level 1 ', True, (0, 0, 0)), (35, 200))
        screen.blit(pygame.font.Font('../font/STKAITI.TTF', 35).render(' Difficult Level 2 ', True, (0, 0, 0)), (260, 200))
        screen.blit(pygame.font.Font('../font/STKAITI.TTF', 35).render(' Difficult level 3 ', True, (0, 0, 0)), (500, 200))
        for i in range(5):
            screen.blit(pygame.font.Font('../font/STKAITI.TTF', 25).render(l1[i], True, (0, 0, 0)), (80, 263 + i * 37))
        for i in range(5):
            screen.blit(pygame.font.Font('../font/STKAITI.TTF', 25).render(l2[i], True, (0, 0, 0)), (340, 263 + i * 37))
        for i in range(5):
            screen.blit(pygame.font.Font('../font/STKAITI.TTF', 25).render(l3[i], True, (0, 0, 0)), (600, 263 + i * 37))

        check_list_events(ai_settings)  # test keyboard
        if ai_settings.game_stats == 0:
            break
        pygame.display.flip()


# /* ----------AI-------------*/
# /*-----------BFS--------------*/

# show the score
def Show_Score(ai_settings, score):
    """
    show the score on the screen
    :param ai_settings: the setting of ai
    :param score: the score input
    :return: nothing
    """
    score_Content = Main_Font.render('Snake Length：%s' % (score), True, (0, 0, 0))
    score_Rect = score_Content.get_rect()
    score_Rect.topleft = (ai_settings.screen_width - 120, 10)
    Main_Display.blit(score_Content, score_Rect)


# get the position of food
def Get_Apple_Location(ai_settings, snake_Coords):
    """
    get the position of the food
    :param ai_settings: the setting of ai
    :param snake_Coords: the position of the snake
    :return: nothing
    """
    flag = True
    while flag:
        apple_location = {'x': random.randint(0, ai_settings.cell_w - 1),
                          'y': random.randint(0, ai_settings.cell_h - 1)}
        if apple_location not in snake_Coords:
            flag = False
    return apple_location


# show the food
def Show_Apple(ai_settings, coord):
    """
    show the apple position on the screen
    :param ai_settings: the setting of ai
    :param coord: the coordinate of apple
    :return: nothing
    """
    x = coord['x'] * ai_settings.cell_size
    y = coord['y'] * ai_settings.cell_size
    apple_Rect = pygame.Rect(x, y, ai_settings.cell_size, ai_settings.cell_size)
    pygame.draw.rect(Main_Display, (255, 0, 0), apple_Rect)


# show the snake
def Show_Snake(ai_settings, coords):
    """
    show the snake on the screen
    :param ai_settings: the setting of ai
    :param coords: the position of snake
    :return: nothing
    """
    x = coords[0]['x'] * ai_settings.cell_size
    y = coords[0]['y'] * ai_settings.cell_size
    Snake_head_Rect = pygame.Rect(x, y, ai_settings.cell_size, ai_settings.cell_size)
    pygame.draw.rect(Main_Display, (0, 80, 255), Snake_head_Rect)
    Snake_head_Inner_Rect = pygame.Rect(x + 4, y + 4, ai_settings.cell_size - 8, ai_settings.cell_size - 8)
    pygame.draw.rect(Main_Display, (0, 80, 255), Snake_head_Inner_Rect)
    for coord in coords[1:]:
        x = coord['x'] * ai_settings.cell_size
        y = coord['y'] * ai_settings.cell_size
        Snake_part_Rect = pygame.Rect(x, y, ai_settings.cell_size, ai_settings.cell_size)
        pygame.draw.rect(Main_Display, (0, 155, 0), Snake_part_Rect)
        Snake_part_Inner_Rect = pygame.Rect(x + 4, y + 4, ai_settings.cell_size - 8, ai_settings.cell_size - 8)
        pygame.draw.rect(Main_Display, (0, 255, 0), Snake_part_Inner_Rect)


# draw the grid
def draw_Grid(ai_settings):
    """
    draw the grid on the screen
    :param ai_settings: the setting of ai
    :return: nothing
    """
    # the verticle direction
    for x in range(0, ai_settings.screen_width, ai_settings.cell_size):
        pygame.draw.line(Main_Display, (255, 204, 204), (x, 0), (x, ai_settings.screen_height))
    # the horizontal direction
    for y in range(0, ai_settings.screen_height, ai_settings.cell_size):
        pygame.draw.line(Main_Display, (255, 204, 204), (0, y), (ai_settings.screen_width, y))


# tell whether this position is vacant
def Is_Cell_Free(ai_settings, idx, psnake):
    """
    tell whether this position is vacant
    :param ai_settings:
    :param idx: the position checked
    :param psnake: the position of the snake
    :return: true or false
    """
    location_x = idx % ai_settings.cell_w
    location_y = idx // ai_settings.cell_w
    idx = {'x': location_x, 'y': location_y}
    return (idx not in psnake)


# reset board
def board_reset(ai_settings, psnake, pboard, pfood):
    """
    reset the board
    :param ai_settings: the setting of ai
    :param psnake: the position of snake
    :param pboard: the position of board
    :param pfood: the position of food
    :return: the board
    """
    temp_board = pboard[:]
    pfood_idx = pfood['x'] + pfood['y'] * ai_settings.cell_w
    for i in range(ai_settings.num):
        if i == pfood_idx:
            temp_board[i] = 0
        elif Is_Cell_Free(ai_settings, i, psnake):
            temp_board[i] = ai_settings.free_place
        else:
            temp_board[i] = ai_settings.snake_place
    return temp_board


# check whether the position idx is proper to make the move direction
def is_move_possible(ai_settings, idx, move_direction):
    """
    check whether the position is proper to make move direction
    :param ai_settings: the setting of ai
    :param idx: the position checked
    :param move_direction: the moving direction input
    :return: true or false
    """
    flag = False
    if move_direction == 'left':
        if idx % ai_settings.cell_w > 0:
            flag = True
        else:
            flag = False
    elif move_direction == 'right':
        if idx % ai_settings.cell_w < ai_settings.cell_w - 1:
            flag = True
        else:
            flag = False
    elif move_direction == 'up':
        if idx > ai_settings.cell_w - 1:
            flag = True
        else:
            flag = False
    elif move_direction == 'down':
        if idx < ai_settings.num - ai_settings.cell_w:
            flag = True
        else:
            flag = False
    return flag


# bread first search the whole board
# calculate every place(except the snake body) to get the food
def board_refresh(ai_settings, psnake, pfood, pboard):
    """
    refresh the board
    :param ai_settings: the setting of ai
    :param psnake: the position of snake
    :param pfood: the position of food
    :param pboard: the position of board
    :return: tuple
    """
    temp_board = pboard[:]
    pfood_idx = pfood['x'] + pfood['y'] * ai_settings.cell_w
    queue = []
    queue.append(pfood_idx)
    inqueue = [0] * ai_settings.num
    found = False
    while len(queue) != 0:
        idx = queue.pop(0)
        if inqueue[idx] == 1:
            continue
        inqueue[idx] = 1
        for move_direction in ['left', 'right', 'up', 'down']:
            if is_move_possible(ai_settings, idx, move_direction):
                if (idx + ai_settings.move_directions[move_direction]) == (
                        psnake[ai_settings.Head_index]['x'] + psnake[ai_settings.Head_index]['y'] * ai_settings.cell_w):
                    found = True
                # the place is not the snake body
                if temp_board[idx + ai_settings.move_directions[move_direction]] < ai_settings.snake_place:
                    if temp_board[idx + ai_settings.move_directions[move_direction]] > temp_board[idx] + 1:
                        temp_board[idx + ai_settings.move_directions[move_direction]] = temp_board[idx] + 1
                    if inqueue[idx + ai_settings.move_directions[move_direction]] == 0:
                        queue.append(idx + ai_settings.move_directions[move_direction])
    return (found, temp_board)


# according to the index of the board
# select the nearest route from the four points around the snake's head
def choose_shortest_safe_move(ai_settings, psnake, pboard):
    """
    according to the index of the board. elect the nearest route from the four points around the snake's head
    :param ai_settings: the setting of ai
    :param psnake: the position of snake
    :param pboard: the position of board
    :return: the best move
    """
    best_move = ai_settings.ERR
    min_distance = ai_settings.snake_place
    for move_direction in ['left', 'right', 'up', 'down']:
        idx = psnake[ai_settings.Head_index]['x'] + psnake[ai_settings.Head_index]['y'] * ai_settings.cell_w
        if is_move_possible(ai_settings, idx, move_direction) and (
                pboard[idx + ai_settings.move_directions[move_direction]] < min_distance):
            min_distance = pboard[idx + ai_settings.move_directions[move_direction]]
            best_move = move_direction
    return best_move


# find the position of snake's head after one move
def find_snake_head(ai_settings, snake_Coords, direction):
    """
    find the position of snake's head after one move
    :param ai_settings: the setting of ai
    :param snake_Coords: the snake position
    :param direction: the moving direction
    :return: the newhead position
    """
    if direction == 'up':
        newHead = {'x': snake_Coords[ai_settings.Head_index]['x'],
                   'y': snake_Coords[ai_settings.Head_index]['y'] - 1}
    elif direction == 'down':
        newHead = {'x': snake_Coords[ai_settings.Head_index]['x'],
                   'y': snake_Coords[ai_settings.Head_index]['y'] + 1}
    elif direction == 'left':
        newHead = {'x': snake_Coords[ai_settings.Head_index]['x'] - 1,
                   'y': snake_Coords[ai_settings.Head_index]['y']}
    elif direction == 'right':
        newHead = {'x': snake_Coords[ai_settings.Head_index]['x'] + 1,
                   'y': snake_Coords[ai_settings.Head_index]['y']}
    return newHead


# make one move
def virtual_move(ai_settings, psnake, pboard, pfood):
    """
    make one move according to the position
    :param ai_settings: te=he setting of ai
    :param psnake: the position of snake
    :param pboard: the position of board
    :param pfood: the position of food
    :return: the position of snake and board
    """
    temp_snake = psnake[:]
    temp_board = pboard[:]
    reset_tboard = board_reset(ai_settings, temp_snake, temp_board, pfood)
    temp_board = reset_tboard
    food_eated = False
    while not food_eated:
        refresh_tboard = board_refresh(ai_settings, temp_snake, pfood, temp_board)[1]
        temp_board = refresh_tboard
        move_direction = choose_shortest_safe_move(ai_settings, temp_snake, temp_board)
        snake_Coords = temp_snake[:]
        temp_snake.insert(0, find_snake_head(ai_settings, snake_Coords, move_direction))
        # if the new snake head is just the position of the food
        if temp_snake[ai_settings.Head_index] == pfood:
            reset_tboard = board_reset(ai_settings, temp_snake, temp_board, pfood)
            temp_board = reset_tboard
            pfood_idx = pfood['x'] + pfood['y'] * ai_settings.cell_w
            temp_board[pfood_idx] = ai_settings.snake_place
            food_eated = True
        else:
            newHead_idx = temp_snake[0]['x'] + temp_snake[0]['y'] * ai_settings.cell_w
            temp_board[newHead_idx] = ai_settings.snake_place
            end_idx = temp_snake[-1]['x'] + temp_snake[-1]['y'] * ai_settings.cell_w
            temp_board[end_idx] = ai_settings.free_place
            del temp_snake[-1]
    return temp_snake, temp_board


# check there is one route for the head and the tail
# not to make no place to move
def is_tail_inside(ai_settings, psnake, pboard, pfood):
    """
    check there is one route for the head and the tail and not to make no place to move
    :param ai_settings: the setting of ai
    :param psnake: the position of snake
    :param pboard: the position of board
    :param pfood: the position of food
    :return: the boolean results
    """
    temp_board = pboard[:]
    temp_snake = psnake[:]
    # see the snake tail as food
    end_idx = temp_snake[-1]['x'] + temp_snake[-1]['y'] * ai_settings.cell_w
    temp_board[end_idx] = 0
    v_food = temp_snake[-1]
    # food as the snake body
    pfood_idx = pfood['x'] + pfood['y'] * ai_settings.cell_w
    temp_board[pfood_idx] = ai_settings.snake_place
    # get the distance of every position to the snake tail
    result, refresh_tboard = board_refresh(ai_settings, temp_snake, v_food, temp_board)
    temp_board = refresh_tboard
    for move_direction in ['left', 'right', 'up', 'down']:
        idx = temp_snake[ai_settings.Head_index]['x'] + temp_snake[ai_settings.Head_index]['y'] * ai_settings.cell_w
        end_idx = temp_snake[-1]['x'] + temp_snake[-1]['y'] * ai_settings.cell_w
        if is_move_possible(ai_settings, idx, move_direction) and (
                idx + ai_settings.move_directions[move_direction] == end_idx) and (len(temp_snake) > 3):
            result = False
    return result



# according to the index of the board find the farthest point around the snake's head
def choose_longest_safe_move(ai_settings, psnake, pboard):
    """
    find the a=farthest point aaround the snake's head according to the index of the baord
    :param ai_settings: the setting of ai
    :param psnake: the position of snake
    :param pboard: the position of board
    :return: return the best move direction
    """
    best_move = ai_settings.ERR
    max_distance = -1
    for move_direction in ['left', 'right', 'up', 'down']:
        idx = psnake[ai_settings.Head_index]['x'] + psnake[ai_settings.Head_index]['y'] * ai_settings.cell_w
        if is_move_possible(ai_settings, idx, move_direction) and (
                pboard[idx + ai_settings.move_directions[move_direction]] > max_distance) and (
                pboard[idx + ai_settings.move_directions[move_direction]] < ai_settings.free_place):
            max_distance = pboard[idx + ai_settings.move_directions[move_direction]]
            best_move = move_direction
    return best_move


# make the snake's head move towards the snake's tail
def follow_tail(ai_settings, psnake, pboard, pfood):
    """
    make the snake's head move towards the snake's talil
    :param ai_settings: the setting of ai
    :param psnake: the position of snake
    :param pboard: the position of board
    :param pfood: the position of board
    :return: call the function choose_longest_safe_move
    """
    temp_snake = psnake[:]
    temp_board = board_reset(ai_settings, temp_snake, pboard, pfood)
    # see the snake tail as the food
    end_idx = temp_snake[-1]['x'] + temp_snake[-1]['y'] * ai_settings.cell_w
    temp_board[end_idx] = 0
    v_food = temp_snake[-1]
    # see the food as the snake body
    pfood_idx = pfood['x'] + pfood['y'] * ai_settings.cell_w
    temp_board[pfood_idx] = ai_settings.snake_place
    # get each position to the snake's tail
    result, refresh_tboard = board_refresh(ai_settings, temp_snake, v_food, temp_board)
    temp_board = refresh_tboard
    # reset
    temp_board[end_idx] = ai_settings.snake_place
    # temp_board[pfood_idx] = FOOD
    return choose_longest_safe_move(ai_settings, temp_snake, temp_board)



# if there is a way between snake and the food, we should find a safe route
def find_safe_way(ai_settings, psnake, pboard, pfood):
    """

    :param ai_settings: the setting of ai
    :param psnake: snake position
    :param pboard: board position
    :param pfood: food position
    :return: safe move position
    """
    safe_move = ai_settings.ERR
    real_snake = psnake[:]
    real_board = pboard[:]
    v_psnake, v_pboard = virtual_move(ai_settings, psnake, pboard, pfood)
    # find the shortest route
    if is_tail_inside(ai_settings, v_psnake, v_pboard, pfood):
        safe_move = choose_shortest_safe_move(ai_settings, real_snake, real_board)
    else:
        safe_move = follow_tail(ai_settings, real_snake, real_board, pfood)
    return safe_move


# make a move on a random direction
def any_possible_move(ai_settings, psnake, pboard, pfood):
    """
    to make a move on a random direction
    :param ai_settings:
    :param psnake:
    :param pboard:
    :param pfood:
    :return: the best move
    """
    best_move = ai_settings.ERR
    reset_board = board_reset(ai_settings, psnake, pboard, pfood)
    pboard = reset_board
    result, refresh_board = board_refresh(ai_settings, psnake, pfood, pboard)
    pboard = refresh_board
    min_distance = ai_settings.snake_place
    for move_direction in ['left', 'right', 'up', 'down']:
        idx = psnake[ai_settings.Head_index]['x'] + psnake[ai_settings.Head_index]['y'] * ai_settings.cell_w
        if is_move_possible(ai_settings, idx, move_direction) and (
                pboard[idx + ai_settings.move_directions[move_direction]] < min_distance):
            min_distance = pboard[idx + ai_settings.move_directions[move_direction]]
            best_move = move_direction
    return best_move


def run_game_ai(ai_settings):
    """
    run the game according to the ai-setting input
    :param ai_settings: the input setting of ai
    :return: nothing
    """
    pygame.display.set_caption('GreedySnake-AI')
    global Main_Display, Main_Font, Snake_Clock
    Snake_Clock = pygame.time.Clock()
    Main_Display = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    Main_Font = pygame.font.Font('../font/STKAITI.TTF', 18)

    # move grid
    board = [0] * ai_settings.num
    # birth place
    start_x = random.randint(5, ai_settings.cell_w - 6)
    start_y = random.randint(5, ai_settings.cell_h - 6)
    snake_Coords = [{'x': start_x, 'y': start_y},
                    {'x': start_x - 1, 'y': start_y},
                    {'x': start_x - 2, 'y': start_y}]
    apple_location = Get_Apple_Location(ai_settings, snake_Coords)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        Main_Display.fill(ai_settings.bg_color)
        draw_Grid(ai_settings)
        Show_Snake(ai_settings, snake_Coords)
        Show_Apple(ai_settings, apple_location)
        Show_Score(ai_settings, len(snake_Coords) - 3)
        # reset board
        reset_board = board_reset(ai_settings, snake_Coords, board, apple_location)
        board = reset_board
        result, refresh_board = board_refresh(ai_settings, snake_Coords, apple_location, board)
        board = refresh_board
        # if snake can eat food
        if result:
            best_move = find_safe_way(ai_settings, snake_Coords, board, apple_location)
        else:
            best_move = follow_tail(ai_settings, snake_Coords, board, apple_location)
        if best_move == ai_settings.ERR:
            best_move = any_possible_move(ai_settings, snake_Coords, board, apple_location)
        if best_move != ai_settings.ERR:
            newHead = find_snake_head(ai_settings, snake_Coords, best_move)
            snake_Coords.insert(0, newHead)
            head_idx = snake_Coords[ai_settings.Head_index]['x'] + snake_Coords[ai_settings.Head_index][
                'y'] * ai_settings.cell_w
            end_idx = snake_Coords[-1]['x'] + snake_Coords[-1]['y'] * ai_settings.cell_w
            if (snake_Coords[ai_settings.Head_index]['x'] == apple_location['x']) and (
                    snake_Coords[ai_settings.Head_index]['y'] == apple_location['y']):
                board[head_idx] = ai_settings.snake_place
                if len(snake_Coords) < ai_settings.num:
                    apple_location = Get_Apple_Location(ai_settings, snake_Coords)
            else:
                board[head_idx] = ai_settings.snake_place
                board[end_idx] = ai_settings.free_place
                del snake_Coords[-1]
        else:
            return
        pygame.display.update()
        Snake_Clock.tick(ai_settings.display_clock)
