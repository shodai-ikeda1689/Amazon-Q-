import pygame
import sys
import random

# 初期化
pygame.display.init()
pygame.font.init()

# 画面設定
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("ボールキャッチゲーム")

# 色の定義
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# プレイヤー設定
player_width = 100
player_height = 20
player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT - 50
player_speed = 10

# ボール設定
ball_radius = 15
ball_x = random.randint(ball_radius, WIDTH - ball_radius)
ball_y = 0
initial_ball_speed = 5
ball_speed = initial_ball_speed

# スコア
score = 0
font = pygame.font.Font(None, 36)

# ゲームループ
clock = pygame.time.Clock()
running = True

while running:
    # イベント処理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    
    # キー入力処理
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_width:
        player_x += player_speed
    
    # ボールの移動
    ball_y += ball_speed
    
    # ボールがプレイヤーに当たったかチェック
    if (player_y - ball_radius <= ball_y <= player_y + player_height and
            player_x <= ball_x <= player_x + player_width):
        score += 1
        ball_x = random.randint(ball_radius, WIDTH - ball_radius)
        ball_y = 0
        ball_speed += 0.2  # ボールの速度を少し上げる
    
    # ボールが画面外に出たかチェック
    elif ball_y > HEIGHT:
        score -= 1
        ball_x = random.randint(ball_radius, WIDTH - ball_radius)
        ball_y = 0
    
    # 描画
    screen.fill(WHITE)
    
    # プレイヤーの描画
    pygame.draw.rect(screen, BLUE, (player_x, player_y, player_width, player_height))
    
    # ボールの描画
    pygame.draw.circle(screen, RED, (ball_x, ball_y), ball_radius)
    
    # スコアの表示
    score_text = font.render(f"スコア: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))
    
    # 画面更新
    pygame.display.flip()
    clock.tick(60)

# 終了処理
pygame.quit()
sys.exit()
