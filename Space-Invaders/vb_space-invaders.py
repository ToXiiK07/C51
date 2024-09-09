import tkinter as tk
import random
import time


# --- Modèle (Model) ---
class GameModel:
    def __init__(self):
        self.width = 800
        self.height = 600
        self.ship_x = self.width // 2 - 20
        self.ship_y = self.height - 40
        self.ship_speed = 10
        self.ship_bullet_speed = 10
        self.invader_speed = 2
        self.invaders_direction = 1
        self.invaders = []
        self.bullets = []
        self.enemy_bullets = []
        self.shields = []
        self.score = 0
        self.enemies_defeated = 0
        self.wave_number = 1
        self.game_over = False
        self.create_invaders()
        self.create_shields()
        self.last_bullet_time = time.time()
        self.last_enemy_bullet_time = time.time()

    def create_invaders(self):
        self.invaders = []
        for i in range(5):
            for j in range(10):
                x = j * 50 + 30
                y = i * 40 + 30
                self.invaders.append({'x': x, 'y': y, 'type': 'regular'})

    def create_shields(self):
        self.shields = [{'x': 100 * i + 50, 'y': self.height - 150, 'life': 10} for i in range(7)]

    def fire_bullet(self):
        current_time = time.time()
        if not self.game_over and (current_time - self.last_bullet_time >= 0.3):
            self.bullets.append([self.ship_x + 20, self.ship_y])
            self.last_bullet_time = current_time

    def fire_enemy_bullet(self):
        current_time = time.time()
        if not self.game_over and self.invaders and (
                current_time - self.last_enemy_bullet_time >= 1):  # Délai d'une seconde entre les tirs
            for invader in random.sample(self.invaders, min(2, len(self.invaders))):
                if random.random() < 0.60:  # Réduit la probabilité de tir
                    self.enemy_bullets.append([invader['x'] + 20, invader['y'] + 40])
            self.last_enemy_bullet_time = current_time  # Met à jour le temps du dernier tir

    def move_ship(self, direction):
        if not self.game_over:
            self.ship_x = max(0, min(self.width - 40, self.ship_x + direction * self.ship_speed))

    def move_invaders(self):
        if not self.game_over:
            if not self.invaders:
                self.start_new_wave()
                return  # Empêche le mouvement des envahisseurs pendant le démarrage d'une nouvelle vague

            move_down = False
            for invader in self.invaders:
                invader['x'] += self.invader_speed * self.invaders_direction
                if invader['x'] >= self.width - 40 or invader['x'] <= 0:
                    move_down = True

            if move_down:
                self.invaders_direction *= -1
                for invader in self.invaders:
                    invader['y'] += 20
                    if invader['y'] >= self.height - 150:
                        self.game_over = True

    def update_bullets(self):
        self.bullets = [[x, y - self.ship_bullet_speed] for x, y in self.bullets if y > 0]
        self.enemy_bullets = [[x, y + 5] for x, y in self.enemy_bullets if y < self.height]

    def check_collisions(self):
        for bullet in self.bullets:
            for invader in self.invaders:
                if invader['x'] < bullet[0] < invader['x'] + 40 and invader['y'] < bullet[1] < invader['y'] + 40:
                    self.invaders.remove(invader)
                    self.bullets.remove(bullet)
                    self.score += 10
                    self.enemies_defeated += 1
                    break

        for enemy_bullet in self.enemy_bullets:
            if self.ship_x < enemy_bullet[0] < self.ship_x + 40 and self.ship_y < enemy_bullet[1] < self.ship_y + 20:
                self.game_over = True

        for enemy_bullet in self.enemy_bullets[:]:
            for shield in self.shields:
                if shield['x'] < enemy_bullet[0] < shield['x'] + 60 and shield['y'] < enemy_bullet[1] < shield[
                    'y'] + 20:
                    shield['life'] -= 1
                    self.enemy_bullets.remove(enemy_bullet)
                    if shield['life'] <= 0:
                        self.shields.remove(shield)
                    break

    def apply_power_up(self, type_):
        if type_ == 'shield':
            # Add shield effect
            pass
        elif type_ == 'rapid':
            self.ship_bullet_speed = 15
            self.root.after(5000, lambda: self.set_bullet_speed(10))  # Reset speed after 5 seconds

    def get_shield_color(self, shield):
        life_percentage = shield['life'] / 10
        return f'#{int(255 * (1 - life_percentage)):02x}{int(255 * life_percentage):02x}00'

    def start_new_wave(self):
        self.wave_number += 1
        self.create_invaders()

