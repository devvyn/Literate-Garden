// Barkour - Web Canvas Implementation
// Uses shared architecture from ../shared/barkour_config.json

// Load configuration
let CONFIG = null;

fetch('../../shared/barkour_config.json')
    .then(r => r.json())
    .then(config => {
        CONFIG = config;
        initGame();
    })
    .catch(err => {
        console.error('Failed to load config:', err);
        alert('Error loading game config. Make sure shared/barkour_config.json exists!');
    });

// === PowerUpManager (same logic as Python version) ===
class PowerUpManager {
    constructor(config) {
        this.powered = false;
        this.timer = 0;
        this.duration = config.powerup.duration_ms;
    }

    collectBacon() {
        this.powered = true;
        this.timer = this.duration;
    }

    update(dt) {
        if (this.powered) {
            this.timer -= dt;
            if (this.timer <= 0) {
                this.powered = false;
                this.timer = 0;
            }
        }
    }

    isPowered() {
        return this.powered;
    }

    getTimeRemaining() {
        return Math.max(0, this.timer / 1000);
    }
}

// === Bacon (same logic as Python version) ===
class Bacon {
    constructor(x, y) {
        this.x = x;
        this.y = y;
        this.width = 30;
        this.height = 20;
        this.collected = false;
        this.bobOffset = 0;
        this.bobSpeed = 0.1;
    }

    update() {
        if (!this.collected) {
            this.bobOffset += this.bobSpeed;
        }
    }

    getRect() {
        const bobY = this.y + Math.sin(this.bobOffset) * 5;
        return {
            x: this.x,
            y: bobY,
            width: this.width,
            height: this.height
        };
    }

    draw(ctx, config) {
        if (this.collected) return;

        const rect = this.getRect();
        const [pink_r, pink_g, pink_b] = config.colors.bacon_pink;
        const [red_r, red_g, red_b] = config.colors.bacon_red;

        // Bacon body
        ctx.fillStyle = `rgb(${pink_r}, ${pink_g}, ${pink_b})`;
        ctx.beginPath();
        ctx.roundRect(rect.x, rect.y, rect.width, rect.height, 3);
        ctx.fill();

        // Red streaks
        ctx.strokeStyle = `rgb(${red_r}, ${red_g}, ${red_b})`;
        ctx.lineWidth = 3;
        for (let i = 0; i < 3; i++) {
            const stripeY = rect.y + (i * 7);
            ctx.beginPath();
            ctx.moveTo(rect.x + 3, stripeY);
            ctx.lineTo(rect.x + rect.width - 3, stripeY);
            ctx.stroke();
        }
    }
}

// === Player (same logic as Python version) ===
class Player {
    constructor(x, y, powerManager, config) {
        this.x = x;
        this.y = y;
        this.width = config.player.width;
        this.height = config.player.height;
        this.velocityX = 0;
        this.velocityY = 0;
        this.onGround = false;
        this.touchingWall = null;
        this.canWallJump = false;
        this.wallJumpCooldown = 0;
        this.powerManager = powerManager;
        this.wallSlideParticles = [];
        this.config = config;
        // Jump feel mechanics (per spec)
        this.coyoteTimer = 0;
        this.jumpBufferTimer = 0;
        this.wasOnGround = false;
    }

    getMovementSpeed() {
        if (this.powerManager.isPowered()) {
            return this.config.physics.base_movement_speed * this.config.powerup.speed_multiplier;
        }
        return this.config.physics.base_movement_speed;
    }

    getJumpStrength() {
        if (this.powerManager.isPowered()) {
            return this.config.physics.base_jump_strength * this.config.powerup.jump_multiplier;
        }
        return this.config.physics.base_jump_strength;
    }

    getWallJumpStrength() {
        let strength = this.config.physics.wall_jump_strength;
        if (this.powerManager.isPowered()) {
            strength *= this.config.powerup.wall_jump_multiplier;
        }
        return strength;
    }

    checkWallCollision(walls) {
        if (this.wallJumpCooldown > 0) {
            this.wallJumpCooldown--;
            return null;
        }

        const playerRect = this.getRect();

        for (const wall of walls) {
            if (this.rectCollision(playerRect, wall)) {
                if (this.velocityX > 0) return "right";
                if (this.velocityX < 0) return "left";
            }
        }
        return null;
    }

