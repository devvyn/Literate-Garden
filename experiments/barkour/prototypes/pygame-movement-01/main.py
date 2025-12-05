#!/usr/bin/env python3
"""
Barkour - PyGame Movement Prototype 01 + Bacon Power-ups + WALL JUMPS!
Focus: Bacon-powered parkour with wall mechanics

Run: python main.py
Controls: Arrow keys to move, Space to jump, touch walls to wall jump!
"""

import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Colors
SKY_BLUE = (135, 206, 235)
GROUND_BROWN = (139, 90, 43)
WALL_GRAY = (100, 100, 120)
TILLY_BEIGE = (210, 180, 140)  # Brownish-blonde
TILLY_BLACK = (30, 30, 30)     # Black muzzle
TILLY_POWERED = (255, 215, 100)  # Golden glow when powered
BACON_PINK = (255, 105, 180)
BACON_RED = (220, 20, 60)
POWER_GLOW = (255, 255, 150, 128)  # Semi-transparent yellow
WALL_SLIDE_PARTICLE = (200, 220, 255)

# Physics parameters (tunable)
GRAVITY = 0.5
BASE_JUMP_STRENGTH = -12
BASE_MOVEMENT_SPEED = 5
MAX_FALL_SPEED = 15
WALL_SLIDE_SPEED = 2  # Slow fall when touching wall
WALL_JUMP_PUSH = 8  # Horizontal push from wall
WALL_JUMP_STRENGTH = -13  # Vertical jump from wall

# Power-up parameters
POWERED_SPEED_MULTIPLIER = 1.5
POWERED_JUMP_MULTIPLIER = 1.2
POWERED_WALL_JUMP_MULTIPLIER = 1.3
POWERUP_DURATION = 5000  # 5 seconds in milliseconds


class PowerUpManager:
    """Manages bacon power-up state"""

    def __init__(self):
        self.powered = False
        self.timer = 0
        self.duration = POWERUP_DURATION

    def collect_bacon(self):
        """Activate power-up"""
        self.powered = True
        self.timer = self.duration

    def update(self, dt):
        """Update power-up timer"""
        if self.powered:
            self.timer -= dt
            if self.timer <= 0:
                self.powered = False
                self.timer = 0

    def is_powered(self):
        return self.powered

    def get_time_remaining(self):
        """Return remaining time in seconds"""
        return max(0, self.timer / 1000.0)


class Bacon:
    """Collectible bacon power-up"""

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 30
        self.height = 20
        self.collected = False
        self.bob_offset = 0  # For floating animation
        self.bob_speed = 0.1

    def update(self):
        """Animate the bacon"""
        if not self.collected:
            self.bob_offset += self.bob_speed

    def get_rect(self):
        """Get collision rect with bobbing animation"""
        bob_y = self.y + math.sin(self.bob_offset) * 5
        return pygame.Rect(self.x, bob_y, self.width, self.height)

    def draw(self, screen):
        """Draw bacon as a simple striped rectangle"""
        if not self.collected:
            rect = self.get_rect()
            # Bacon strips
            pygame.draw.rect(screen, BACON_PINK, rect, border_radius=3)
            # Red streaks
            for i in range(3):
                stripe_y = rect.y + (i * 7)
                pygame.draw.line(screen, BACON_RED,
                               (rect.x + 3, stripe_y),
                               (rect.x + rect.width - 3, stripe_y), 3)


