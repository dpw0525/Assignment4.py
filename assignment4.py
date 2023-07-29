import csv
import math
from Shapes import Polygon, Circle, Cube, Cuboid, Cylinder 

import csv

class Solver:
    @staticmethod
    def read_csv_file(file):
        shapes = []
        with open(file, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for row in reader:
                if row[0] == "prism":
                    shape = Polygon(float(row[1]), float(row[2]), float(row[3]))
                elif row[0] == "sphere":
                    shape = Circle(float(row[1]))
                elif row[0] == "cube":
                    shape = Cube(float(row[1]))
                elif row[0] == "cuboid":
                    shape = Cuboid(float(row[1]), float(row[2]), float(row[3]))
                elif row[0] == "cylinder":
                    shape = Cylinder(float(row[1]), float(row[2]))
                shapes.append((shape, int(row[4])))
        return shapes
    
    def calculate(shapes):
        total = 0
        for shape, scale in shapes:
            total += shape.volume() * scale
        return total

if __name__ == "__main__":
    shapes = Solver.read_csv_file('examples3.csv')
    total = Solver.calculate(shapes)
    print(total)

 #Calculate and print the volume and surface area of each shape
print("Cube volume:", cube.get_volume())
print("Cube surface area:", cube.get_surface_area())

print("Sphere volume:", sphere.get_volume())
print("Sphere surface area:", sphere.get_surface_area())

print("Cylinder volume:", cylinder.get_volume())
print("Cylinder surface area:", cylinder.get_surface_area())

print("Prism volume:", Polygon.GetArea())
print("Prism surface area:", Polygon.GetPerimeter())
