import pygame, random

pygame.init()
D = pygame.display.set_mode((1000, 650))
pygame.display.set_caption('Memory game')
cardwidth = 160
cardheight = 128
wboardmod = 5
hboardmod = 4
gap = 20
startx = 20
starty = 20
h = 0
l = 0
i = 0
coordinates = []
while i < wboardmod * hboardmod:
    # adds tuples which are top left coordinates of each card to coordinates array
    coordinates.append((startx + h * cardwidth + h * gap, starty + l * gap + l * cardheight))
    if h < (wboardmod - 1):
        h += 1
    else:
        h = 0
        l += 1
    i += 1
Rest = pygame.image.load('restart.jpeg')
Win = pygame.image.load('win.jpeg')
Int = pygame.image.load('integral.jpeg')
Blue = pygame.image.load('BlueCircle.jpeg')
Att = pygame.image.load('attack.jpeg')
Sig = pygame.image.load('sigma.jpeg')
Py = pygame.image.load('python.jpeg')
Card = pygame.image.load('card.jpeg')
images = []
i = 0
while i < (hboardmod * wboardmod) / 5:  # creates an array images and adds the back faces of the cards to it
    images.append(Int)
    images.append(Blue)
    images.append(Att)
    images.append(Sig)
    images.append(Py)
    i += 1

Screencolor = (0, 0, 0)


def pressedrect(event, tlx, tly, w, h):
    # checks whether the mouse has clicked a rectangular region

    if event.type == pygame.MOUSEBUTTONDOWN:
        x, y = pygame.mouse.get_pos()
        if x >= tlx and x <= tlx + w and y >= tly and y <= tly + h:
            return True
        else:
            return False
    else:
        return False


G = pygame.image.load('card.jpeg')
pygame.display.update()
restat = 0
while restat == 0:  # restat is switched to 1 in the main game loop, if the user clicks restart, it switches restat back to 0
    D.fill(Screencolor)  # so that the game loops again
    for i in range(0, len(coordinates)):
        x1, y1 = coordinates[i]  # blits cards on to the screen
        D.blit(G, (x1, y1))
    assignment = {}
    Sh = random.sample(images, len(images))  # shuffles the srray images

    for i in range(0, len(Sh)):
        assignment[coordinates[i]] = Sh[i]  # assigns the coordinate of eaach card to a random image in images

    status = {}
    for i in range(0, len(coordinates)):
        status[coordinates[i]] = "unpressed"  # assigns each card a status "unpressed"

    openc = 0
    openci = []
    game = True
    restat = 1
    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False

        for i in range(0, len(coordinates)):
            x, y = coordinates[i]
            if pressedrect(event, x, y, cardwidth, cardheight):
                if status[coordinates[i]] == "unpressed":
                    D.blit(assignment[coordinates[i]], (x, y))

                    status[coordinates[i]] = "pressed"
                    pygame.display.update()
                    openc += 1
                    openci.append(coordinates[i])

                    if openc == 2:
                        x3, y3 = openci[0]
                        x4, y4 = openci[1]
                        if assignment[openci[0]] == assignment[openci[1]]:
                            pygame.time.wait(750)
                            pygame.draw.rect(D, Screencolor, (x3, y3, cardwidth, cardheight))
                            pygame.draw.rect(D, (0, 0, 0), (x4, y4, cardwidth, cardheight))


                        else:

                            status[openci[0]] = "unpressed"
                            status[openci[1]] = "unpressed"
                            pygame.time.wait(750)
                            D.blit(G, openci[0])
                            D.blit(G, openci[1])
                            pygame.display.update()
                        openc = 0
                        openci = []
        k = 0

        for i in coordinates:
            if status[i] == "pressed":
                k += 1
        if k == hboardmod * wboardmod:
            pygame.time.wait(600)
            D.blit(Win, (0, 0))
            D.blit(Rest, (700, 300))
            for event in pygame.event.get():
                if pressedrect(event, 700, 300, 238, 250):
                    restat = 0
                    game = False

        pygame.display.update()