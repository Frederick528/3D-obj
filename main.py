from object_3d import *
from camera import *
from projection import *
import pygame as pg

class SoftwareRender:
    def __init__(self):
        pg.init()
        self.RES = self.WIDTH, self.HEIGHT = 1360, 768
        self.H_WIDTH, self.H_HEIGHT = self.WIDTH //2, self.HEIGHT // 2
        self.FPS = 60
        self.screen = pg.display.set_mode(self.RES)
        self.clock = pg.time.Clock()
        self.create_objects()

    def create_objects(self):
        self.camera = Camera(self, [0, -3, -50])
        self.projection = Projection(self)
        self.object1 = self.get_object_from_file('shark/SHARK.obj')
        self.object1.translate([10, 2, 0])
        self.object2 = self.get_object_from_file('stingray/STINGRAY.obj')
        self.object2.translate([5, 10, 0])
        self.object3 = self.get_object_from_file('stingray/STINGRAY.obj')
        self.object3.translate([3, -4, 0])
        self.object4 = self.get_object_from_file('stingray/STINGRAY.obj')
        self.object4.translate([9, -6, 0])
        self.object5 = self.get_object_from_file('stingray/STINGRAY.obj')
        self.object5.translate([13, 6, 0])
        self.object6 = self.get_object_from_file('stingray/STINGRAY.obj')
        self.object6.translate([4, 4, 0])
        self.object7 = self.get_object_from_file('stingray/STINGRAY.obj')
        self.object7.translate([5, 2, 0])
        self.object8 = self.get_object_from_file('stingray/STINGRAY.obj')
        self.object8.translate([1, 7, 0])
        self.object9 = self.get_object_from_file('stingray/STINGRAY.obj')
        self.object9.translate([6, 3, 0])
        self.object10 = self.get_object_from_file('stingray/STINGRAY.obj')
        self.object10.translate([8, 0, 0])
        self.object11 = self.get_object_from_file('stingray/STINGRAY.obj')
        self.object11.translate([9, -4, 0])
        self.object12 = self.get_object_from_file('stingray/STINGRAY.obj')
        self.object12.translate([9, 2, 0])
        self.object13 = self.get_object_from_file('stingray/STINGRAY.obj')
        self.object13.translate([2, 1, 0])
        self.object14 = self.get_object_from_file('stingray/STINGRAY.obj')
        self.object14.translate([5, 2, 0])
        self.object15 = self.get_object_from_file('shark/SHARK.obj')
        self.object15.translate([15, 3, 0])
        self.object16 = self.get_object_from_file('stingray/STINGRAY.obj')
        self.object16.translate([2, 0, 0])
        self.object17 = self.get_object_from_file('stingray/STINGRAY.obj')
        self.object17.translate([8, -4, 0])
        self.object18 = self.get_object_from_file('stingray/STINGRAY.obj')
        self.object18.translate([5, 2, 0])
        self.object19 = self.get_object_from_file('stingray/STINGRAY.obj')
        self.object19.translate([9, -3, 0])
        self.object20 = self.get_object_from_file('stingray/STINGRAY.obj')
        self.object20.translate([5, -4, 0])
        # self.object1 = self.get_object_from_file('Tank/t_34_obj.obj')
        # self.camera = Camera(self, [0.5, 1, -4])
        # self.projection = Projection(self)
        # self.object = Object3D(self)
        # self.object.translate([0.2, 0.4, 0.2])
        # self.axes = Axes(self)
        # self.axes.translate([0.7, 0.9, 0.7])
        # self.world_axes = Axes(self)
        # self.world_axes.movement_flag = False
        # self.world_axes.scale(2.5)
        # self.world_axes.translate([0.0001, 0.0001, 0.0001])

    def get_object_from_file(self, filename):
        vertex, faces = [], []
        with open(filename) as f:
            for line in f:
                if line.startswith('v '):
                    vertex.append([float(i) for i in line.split()[1:]] + [1])
                elif line.startswith('f'):
                    faces_ = line.split()[1:]
                    faces.append([int(face_.split('/')[0]) - 1 for face_ in faces_])
        return Object3D(self, vertex, faces)

    def draw(self):
        self.screen.fill(pg.Color('darkslategray'))
        # self.world_axes.draw()
        # self.axes.draw()
        self.object1.draw_1()
        self.object2.draw_2()
        self.object3.draw_3()
        self.object4.draw_4()
        self.object5.draw_5()
        self.object6.draw_6()
        self.object7.draw_7()
        self.object8.draw_5()
        self.object9.draw_1()
        self.object10.draw_2()
        self.object11.draw_4()
        self.object12.draw_3()
        self.object13.draw_6()
        self.object14.draw_5()
        self.object15.draw_7()
        self.object16.draw_2()
        self.object17.draw_1()
        self.object18.draw_3()
        self.object19.draw_5()
        self.object20.draw_4()

    def run(self):
        while True:
            self.draw()
            self.camera.control()
            [exit() for i in pg.event.get() if i.type == pg.QUIT]
            pg.display.set_caption(str(self.clock.get_fps()))
            pg.display.flip()
            self.clock.tick(self.FPS)

if __name__ == '__main__':
    app = SoftwareRender()
    app.run()

