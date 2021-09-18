import random
import math
import time
import arcade


class SpaceCraft(arcade.Sprite):
    def __init__(self, w, h):
        super().__init__(':resources:images/space_shooter/playerShip1_green.png')
        self.width = 48
        self.height = 48
        self.center_x = w//2
        self.center_y = 58
        self.angle = 0
        self.change_angle = 0 
        self.bullet_list = []
        self.speed = 4
        self.score = 0
        self.life = 3
        
       
        
    def rotate(self):
        self.angle += self.change_angle * self.speed
    
    def fire(self):
        self.bullet_list.append(Bullet(self))
        arcade.play_sound(arcade.sound.Sound(':resources:sounds/laser4.wav'))
    
    
class Bullet(arcade.Sprite):
    def __init__(self, host):
        super().__init__(':resources:images/space_shooter/laserRed01.png')
        self.speed = 4
        self.angle = host.angle
        self.center_x = host.center_x
        self.center_y = host.center_y
        
        
    def move(self):
        angle_rad = math.radians(self.angle)
        self.center_x -= self.speed*math.sin(angle_rad)
        self.center_y += self.speed*math.cos(angle_rad)
        
class Enemy(arcade.Sprite):
    def __init__(self, w, h, s=3):
        super().__init__('tasweiro bezar') 
        self.speed = s
        self.center_x = random.randint(0, w)
        self.center_y = h
        self.width = 80
        self.height = 80
        
    def move(self):
        self.center_y -= self.speed       
        
class Game(arcade.Window):
    def __init__(self):
        self.w = 600
        self.h = 600
        super().__init__(self.w, self.h, 'silver spacecraft')
        arcade.set_background_color('Bckgroundimage.jpg')
        self.background_image = arcade.load_texture('Lighthouse.png')
        
        self.me = SpaceCraft(self.w, self.h)
        self.enemy_list = arcade.SpriteList()
        self.next_enemy_time = random.randint(0, 5)
        self.game_start_time = time.time()
        self.start_time = time.time()
        self.life_image = arcade.load_texture('Bckgroundimage.jpg')
        
        
    def on_draw(self):
            arcade.start_render()
            if self.me.life <= 0:
                arcade.set_background_color(arcade.color.BLACK)
                arcade.draw_text('GAME OVER', 150, self.h//2, arcade.color.GREEN, 60)

            else:
                
                arcade.draw_lrwh_rectangle_textured(0, 0, 600, 476, self.background_image)
                
            self.me.draw()
            
            for i in range(len(self.me.bullet_list)):
                self.me.bullet_list[i].draw
                
            for i in range(len(self.enemy_list)):
                self.enemy_list[i].draw()
                
            for life in range(self.me.life):
                   life_image = arcade.load_texture('heart.png')
                   arcade.draw_lrwh_rectangle_textured(5 + life * 21, 10 , 20, 20 , life_image)
            
            arcade.draw_text(f'score: {self.me.score}', 680, 20, arcade.color.PINK, 20)    
        
    
        
    def on_update(self, delta_time):
        self.me.rotate()
        self.end_time = time.time()
        enemy_time = random.randint(0, 10)
        if (self.end_time - self.start_time) > enemy_time:
                self.enemy_list.append(Enemy(self.w, self.h))
                self.start_time = time.time()
                

        
        #for i in range(len(self.me.bullet_list)):
        #    self.me.bullet_list[i].move()
            
            
        #for i in range(len(self.enemy_list)):
        #        self.enemy_list[i].move()
        
        for bullet in self.me.bullet_list:
            bullet.move()
            
        for enemy in self.enemy_list:
            enemy.move()
            
            
        for bullet in self.me.bullet_list:
            for enemy in self.enemy_list:
                if arcade.check_for_collision(bullet, enemy):
                    self.me.bullet_list.remove(bullet)
                    self.enemy_list.remove(enemy)
                    
                    
                
               
                   
        for Bullet in range(len(self.me.bullet_list)): 
             for Enemy in range(len(self.enemy_list)):          
                if Bullet.center_x == Enemy.center_x:
                  self.enemy_list.remove(enemy)
                elif Bullet.center_y == Enemy.center_y:
                  self.enemy_list.remove()
                  self.me.score += 1
                  
        for enemy in self.enemy_list:
            if enemy.center_y < 0:
                self.me.life -= 1
                self.enemy_list.remove(enemy)
        
        for Bullet in self.me.bullet_list:
            if bullet.center_y > self.height or bullet.center_x > self.width :
                self.me.bullet_list.remove(bullet)               
        
                  
                  
    def on_key_press(self, key, modifiers):
        if key == arcade.key.RIGHT:
            self.me.change_angle = -1
            
        elif key == arcade.key.LEFT:
            self.me.change_angle = 1
            
        elif key == arcade.key.SPACE:
            self.me.fire()
            
            
    def on_key_release(self, key, modifiers): 
        self.me.change_angle = 0 
        
                      
                
def main():
    window = Game()
    window.center_window()
    arcade.run()
    
if __name__ == "__main__":
    main()        
        
game = Game()
arcade.run() 