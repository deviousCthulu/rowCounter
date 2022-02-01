import pygame

time = 0

#Counter Increase
def timeIncrease():
    global time
    time = time + 1

#Counter Decrease
def timeDecrease():
    global time
    time = time - 1

def main():
    global time
    # Initialise Screen
    pygame.init()
    screen = pygame.display.set_mode((600,850))
    pygame.display.set_caption('Row Counter')
    pygame.display.set_allow_screensaver(False)

    #Background
    background = pygame.image.load('rowCounterBackground.png')
    background = pygame.transform.scale(background, (600,850))

    #Current Row Count Display
    font = pygame.font.SysFont('comicsans', 100)
    text = font.render(str(time),True, (255,255,255))

    #Blit to screen
    screen.blit(background,(0,0))
    pygame.display.flip()

    while True:
    #Button Presses; Increase 1, Decrease 1, Reset
        for event in pygame.event.get():
            if event.type == pygame.K_SPACE:
                timeIncrease()
            else:
                if event.type == pygame.K_BACKSPACE:
                    timeDecrease()
                else:
                    if event.type == pygame.K_RETURN:
                        time = 0

    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.blit(background, (0,0))
        screen.blit(text, (275,225))
        pygame.display.flip()

main()
