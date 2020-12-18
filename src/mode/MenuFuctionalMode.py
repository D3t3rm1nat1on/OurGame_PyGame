import pygame
from pygame.math import Vector2

from layer import Layer


class MenuFunctional:
    color = [
        [(255, 20, 147), (176, 255, 46)],
        [(176, 255, 46), (255, 20, 147)]]
    theme = 0

    def move_pointer(self, ev, cur_list, menu_type):
        if menu_type == 1 and self.num_ren == 1 and (ev.key == pygame.K_RIGHT or ev.key == pygame.K_LEFT):
            self.button_soung(ev)
            return
        if self.ind > 0:
            if ev.key == pygame.K_UP:
                self.ind -= 1
                cur_list[self.ind + 1][4] = False
                cur_list[self.ind][4] = True
        if self.ind < len(cur_list) - 1:
            if menu_type == 1 and self.num_ren == 1 and self.ind == 2:
                return
            if ev.key == pygame.K_DOWN:
                self.ind += 1
                if self.ind != 0:
                    cur_list[self.ind - 1][4] = False
                cur_list[self.ind][4] = True

    def chosen_button(self, x, y, temp):
        for el in temp:
            if el[1][0] <= x <= (el[1][0] + el[1][2]) and el[1][1] <= y <= (el[1][3] + el[1][1]):
                el[4] = True
            else:
                el[4] = False

    def into_new_render(self, x, y, text):
        for el in text:
            if el[1][0] <= x <= (el[1][0] + el[1][2]) and el[1][1] <= y <= (el[1][3] + el[1][1]) and el[5] != -1:
                self.num_ren = el[5]

    def draw_frame(self, window, x, y, lx, ly):
        wildth = 5
        pygame.draw.line(window, self.color[self.theme][1], (x, y), (x + lx, y), wildth)
        pygame.draw.line(window, self.color[self.theme][1], (x, y), (x, y + ly), wildth)
        pygame.draw.line(window, self.color[self.theme][1], (x, y + ly), (x + lx, y + ly), wildth)
        pygame.draw.line(window, self.color[self.theme][1], (x + lx, y), (x + lx, y + ly), wildth)

    def button(self, window, color_rect, coordinates, text, start_text):
        color_rect = self.color[self.theme][0]
        pygame.draw.rect(window, color_rect, coordinates)
        window.blit(pygame.font.SysFont('Comic Sans MS', 30).render(text, True, (0, 0, 0)),
                    start_text)

    def print_button(self, window, text):
        for i, el in enumerate(text):
            self.button(window, el[0], el[1], el[2], el[3])

    def render_icons(self, window):
        layer = Layer(Vector2(64, 64), "assets/units_spritesheet_scaled.png")
        for i in range(3):
            layer.render_tile(window, Vector2(3.5, 1.2 + i * 1), Vector2(3, 6 + i * 1), Vector2(0.5, 0.5))



class Sound:
    vol = 0

    def __init__(self):
        self.read_music_volume()
        self.play_music(self.vol)

    def lower_sound(self):
        if self.vol > 0:
            self.vol -= 10
            pygame.mixer.music.set_volume(self.vol / 100.0)

    def louder_sound(self):
        if self.vol < 100:
            self.vol += 10
            pygame.mixer.music.set_volume(self.vol / 100.0)

    def play_music(self, volume):
        self.vol = volume
        # pygame.mixer.music.load('assets/song.mp3')
        # pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(self.vol / 100.0)

    def read_music_volume(self):
        with open('src/config.txt', 'r') as f:
            nums = f.read()
        Sound.vol = int(nums)
