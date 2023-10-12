import pygame
import random

pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Mga Balls in Marcelo")
clock= pygame.time.Clock()
running = True


class Ball:
    
    ball_Radius = 50
    # ball_Speed = 5 //let's random this speed

    # variable that will store the ball object in the array
    list_balls =[]

    def __init__(self):

        self.radius = self.ball_Radius

        # Iam gonna try to use Vector2 for the Balls position
        self.position = pygame.Vector2(
            random.randint(self.radius, 1280 - self.radius),
            random.randint(self.radius, 720 - self.radius)
        )
        
#random.uniform, Random number between, and included -1 and 10
    # Using Vector2 for the random speed of the balls
        self.speed = pygame.Vector2(
            random.uniform(-10,5),
            random.uniform(-10,5)
        )

    #The logic that this will append all the ball object in the list_balls..... 
        self.list_balls.append(self)

    def move(self):
        self.position += self.speed

        if self.position.x <= self.radius or self.position.x >= 1280 - self.radius:
            self.speed.x *= -1
        if self.position.y <= self.radius or self.position.y >= 720 -self.radius:
            self.speed.y *= -1

# subclasses
class color(Ball):
    def __init__(self):

         # Call the parent class's 
        super().__init__()    
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        # the (0,255) will be randomly create a color  using Hex...

    def display(self):
        pygame.draw.circle(screen, self.color, self.position, self.radius)



ball_count = 10
for x in range(ball_count):
    color()


# Game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # the game will stop
            running = False
    screen.fill("red")

# calling all the function...
    for x in Ball.list_balls:
        x.move()
        x.display()


    pygame.display.update()
# This function is like an optimized version of pygame.display.flip() for software displays.
#  It allows only a portion of the screen to be updated, instead of the entire area. 
# If no argument is passed it updates the entire Surface area like pygame.display.flip().

pygame.quit()