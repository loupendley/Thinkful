import random

class Quark(object):
    # This method is automatically called whenever we create a new quark.
    # It sets the color and flavor attributes when we create an instance.
    def __init__(self, color, flavor, spin):
        self.color = color
        self.flavor = flavor
        value = random.randint(0, 50)
        # if value <= 0.50:
        #     self.spin = -1 / 2
        # else:
        #     self.spin = 1 / 2
        # self.spin = spin
        self.spin = spin

    # Every quark has the same baryon number, so we set this outside the
    # init function.
    baryon_number = 1 / 3
    spin = 0

    # This method models the way quarks interact with one another by
    # exchanging color.
    def interact(self, other_quark):
        self.color, other_quark.color = other_quark.color, self.color
        value = random.randint(0,100)
        if value <= 50:
            self.spin = -1/2
        else:
            self.spin = 1/2

    # The repr method controls how the object is represented by the
    # print() function and other representations of the object.

    def __repr__(self):
        return "{} {} quark with spin of {}".format(self.color, self.flavor, self.spin)

# Now that we have the class set up, let's call Quark() to create two
# actual instances of quark objects.


q1 = Quark("red", "up", 0)
q2 = Quark("blue", "down", 0)

# Print each object to see what they look like.
print("q1 is a {}".format(q1))
print("q2 is a {}".format(q2))

# Test our interact() method by having q1 and q2 interact.
q1.interact(q2)

# Print them out again to see how they changed.
print("Now q1 is a {}".format(q1))
print("Now q2 is a {}".format(q2))

# Print them out again to see how they changed.

q2.interact(q1)
print("again, Now q1 is a {}".format(q1))
print("again, Now q2 is a {}".format(q2))

# Test how our object deals with the built-in type() function.
print("q1 is a {} object".format(type(q1)))