class Player:
    """Tilly the Pekingese with WALL JUMP abilities!"""

    def __init__(self, x, y, power_manager):
        self.x = x
        self.y = y
        self.width = 40
        self.height = 40
        self.velocity_x = 0
        self.velocity_y = 0
        self.on_ground = False
        self.touching_wall = None  # "left", "right", or None
        self.can_wall_jump = False
        self.wall_jump_cooldown = 0  # Prevent instant re-grab
        self.power_manager = power_manager
        self.wall_slide_particles = []

    def get_movement_speed(self):
        """Get current movement speed based on power-up state"""
        if self.power_manager.is_powered():
            return BASE_MOVEMENT_SPEED * POWERED_SPEED_MULTIPLIER
        return BASE_MOVEMENT_SPEED

    def get_jump_strength(self):
        """Get current jump strength based on power-up state"""
        if self.power_manager.is_powered():
            return BASE_JUMP_STRENGTH * POWERED_JUMP_MULTIPLIER
        return BASE_JUMP_STRENGTH

    def get_wall_jump_strength(self):
        """Get wall jump strength (boosted when powered)"""
        strength = WALL_JUMP_STRENGTH
        if self.power_manager.is_powered():
            strength *= POWERED_WALL_JUMP_MULTIPLIER
        return strength

    def check_wall_collision(self, walls):
        """Check if player is touching a wall"""
        if self.wall_jump_cooldown > 0:
            self.wall_jump_cooldown -= 1
            return None

        player_rect = pygame.Rect(self.x, self.y, self.width, self.height)

        for wall in walls:
            if player_rect.colliderect(wall):
                # Check which side we're touching
                if self.velocity_x > 0:  # Moving right, hit right wall
                    return "right"
                elif self.velocity_x < 0:  # Moving left, hit left wall
                    return "left"
        return None

    def update(self, keys, platforms, walls):
        # Apply gravity (reduced when wall sliding)
        if self.touching_wall and self.velocity_y > 0 and not self.on_ground:
            # Wall slide - slow fall
            self.velocity_y = min(self.velocity_y + GRAVITY, WALL_SLIDE_SPEED)
            # Add slide particles
            if len(self.wall_slide_particles) < 3:
                particle_x = self.x if self.touching_wall == "left" else self.x + self.width
                self.wall_slide_particles.append({
                    'x': particle_x,
                    'y': self.y + self.height // 2,
                    'life': 20
                })
        else:
            self.velocity_y += GRAVITY
            if self.velocity_y > MAX_FALL_SPEED:
                self.velocity_y = MAX_FALL_SPEED

        # Update particles
        self.wall_slide_particles = [p for p in self.wall_slide_particles if p['life'] > 0]
        for particle in self.wall_slide_particles:
            particle['life'] -= 1
            particle['y'] += 2

        # Horizontal movement (with power-up boost)
        movement_speed = self.get_movement_speed()
        if keys[pygame.K_LEFT]:
            self.velocity_x = -movement_speed
        elif keys[pygame.K_RIGHT]:
            self.velocity_x = movement_speed
        else:
            self.velocity_x = 0

        # Check wall collision before jump
        self.touching_wall = self.check_wall_collision(walls)
        self.can_wall_jump = self.touching_wall is not None and not self.on_ground

        # Jumping - regular or wall jump
        if keys[pygame.K_SPACE] or keys[pygame.K_UP]:
            if self.on_ground:
                # Regular jump
                self.velocity_y = self.get_jump_strength()
                self.on_ground = False
            elif self.can_wall_jump:
                # WALL JUMP!
                push_direction = WALL_JUMP_PUSH if self.touching_wall == "left" else -WALL_JUMP_PUSH
                self.velocity_x = push_direction
                self.velocity_y = self.get_wall_jump_strength()
                self.touching_wall = None
                self.can_wall_jump = False
                self.wall_jump_cooldown = 10  # Brief cooldown to prevent instant re-grab

        # Update position
        self.x += self.velocity_x
        self.y += self.velocity_y

        # Check collisions with platforms
        self.on_ground = False
        player_rect = pygame.Rect(self.x, self.y, self.width, self.height)

        for platform in platforms:
            if player_rect.colliderect(platform):
                # Simple collision resolution
                if self.velocity_y > 0:  # Falling
                    self.y = platform.top - self.height
                    self.velocity_y = 0
                    self.on_ground = True
                    self.touching_wall = None  # Reset wall touch when landing
                elif self.velocity_y < 0:  # Jumping into platform from below
                    self.y = platform.bottom
                    self.velocity_y = 0

        # Keep player in bounds
        if self.x < 0:
            self.x = 0
        if self.x + self.width > SCREEN_WIDTH:
            self.x = SCREEN_WIDTH - self.width

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, screen):
        """Draw Tilly with power-up visual feedback and wall slide particles"""
        # Draw wall slide particles
        for particle in self.wall_slide_particles:
            alpha = int(255 * (particle['life'] / 20))
            particle_surf = pygame.Surface((6, 6), pygame.SRCALPHA)
            pygame.draw.circle(particle_surf, (*WALL_SLIDE_PARTICLE, alpha), (3, 3), 3)
            screen.blit(particle_surf, (particle['x'], particle['y']))

        # Draw glow effect if powered
        if self.power_manager.is_powered():
            glow_surface = pygame.Surface((self.width + 20, self.height + 20), pygame.SRCALPHA)
            pygame.draw.rect(glow_surface, POWER_GLOW, (0, 0, self.width + 20, self.height + 20), border_radius=5)
            screen.blit(glow_surface, (self.x - 10, self.y - 10))

        # Body color changes when powered
        body_color = TILLY_POWERED if self.power_manager.is_powered() else TILLY_BEIGE

        # Tilt body slightly when wall sliding
        if self.touching_wall and not self.on_ground:
            # Draw rotated rectangle for wall slide pose
            points = [
                (self.x, self.y),
                (self.x + self.width, self.y + 5),
                (self.x + self.width, self.y + self.height),
                (self.x, self.y + self.height - 5)
            ]
            pygame.draw.polygon(screen, body_color, points)
        else:
            pygame.draw.rect(screen, body_color, (self.x, self.y, self.width, self.height))

        # Muzzle (always black)
        muzzle_rect = pygame.Rect(self.x + 5, self.y + self.height - 15, 15, 10)
        pygame.draw.rect(screen, TILLY_BLACK, muzzle_rect)

        # Wall jump indicator
        if self.can_wall_jump:
            indicator_x = self.x - 15 if self.touching_wall == "left" else self.x + self.width + 5
            pygame.draw.circle(screen, (100, 255, 100), (indicator_x, int(self.y + self.height // 2)), 5)


def draw_ui(screen, power_manager):
    """Draw power-up timer UI"""
    font_large = pygame.font.Font(None, 32)
    font_small = pygame.font.Font(None, 24)

    # Controls text
    controls_text = font_small.render("Arrow keys: Move | Space/Up: Jump & WALL JUMP! | ESC: Quit", True, (255, 255, 255))
    screen.blit(controls_text, (10, 10))

    # Power-up status
    if power_manager.is_powered():
        time_remaining = power_manager.get_time_remaining()
        power_text = font_large.render(f"🥓 BACON POWER: {time_remaining:.1f}s", True, (255, 215, 0))
        # Draw background for better visibility
        text_rect = power_text.get_rect()
        text_rect.center = (SCREEN_WIDTH // 2, 40)
        bg_rect = text_rect.inflate(20, 10)
        pygame.draw.rect(screen, (50, 50, 50, 200), bg_rect, border_radius=5)
        screen.blit(power_text, text_rect)
    else:
        hint_text = font_small.render("Collect bacon for POWER! Touch walls to WALL JUMP!", True, (200, 200, 200))
        text_rect = hint_text.get_rect()
        text_rect.center = (SCREEN_WIDTH // 2, 40)
        screen.blit(hint_text, text_rect)


def main():
    """Main game loop"""
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Barkour - Bacon Power + WALL JUMPS!")
    clock = pygame.time.Clock()

    # Create power-up manager
    power_manager = PowerUpManager()

    # Create player (Tilly)
    player = Player(100, 100, power_manager)

    # Create platforms
    platforms = [
        pygame.Rect(0, SCREEN_HEIGHT - 50, SCREEN_WIDTH, 50),  # Ground
        pygame.Rect(200, 450, 150, 20),  # Platform 1
        pygame.Rect(450, 350, 150, 20),  # Platform 2
        pygame.Rect(100, 250, 120, 20),  # Platform 3
        pygame.Rect(600, 200, 150, 20),  # Platform 4
        pygame.Rect(350, 150, 100, 20),  # High platform
    ]

    # Create walls (tall for wall jumping!)
    walls = [
        pygame.Rect(50, 200, 30, 350),   # Left wall
        pygame.Rect(720, 150, 30, 400),  # Right wall
        pygame.Rect(380, 0, 30, 400),    # Center wall
    ]

    # Create bacon collectibles
    bacons = [
        Bacon(300, 400),
        Bacon(500, 300),
        Bacon(150, 200),
        Bacon(650, 150),
        Bacon(400, 100),  # High bacon - need wall jump!
    ]

    # Game loop
    running = True
    while running:
        dt = clock.tick(FPS)  # Delta time in milliseconds

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        # Update
        keys = pygame.key.get_pressed()
        player.update(keys, platforms, walls)
        power_manager.update(dt)

        # Update bacons
        for bacon in bacons:
            bacon.update()

        # Check bacon collision
        player_rect = player.get_rect()
        for bacon in bacons:
            if not bacon.collected and player_rect.colliderect(bacon.get_rect()):
                bacon.collected = True
                power_manager.collect_bacon()

        # Draw
        screen.fill(SKY_BLUE)

        # Draw platforms
        for platform in platforms:
            pygame.draw.rect(screen, GROUND_BROWN, platform)

        # Draw walls
        for wall in walls:
            pygame.draw.rect(screen, WALL_GRAY, wall)
            # Wall texture lines
            for i in range(0, wall.height, 20):
                pygame.draw.line(screen, (80, 80, 100),
                               (wall.x, wall.y + i),
                               (wall.x + wall.width, wall.y + i), 2)

        # Draw bacon
        for bacon in bacons:
            bacon.draw(screen)

        # Draw player
        player.draw(screen)

        # Draw UI
        draw_ui(screen, power_manager)

        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
