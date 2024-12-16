# Task 3: Tuple - Point in a Coordinate System
# Write a Python program that uses tuples to represent points in a
# 2D coordinate system. The program should calculate the distance between two points.


class Coordinate:
    def __init__(self):
        self.tuple_1 = ()
        self.tuple_2 = ()

    def input(self):
        
        print("Enter coordinates for the first point (x1, y1):")
        for i in range(2):
            value = int(input(f"Enter {['x', 'y'][i]} coordinate for point 1: "))
            self.tuple_1 = self.tuple_1 + (value,)

        print("Point 1:", self.tuple_1)
        print("Enter coordinates for the second point (x2, y2):")
        for i in range(2):
            value = int(input(f"Enter {['x', 'y'][i]} coordinate for point 2: "))
            self.tuple_2 = self.tuple_2 + (value,)

        print("Point 2:", self.tuple_2)

    def distance(self):
      
        distance = ((self.tuple_2[0] - self.tuple_1[0])**2 + (self.tuple_2[1] - self.tuple_1[1])**2)**0.5
        print(f"Distance between two points: {distance:.2f}")


a = Coordinate()
a.input()
a.distance()
