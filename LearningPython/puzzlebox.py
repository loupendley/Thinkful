# Time: 642ms
# Test Results:
#  Log
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'answer', 'hint', 'hint_two', 'key', 'lock']
# x.hint=How do you normally unlock things?
#
# x.answer=Ha, not quite that easy.
#
# x.hint_two=The lock attribute is a method. Have you called it with anything yet?
#
# x.key=87
# Help on Puzzlebox in module setup object:
#
# class Puzzlebox(builtins.object)
#  |  Puzzlebox for codewars kata.
#  |
#  |  Methods defined here:
#  |
#  |  __init__(self)
#  |
#  |  __repr__(self)
#  |
#  |  lock(self, *args)
#  |
#  |  ----------------------------------------------------------------------
#  |  Data descriptors defined here:
#  |
#  |  __dict__
#  |      dictionary for instance variables (if defined)
#  |
#  |  __weakref__
#  |      list of weak references to the object (if defined)
#  |
#  |  ----------------------------------------------------------------------
#  |  Data and other attributes defined here:
#  |
#  |  answer = 'Ha, not quite that easy.\n'
#  |
#  |  hint = 'How do you normally unlock things?\n'
#  |
#  |  hint_two = 'The lock attribute is a method. Have you called it with an...

def answer(puzzlebox):
    # Print statements are your friend.

    pass

x = Puzzlebox()
print("x={}".format(x))

print(dir(x))
print('x.hint={}'.format(x.hint))
print('x.answer={}'.format(x.answer))
print('x.hint_two={}'.format(x.hint_two))
# print('x.hint_three={}'.format(x.hint_three))
print('x.key={}'.format(x.key))
# print('x.lock={}'.format(lock))
help(x)
# print("help is {}".format(x.key.__doc__))
x.key(28)
print('x.answer={}'.format(x.answer)
# print("answer = {}".format(answer(x.lock(3))))
# print("answer = {}".format(x))
