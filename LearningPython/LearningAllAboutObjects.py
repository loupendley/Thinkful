#   This is from the book Python For Evrybody, by Charles R. Severance,
#   Page 178


class PartyAnimal:
    x = 0


    def party(self):
        self.x = self.x + 1
        print("So far", self.x)


an = PartyAnimal()
print("the Type of an is {}".format(type(an)))
print("the Dir of an is {}".format(dir(an)))
print("the type  of an.x is {}".format(type(an.x)))
print("the Type of type(an.party) is {}".format(type(an.party)))
# an.party()
# an.party()
# an.party()
# PartyAnimal.party(an)


