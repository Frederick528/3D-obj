import pygame as pg
from matrix_functions import *
from numba import njit
import time

@njit(fastmath=True)
def any_func(arr, a, b):
    return np.any((arr == a) | (arr == b))

class Object3D:
    def __init__(self, render, vertexes, faces):
        self.render = render
        self.vertexes = np.array([np.array(v) for v in vertexes])
        self.faces = np.array([np.array(face) for face in faces])
        # self.vertexes = np.array([(0, 0, 0, 1), (0, 1, 0, 1), (1, 1, 0, 1), (1, 0, 0, 1),
        #                           (0, 0, 1, 1), (0, 1, 1, 1), (1, 1, 1, 1), (1, 0, 1, 1)])
                                
        # self.faces = np.array([(0, 1, 2, 3), (4, 5, 6, 7), (0, 4, 5, 1), (2, 3, 7, 6), (1, 2, 6, 5), (0, 3, 7, 4)])
        
        self.font = pg.font.SysFont('Arial', 30, bold=True)
        self.color_faces = [(pg.Color('orange'), face) for face in self.faces]
        self.movement_flag, self.draw_vertexes = True, False
        self.label = ''

    def draw_1(self):
        self.screen_projection()
        self.movement_z1(0.01)
        self.movement_y1(0.07)
        self.movement_x2(0.7)


    def draw_2(self):
        self.screen_projection()
        self.movement_z1(0.02)
        self.movement_y1(0.1)
        self.movement_x2(1)

    def draw_3(self):
        self.screen_projection()
        self.movement_z1(0.02)
        self.movement_y1(0.05)
        self.movement_x2(0.5)

    def draw_4(self):
        self.screen_projection()
        self.movement_z1(0.02)
        self.movement_y1(0.02)
        self.movement_x2(0.2)

    def draw_5(self):
        self.screen_projection()
        self.movement_z1(0.02)
        self.movement_y1(0.06)
        self.movement_x2(0.6)

    def draw_6(self):
        self.screen_projection()
        self.movement_z1(0.01)
        self.movement_y1(0.04)
        self.movement_x2(0.4)

    def draw_7(self):
        self.screen_projection()
        self.movement_y1(0.01)
        self.movement_x2(0.1)
    
    def movement_x1(self, speed):
        if self.movement_flag:
            self.rotate_x(speed)

    def movement_y1(self, speed):
        if self.movement_flag:
            self.rotate_y(speed)
        
    def movement_z1(self, speed):
        if self.movement_flag:
            self.rotate_z(speed)

    def movement_x2(self, speed):
        if self.movement_flag:
            self.move_x(speed)

    def movement_y2(self, speed):
        if self.movement_flag:
            self.move_y(speed)
        
    def movement_z2(self, speed):
        if self.movement_flag:
            self.move_z(speed)

    def screen_projection(self):
        vertexes = self.vertexes @self.render.camera.camera_matrix()
        vertexes = vertexes @self.render.projection.projection_matrix
        vertexes /= vertexes[:, -1].reshape(-1, 1)
        vertexes[(vertexes > 2) | (vertexes < -2)] = 0
        vertexes = vertexes @self.render.projection.to_screen_matrix
        vertexes = vertexes[:, :2]

        for index, color_face in enumerate(self.color_faces):
            color, face = color_face
            polygon = vertexes[face]
            if not any_func(polygon, self.render.H_WIDTH, self.render.H_HEIGHT):
                pg.draw.polygon(self.render.screen, color, polygon, 1)
                if self.label:
                    text = self.font.render(self.label[index], True, pg.Color('white'))
                    self.render.screen.blit(text, polygon[-1])

        if self.draw_vertexes:
            for vertex in vertexes:
                if not any_func(vertex, self.render.H_WIDTH, self.render.H_HEIGHT):
                    pg.draw.circle(self.render.screen, pg.Color('white'), vertex, 2)

    def translate(self, pos):
        self.vertexes = self.vertexes @translate(pos)

    def scale(self, scale_to):
        self.vertexes = self.vertexes @scale(scale_to)
    
    def move_x(self,distance):
        self.vertexes = self. vertexes @move_x(distance)

    def move_y(self,distance):
        self.vertexes = self.vertexes @move_y(distance)
    
    def move_z(self, distance):
        self.vertexes = self.vertexes @move_z(distance)
    
    def rotate_x(self,angle):
        self.vertexes = self. vertexes @rotate_x(angle)

    def rotate_y(self,angle):
        self.vertexes = self.vertexes @rotate_y(angle)
    
    def rotate_z(self, angle):
        self.vertexes = self.vertexes @rotate_z(angle)

class Axes(Object3D):
    def __init__(self, render):
        super().__init__(render)
        self.vertexes = np.array([(0, 0, 0, 1), (1, 0, 0, 1), (0, 1, 0, 1), (0, 0, 1, 1)])
        self.faces = np.array([(0, 1), (0, 2), (0, 3)])
        self.colors = [pg.Color('red'), pg.Color('green'), pg.Color('blue')]
        self.color_faces = [(color, face) for color, face in zip(self.colors, self.faces)]
        self.draw_vertexes = False
        self.label = 'XYZ'