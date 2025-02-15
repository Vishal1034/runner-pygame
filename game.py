import pygame
import random
from sys import exit

def display_score():
    current_time = int((pygame.time.get_ticks() - start_time ) / 1000)
    score_surface = test_font.render(f'Score : {current_time}', False, (64,64,64))
    score_rect = score_surface.get_rect(center = (400,50))
    screen.blit(score_surface, score_rect)

def draw_fps():
    fps = int(clock.get_fps())
    

    fps_text = test_font.render(f"FPS: {fps}", True, (64,64,64))
    # Draw the text on the screen
    screen.blit(fps_text, (10, 10))
        

    pygame.display.update()
    clock.tick(60)

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("Runner")
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)
game_active = True

SKYSPEED = 2
bgWidth = ground_surface.get_width()

snail_surface1 = pyg').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80,300))

currentState = player_surf
snailState = snail_surface1
currentWalk = False
snailWalk = False

player_stand = pygame.image.load('graphics/Player/player_stand.png').convert_alpha()


start_time = 0

def randomiseSpeed(x):
    x = random.randint(6,20)
    return x


counter = 0

player_gravity = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:  
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom == 300:
                        player_gravity = -20
                        currentState = player_surf_jump

            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos) and player_rect.bottom == 300:
                    player_gravity = -20
        
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                snail_rect.right = 800
                start_time = pygame.time.get_ticks()
                
            
    if game_active:
        bg_x -= BGSPEED 
        sky_x -= SKYSPEED

        if (bg_x <= -bgWidth):
            bg_x = 0     
        if (sky_x <= -skyWidth):
            sky_x = 0
        screen.blit(sky_surface,(sky_x,0))
        screen.blit(sky_surface,(sky_x + skyWidth,0))
        screen.blit(ground_surface,(bg_x,300))
        screen.blit(ground_surface,(bg_x + bgWidth,300))

        if snailWalk:
            snailState = snail_surface1
        else:
            snailState = snail_surface2
        
        display_score()
        screen.blit(snailState,snail_rect)
        if snail_rect.right < 0: 
            snail_rect.right = 800
            snailSpeed = randomiseSpeed(snailSpeed)
        snail_rect.right -= snailSpeed


        #player
        screen.blit(currentState,player_rect)
        player_gravity += 1
        player_rect.bottom += player_gravity
        if player_rect.bottom >= 300: 
            player_rect.bottom = 300
            if counter % 7 == 0:
                currentWalk = not currentWalk
                snailWalk = not snailWalk
            if (currentWalk):
                currentState = player_surf_walk1
            else:
                currentState = player_surf_walk2

        if(player_rect.colliderect(snail_rect)):
            game_active = False
        
        counter += 1

        draw_fps()

    else:
        screen.fill((94,129,162))
        screen.blit(player_stand ,player_stand_rect)
        pygame.display.update()

