#   This is from the book Python For Everybody, by Charles R. Severance,
#   Page 178

from party import PartyAnimal

class CricketFan(PartyAnimal):
    points = 0

    def six(self):
        self.points = self.points + 6
        self.party()
        print(self.name, "just completed {} party, darty points".format(self.points))


#     x = 0
#
#     def __init__(self):
#         print("I am constructed.")
#
#     def party(self):
#         self.x = self.x + 1
#         print("So far", self.x)
#
#     def __del__(self):
#         print('I am destructed', self.x)


# an = PartyAnimal()
# an.party()
# an.party()
# an = 42
# print('an contains', an)
# print("the Type of an is {}".format(type(an)))
# print("the Dir of an is {}".format(dir(an)))
# print("the type  of an.x is {}".format(type(an.x)))
# print("the Type of type(an.party) is {}".format(type(an.party)))
# an.party()
# an.party()
# an.party()
# PartyAnimal.party(an)


s = PartyAnimal('Sylvia')
s.party()
j = PartyAnimal("Jim")
j.party()
print("object \"j\" is now a {}".format(type(j)))
j = CricketFan('Jim')
j.party()
j.six()
print("object \"j\" is now a {}".format(type(j)))
print(dir(j))