    update(keys, platforms, walls, jumpPressed = false) {
        const COYOTE_TIME = this.config.physics.coyote_time_frames || 6;
        const JUMP_BUFFER = this.config.physics.jump_buffer_frames || 4;

        // Track coyote time (frames since leaving ground)
        if (this.wasOnGround && !this.onGround) {
            // Just left the ground
            this.coyoteTimer = COYOTE_TIME;
        } else if (this.onGround) {
            this.coyoteTimer = COYOTE_TIME;
        } else if (this.coyoteTimer > 0) {
            this.coyoteTimer--;
        }
        this.wasOnGround = this.onGround;

        // Track jump buffer (frames since jump pressed)
        if (jumpPressed) {
            this.jumpBufferTimer = JUMP_BUFFER;
        } else if (this.jumpBufferTimer > 0) {
            this.jumpBufferTimer--;
        }

        // Apply gravity (reduced when wall sliding)
        if (this.touchingWall && this.velocityY > 0 && !this.onGround) {
            this.velocityY = Math.min(this.velocityY + this.config.physics.gravity,
                                     this.config.physics.wall_slide_speed);
            // Add slide particles
            if (this.wallSlideParticles.length < 3) {
                const particleX = this.touchingWall === "left" ? this.x : this.x + this.width;
                this.wallSlideParticles.push({
                    x: particleX,
                    y: this.y + this.height / 2,
                    life: 20
                });
            }
        } else {
            this.velocityY += this.config.physics.gravity;
            if (this.velocityY > this.config.physics.max_fall_speed) {
                this.velocityY = this.config.physics.max_fall_speed;
            }
        }

        // Update particles
        this.wallSlideParticles = this.wallSlideParticles.filter(p => p.life > 0);
        this.wallSlideParticles.forEach(p => {
            p.life--;
            p.y += 2;
        });

        // Horizontal movement
        const movementSpeed = this.getMovementSpeed();
        if (keys.ArrowLeft) {
            this.velocityX = -movementSpeed;
        } else if (keys.ArrowRight) {
            this.velocityX = movementSpeed;
        } else {
            this.velocityX = 0;
        }

        // Check wall collision
        this.touchingWall = this.checkWallCollision(walls);
        this.canWallJump = this.touchingWall !== null && !this.onGround;

        // Determine if we can jump (coyote time allows jumping shortly after leaving ground)
        const canGroundJump = this.onGround || this.coyoteTimer > 0;
        const wantToJump = jumpPressed || this.jumpBufferTimer > 0;

        // Jumping (regular or wall jump)
        if (wantToJump) {
            if (canGroundJump) {
                // Regular jump (or coyote jump)
                this.velocityY = this.getJumpStrength();
                this.onGround = false;
                this.coyoteTimer = 0;  // Consume coyote time
                this.jumpBufferTimer = 0;  // Consume buffer
            } else if (this.canWallJump) {
                // WALL JUMP!
                const pushDirection = this.touchingWall === "left" ?
                    this.config.physics.wall_jump_push : -this.config.physics.wall_jump_push;
                this.velocityX = pushDirection;
                this.velocityY = this.getWallJumpStrength();
                this.touchingWall = null;
                this.canWallJump = false;
                this.wallJumpCooldown = 10;
                this.jumpBufferTimer = 0;  // Consume buffer
            }
        }

        // Update position
        this.x += this.velocityX;
        this.y += this.velocityY;

        // Check platform collisions
        this.onGround = false;
        const playerRect = this.getRect();

        for (const platform of platforms) {
            if (this.rectCollision(playerRect, platform)) {
                if (this.velocityY > 0) { // Falling
                    this.y = platform.y - this.height;
                    this.velocityY = 0;
                    this.onGround = true;
                    this.touchingWall = null;
                } else if (this.velocityY < 0) { // Jumping into platform
                    this.y = platform.y + platform.height;
                    this.velocityY = 0;
                }
            }
        }

        // Keep in bounds
        if (this.x < 0) this.x = 0;
        if (this.x + this.width > this.config.game.screen.width) {
            this.x = this.config.game.screen.width - this.width;
        }
    }

    getRect() {
        return {
            x: this.x,
            y: this.y,
            width: this.width,
            height: this.height
        };
    }

    rectCollision(rect1, rect2) {
        return rect1.x < rect2.x + rect2.width &&
               rect1.x + rect1.width > rect2.x &&
               rect1.y < rect2.y + rect2.height &&
               rect1.y + rect1.height > rect2.y;
    }

    draw(ctx) {
        // Draw wall slide particles
        this.wallSlideParticles.forEach(p => {
            const alpha = p.life / 20;
            const [r, g, b] = this.config.colors.power_glow.slice(0, 3);
            ctx.fillStyle = `rgba(200, 220, 255, ${alpha})`;
            ctx.beginPath();
            ctx.arc(p.x, p.y, 3, 0, Math.PI * 2);
            ctx.fill();
        });

        // Draw glow if powered
        if (this.powerManager.isPowered()) {
            const [r, g, b, a] = this.config.colors.power_glow;
            ctx.fillStyle = `rgba(${r}, ${g}, ${b}, ${a / 255})`;
            ctx.fillRect(this.x - 10, this.y - 10, this.width + 20, this.height + 20);
        }

        // Body color
        const bodyColor = this.powerManager.isPowered() ?
            this.config.colors.tilly_powered : this.config.colors.tilly_beige;
        const [br, bg, bb] = bodyColor;
        ctx.fillStyle = `rgb(${br}, ${bg}, ${bb})`;

        // Tilt when wall sliding
        if (this.touchingWall && !this.onGround) {
            ctx.fillRect(this.x, this.y, this.width, this.height);
        } else {
            ctx.fillRect(this.x, this.y, this.width, this.height);
        }

        // Muzzle
        const [mr, mg, mb] = this.config.colors.tilly_black;
        ctx.fillStyle = `rgb(${mr}, ${mg}, ${mb})`;
        ctx.fillRect(this.x + 5, this.y + this.height - 15, 15, 10);

        // Wall jump indicator
        if (this.canWallJump) {
            const indicatorX = this.touchingWall === "left" ? this.x - 15 : this.x + this.width + 5;
            ctx.fillStyle = 'rgb(100, 255, 100)';
            ctx.beginPath();
            ctx.arc(indicatorX, this.y + this.height / 2, 5, 0, Math.PI * 2);
            ctx.fill();
        }
    }
}

