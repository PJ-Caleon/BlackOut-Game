import pygame, random
from pathlib import Path
from player import Player
from obstacle import Obstacle
from playerHealth import PlayerHealth
from healthUp import healthItem

pygame.init()
pygame.mixer.init()
pygame.display.set_caption("Black Out 1.0")

# Constants
WIDTH, HEIGHT = 900, 600
color = (255, 0, 0)

# Load audio files
health_sound_path = Path(__file__).parent / "audio" / "powerUP.wav"
healthSound = pygame.mixer.Sound(str(health_sound_path))
damage_sound_path = Path(__file__).parent / "audio" / "damaged.wav"
damageSound = pygame.mixer.Sound(str(damage_sound_path))

# Create a player instance
pygame.mouse.set_visible(False)
player = Player(color, radius=10)
player_health = PlayerHealth(initial_health=100)

# Health item instance
health_item = healthItem()
health_item.x = random.randint(50, WIDTH - 50)
health_item.y = random.randint(50, HEIGHT - 50)

# Create obstacle instance
obstacles = [Obstacle() for _ in range(5)]

# Score system
score = 0
start_time = pygame.time.get_ticks()

# Game State
game_over = False

# Collision Cooldown
collision_timer = 0
collision_cooldown = 1000

screen = pygame.display.set_mode((WIDTH, HEIGHT))

run = True
while run:
    if not game_over:
        # White background
        screen.fill((210, 210, 210)) 

        # Player health bar
        player_health.draw_health_bar(screen, 20, 20)
        
        # Update player position
        player.update_position()
        player.draw(screen)

        # Randomly spawn health item on screen
        health_item.draw(screen)

        # Check for collision with health item
        if player.x - player.radius < health_item.x + health_item.width and \
           player.x + player.radius > health_item.x and \
           player.y - player.radius < health_item.y + health_item.height and \
           player.y + player.radius > health_item.y:
            player_health.heal(10)  # Heal the player 
            healthSound.play()  
            
            # Reposition the health item
            health_item.x = random.randint(50, WIDTH - 50)
            health_item.y = random.randint(50, HEIGHT - 50)


        # Update and Display score
        current_time = (pygame.time.get_ticks() - start_time) // 1000
        score = current_time

        gameScoreText = pygame.font.Font(None, 24).render(f"{score}" , True, (0, 0, 0))
        screen.blit(gameScoreText, (1.95*WIDTH // 2 - gameScoreText.get_width() // 2, 0.09*HEIGHT // 1.75 - gameScoreText.get_height() // 2))

        # Spawn obstacles
        for obstacle in obstacles:
            obstacle.update_position(random.randint(0, WIDTH), random.randint(0, HEIGHT))
            obstacle.draw(screen)

            # Spawn more if score is greater than 20
            if score >= 20 & len(obstacles) < 10:
                obstacles.append(Obstacle())

            # Check for collision with player
            current_time = pygame.time.get_ticks()
            if current_time - collision_timer > collision_cooldown:
                if player.check_collision(obstacles):
                    
                    # Player takes damage
                    player_health.take_damage(20)
                    damageSound.play()
                    collision_timer = current_time

                    # Game over Screen
                    if player_health.health <= 0:
                        game_over = True

        # Despawn obstacles after 5 seconds
        if pygame.time.get_ticks() % 5000 == 0:
            if obstacles:
                obstacles.pop(0)
            obstacles.append(Obstacle())

    else:
        # Game over screen
        screen.fill((0, 0, 0))
        font = pygame.font.Font(None, 74)
        scoreText = pygame.font.Font(None, 24).render(f"Score: {score}" , True, (255, 0, 0))
        screen.blit(scoreText, (WIDTH // 2 - scoreText.get_width() // 2, HEIGHT // 1.75 - scoreText.get_height() // 2))
        
        text = font.render("You Blacked Out", True, (255, 255, 255))
        screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
        
        retryText = font = pygame.font.Font(None, 50).render("Press 'R' to Retry", True, (255, 255, 255))
        screen.blit(retryText, (WIDTH // 2 - retryText.get_width() // 2, HEIGHT // 1.2 - retryText.get_height() // 2))

    # Event handling
    for event in pygame.event.get():
            # Quit Game Function
            if event.type == pygame.QUIT:
                run = False
            # Restart Game Function
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r and game_over:
                    score = current_time = 0
                    start_time = pygame.time.get_ticks()
                    player_health = PlayerHealth(initial_health=100)
                    obstacles = [Obstacle() for _ in range(5)]
                    health_item.x = random.randint(50, WIDTH - 50)
                    health_item.y = random.randint(50, HEIGHT - 50)
                    game_over = False

    # Update the display 
    pygame.display.flip()  
pygame.quit()