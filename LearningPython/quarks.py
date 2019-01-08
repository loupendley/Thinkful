class Quark(object):

    """
    You're modelling the interaction between a large number of quarks and have decided to create a
    Quark class so you can generate your own quark objects.

    Quarks are fundamental particles and the only fundamental particle to
    experience all four fundamental forces.

    Your task
    Your Quark class should allow you to create quarks of any valid color
    ("red", "blue", and "green") and
    any valid flavor ('up', 'down', 'strange', 'charm', 'top', and 'bottom').

    Every quark has the same baryon_number (BaryonNumber in C#): 1/3.

    Every quark should have an .interact() (.Interact() in C#) method that
    allows any quark to interact with another quark via the strong force.
    When two quarks interact they exchange colors.

    # >>> q1 = Quark("red", "up")
    # >>> q1.color
    # "red"
    # >>> q1.flavor
    # "up"
    # >>> q2 = Quark("blue", "strange")
    # >>> q2.color
    # "blue"
    # >>> q2.baryon_number
    # 0.3333333333333333
    # >>> q1.interact(q2)
    # >>> q1.color
    # "blue"
    # >>> q2.color
    # "red"
    """

    def __init__(self, color, flavor):
        try:
            assert color in ['red', 'blue', 'green']
        except AssertionError:
            raise AssertionError("Invalid Quark color encountered, {}.".format(color))

        try:
            assert flavor in ['up', 'down', 'strange', 'charm', 'top', 'bottom']
        except AssertionError:
            raise AssertionError("Invalid Quark flavor encountered, {}.".format(flavor))

        self.color = color
        self.flavor = flavor
        self.baryon_number = 1.0/3.0

    def __repr__(self):
        return "Quark has color of {}, and flavor of {}, and baryon_number of {}".format(self.color,
                                                                                         self.flavor,
                                                                                         self.baryon_number)

    def interact(self, other):
        other.color, self.color = self.color, other.color


print("let us start now")
# these should fail, quite well
# q1=Quark(color="pink", flavor="chocolate")
# print("here we go")
# print("q1 object type is {}".format(type(q1)))
# print("we are now done")
q1=Quark(color="blue", flavor="charm")
q2=Quark(color="red",  flavor="up")
print("q1 = {}".format(q1))
print("q2 = {}".format(q2))
print("now, we run interact...")
q1.interact(q2)
print('q1.color={}, q1.flavor={}'.format(q1.color, q1.flavor))
print('q2.color={}, q2.flavor={}'.format(q2.color, q2.flavor))
