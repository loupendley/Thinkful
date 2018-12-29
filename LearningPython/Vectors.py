# Create a Vector class with x and a y attributes that represent component magnitudes in the x and y directions.
#
# Your vectors should handle vector additon with an .add() method that takes a second vector as an argument and
# returns a new vector equal to the sum of the vector you call .add() on and the vector you pass in.

# soluzione!!!
#
# class Vector(object):
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def add(self, vector):
#         return Vector(self.x + vector.x, self.y + vector.y)

class Vector(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, other):
        print('zoog self = {}'.format(self))
        # self.x, self.y,  =  other.x + self.x, other.y + self.y
        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return "x value is {}, and y value is {}".format(self.x, self.y)


vector_x = Vector(1, 2)
vector_y = Vector(16, 32)
print("vector_y is: ", vector_y)
print("vector_x is: ", vector_x)
print("vector_x = {}".format(vector_x))

vector_z = vector_x.add(vector_y)
print("after adding vector_y, vetor_x is now... ", vector_x)
print("vector_x now equals {}".format(vector_x))
print("vector_z now equals {}".format(vector_z))
print("vector_z: ", vector_z)
# print("x_vectory new values are {}".format(vector_x))
# vector_x1 = Vector(3, 4)
# print("testcase 1 = {}".format(vector_x1))
# print("Vector(3,4).y = {}".format(Vector(3.4).y))
# test.describe("Basic tests")
# test.it("Vectors have correct x attributes.")
# 1. test.assert_equals(Vector(3, 4).x, 3)
# test.it("Vectors have correct y attributes.")
# 2. test.assert_equals(Vector(3, 4).y, 4)
# test.expect(hasattr(Vector(3, 4), "add"), "Vectors should have an .add() method.")
# test.expect(isinstance(Vector(3, 4).add(Vector(1, 2)), Vector), ".add should return a vector.")
# test.it("Vectors add x components correctly.")
# 3.  test.assert_equals(Vector(3, 4).add(Vector(1, 2)).x, 4)
# test.it("Vectors add y components correctly.")
# 4. test.assert_equals(Vector(3, 4).add(Vector(1, 2)).y, 6)