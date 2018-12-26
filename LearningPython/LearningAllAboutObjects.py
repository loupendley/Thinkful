#   This is from the book Python For Evrybody, by Charles R. Severance,
#   Page 178

from party import PartyAnimal

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

# class PartyAnimal:
#     x = 0
#     name = ''
#
#     def __init__(self, nam):
#         self.name = nam
#         print(self.name, 'constructed')
#
#     def party(self):
#         self.x = self.x + 1
#         print(self.name, 'attended party number', self.x)



s = PartyAnimal('Sylvia')
j = PartyAnimal('Jim')

s.party()
j.party()
s.party()



