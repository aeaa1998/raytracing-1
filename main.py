from sphere import Sphere, Material
from raytracer import Raytracer
from lib import *
white = Material(diffuse=color(255, 255, 255))
eye = Material(diffuse=color(134, 129, 120))
black = Material(diffuse=color(0, 0, 0))
button = Material(diffuse=color(24, 24, 24))
carrot = Material(diffuse=color(255, 172, 4))


r = Raytracer(1000, 1000)
r.scene = [
  # Sphere(V3(0, 1, -8), 1.7, white),
Sphere(V3(0, 0.99, -5), 0.7, white),
Sphere(V3(0, -0.1, -5), 0.9, white),
  Sphere(V3(0, -1.4, -5), 1.2, white),
Sphere(V3(0, -1.5, -4), 0.23, button),
Sphere(V3(0, -1, -4), 0.15, button),
Sphere(V3(0, -0.6, -4), 0.1, button),
Sphere(V3(0, 0.5, -4), 0.045, button),
Sphere(V3(0.15, 0.52, -4), 0.045, button),
Sphere(V3(-0.15, 0.52, -4), 0.045, button),
Sphere(V3(0.3, 0.54, -4), 0.045, button),
Sphere(V3(-0.3, 0.54, -4), 0.045, button),
Sphere(V3(0, 0.75, -4), 0.09, carrot),
Sphere(V3(-.2, 1, -4), 0.07, eye),
Sphere(V3(.2, 1, -4), 0.07, eye),
Sphere(V3(-.17, .88, -3.5), 0.03, black),
Sphere(V3(.17, .88, -3.5), 0.03, black),
]
r.render()
r.write('out.bmp')