// === Game State ===
let canvas, ctx;
let powerManager, player, platforms, walls, bacons;
let keys = {};
let jumpPressedThisFrame = false;
let lastTime = 0;

function initGame() {
    // Setup canvas
    canvas = document.getElementById('gameCanvas');
    canvas.width = CONFIG.game.screen.width;
    canvas.height = CONFIG.game.screen.height;
    ctx = canvas.getContext('2d');

    // Create game objects (same as Python version)
    powerManager = new PowerUpManager(CONFIG);
    player = new Player(CONFIG.player.start_x, CONFIG.player.start_y, powerManager, CONFIG);

    // Load level from config
    platforms = CONFIG.levels.demo.platforms;
    walls = CONFIG.levels.demo.walls;
    bacons = CONFIG.levels.demo.bacon.map(b => new Bacon(b.x, b.y));

    // Input handling
    window.addEventListener('keydown', e => {
        keys[e.key] = true;
        if (e.key === ' ' || e.key === 'ArrowUp') {
            jumpPressedThisFrame = true;
            e.preventDefault(); // Prevent page scroll
        }
    });
    window.addEventListener('keyup', e => keys[e.key] = false);

    // Start game loop
    requestAnimationFrame(gameLoop);
}

function gameLoop(currentTime) {
    const dt = currentTime - lastTime;
    lastTime = currentTime;

    // Update
    player.update(keys, platforms, walls, jumpPressedThisFrame);
    jumpPressedThisFrame = false;  // Reset after use
    powerManager.update(dt);
    bacons.forEach(b => b.update());

    // Check bacon collision
    const playerRect = player.getRect();
    bacons.forEach(bacon => {
        if (!bacon.collected) {
            const baconRect = bacon.getRect();
            if (player.rectCollision(playerRect, baconRect)) {
                bacon.collected = true;
                powerManager.collectBacon();
            }
        }
    });

    // Render
    render();

    requestAnimationFrame(gameLoop);
}

function render() {
    // Clear screen
    const [r, g, b] = CONFIG.colors.sky_blue;
    ctx.fillStyle = `rgb(${r}, ${g}, ${b})`;
    ctx.fillRect(0, 0, canvas.width, canvas.height);

    // Draw platforms
    const [pr, pg, pb] = CONFIG.colors.ground_brown;
    ctx.fillStyle = `rgb(${pr}, ${pg}, ${pb})`;
    platforms.forEach(p => ctx.fillRect(p.x, p.y, p.width, p.height));

    // Draw walls
    const [wr, wg, wb] = CONFIG.colors.wall_gray;
    ctx.fillStyle = `rgb(${wr}, ${wg}, ${wb})`;
    walls.forEach(w => {
        ctx.fillRect(w.x, w.y, w.width, w.height);
        // Texture lines
        ctx.strokeStyle = 'rgba(80, 80, 100, 0.5)';
        ctx.lineWidth = 2;
        for (let i = 0; i < w.height; i += 20) {
            ctx.beginPath();
            ctx.moveTo(w.x, w.y + i);
            ctx.lineTo(w.x + w.width, w.y + i);
            ctx.stroke();
        }
    });

    // Draw bacon
    bacons.forEach(b => b.draw(ctx, CONFIG));

    // Draw player
    player.draw(ctx);

    // Draw UI
    drawUI();
}

function drawUI() {
    ctx.font = '24px "Courier New", monospace';
    ctx.textAlign = 'center';

    if (powerManager.isPowered()) {
        const timeRemaining = powerManager.getTimeRemaining().toFixed(1);
        // Background
        ctx.fillStyle = 'rgba(50, 50, 50, 0.8)';
        ctx.fillRect(canvas.width / 2 - 150, 30, 300, 40);
        // Text
        ctx.fillStyle = 'rgb(255, 215, 0)';
        ctx.font = '32px "Courier New", monospace';
        ctx.fillText(`🥓 BACON POWER: ${timeRemaining}s`, canvas.width / 2, 58);
    } else {
        ctx.fillStyle = 'rgba(200, 200, 200, 0.9)';
        ctx.font = '20px "Courier New", monospace';
        ctx.fillText('Collect bacon for POWER! Touch walls to WALL JUMP!', canvas.width / 2, 50);
    }
}