# --- Vue (View) ---
class GameView:
    def __init__(self, root, model):
        self.root = root
        self.model = model
        self.canvas = tk.Canvas(root, width=self.model.width, height=self.model.height, bg='black')
        self.canvas.pack()

    def draw(self):
        self.canvas.delete("all")
        self.draw_ship()
        self.draw_invaders()
        self.draw_bullets()
        self.draw_enemy_bullets()
        self.draw_shields()
        self.draw_stats()

    def draw_ship(self):
        self.canvas.create_rectangle(self.model.ship_x, self.model.ship_y,
                                     self.model.ship_x + 40, self.model.ship_y + 20, fill='blue')

    def draw_invaders(self):
        for invader in self.model.invaders:
            self.canvas.create_rectangle(invader['x'], invader['y'],
                                         invader['x'] + 40, invader['y'] + 40, fill='green')

    def draw_bullets(self):
        for bullet in self.model.bullets:
            self.canvas.create_rectangle(bullet[0], bullet[1],
                                         bullet[0] + 5, bullet[1] + 10, fill='white')

    def draw_enemy_bullets(self):
        for enemy_bullet in self.model.enemy_bullets:
            self.canvas.create_rectangle(enemy_bullet[0], enemy_bullet[1],
                                         enemy_bullet[0] + 5, enemy_bullet[1] + 10, fill='red')

    def draw_shields(self):
        for shield in self.model.shields:
            self.canvas.create_rectangle(shield['x'], shield['y'],
                                         shield['x'] + 60, shield['y'] + 20,
                                         fill=self.get_shield_color(shield))

    def draw_stats(self):
        self.canvas.create_text(self.model.width // 2, 20,
                                text=f"Score: {self.model.score}  Vagues: {self.model.wave_number}",
                                fill='white', font=('Arial', 20))

    def show_game_over_screen(self):
        self.canvas.create_text(self.model.width // 2, self.model.height // 2 - 50,
                                text="GAME OVER", fill='red', font=('Arial', 40, 'bold'))
        self.canvas.create_text(self.model.width // 2, self.model.height // 2,
                                text=f"Score: {self.model.score}", fill='white', font=('Arial', 30))
        self.canvas.create_text(self.model.width // 2, self.model.height // 2 + 50,
                                text=f"Vagues: {self.model.wave_number}", fill='white', font=('Arial', 30))
        self.canvas.create_text(self.model.width // 2, self.model.height // 2 + 100,
                                text="Appuyez sur R pour recommencer", fill='yellow', font=('Arial', 20))

    def clear_game_over_screen(self):
        self.canvas.delete("all")
        self.draw()  # Redessine le jeu sans l'écran de Game Over

    def get_shield_color(self, shield):
        life_percentage = shield['life'] / 10
        return f'#{int(255 * (1 - life_percentage)):02x}{int(255 * life_percentage):02x}00'


# --- Contrôleur (Controller) ---
class GameController:
    def __init__(self, root, model, view):
        self.root = root
        self.model = model
        self.view = view
        self.setup_controls()
        self.update()

    def setup_controls(self):
        self.root.bind("<Left>", lambda event: self.model.move_ship(-1))
        self.root.bind("<Right>", lambda event: self.model.move_ship(1))
        self.root.bind("<space>", lambda event: self.model.fire_bullet())
        self.root.bind("<r>", self.restart_game)

    def update(self):
        if not self.model.game_over:
            self.model.move_invaders()
            self.model.update_bullets()
            self.model.fire_enemy_bullet()
            self.model.check_collisions()
            self.view.draw()
            self.root.after(50, self.update)  # Continuez à mettre à jour le jeu
        else:
            self.view.show_game_over_screen()  # Affiche l'écran de Game Over

    def restart_game(self, event=None):
        # Réinitialisez le modèle
        self.model = GameModel()

        # Réinitialisez la vue
        self.view.clear_game_over_screen()

        # Assurez-vous que les contrôles sont réinitialisés
        self.setup_controls()

        # Relancez la boucle de mise à jour du jeu
        self.update()


# --- Lancer le jeu ---
if __name__ == "__main__":
    root = tk.Tk()
    model = GameModel()
    view = GameView(root, model)
    controller = GameController(root, model, view)
    root.mainloop()
