import pygame
import sys

pygame.init()
pygame.mixer.init()

WIDTH, HEIGHT = 500, 300
sc = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Music Player")

font = pygame.font.Font(None, 18)

songs = ["music/Ma_Meilleure_Ennemie.mp3", "music/Love_Like_You.mp3", "music/Come-play.mp3"]
queue = 0
playing = False

def text(text, x, y, color=(255, 255, 255)):
    render = font.render(text, True, color)
    sc.blit(render, (x, y))

def update_caption():
    state = "Playing" if playing else "Paused"
    """
    if playing:
        state = 'Playing'
    else:
        state = 'Paused'
    """
    pygame.display.set_caption(f"Track: {songs[queue]} | {state} | SPACE = Play/Pause | → Next | ← Previous")

pygame.mixer.music.load(songs[queue])

run = True
while run:
    sc.fill((50, 50, 50))

    text(f"Track: {songs[queue]}", 50, 70)
    text("SPACE = Play/Pause | стрелка право Next | стрелка лево Previous", 20, 30)
    
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if playing:
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
                playing = not playing
                
            elif event.key == pygame.K_RIGHT:
                queue = (queue + 1) % len(songs)
                pygame.mixer.music.load(songs[queue])
                if playing:
                    pygame.mixer.music.play()
                    
            elif event.key == pygame.K_LEFT:
                queue = (queue - 1) % len(songs)
                pygame.mixer.music.load(songs[queue])
                if playing:
                    pygame.mixer.music.play()
                    
            update_caption()

pygame.quit()
sys.exit()