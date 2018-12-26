# this is the class module file

class PartyAnimal(object):
    x = 0
    name = ''

    def __init__(self, nam, x):
        self.name = nam
        self.x = x
        print(self.name, 'constructed')

    def party(self):
        self.x = self.x + 1
        print(self.name, 'attended party number', self.x)

    def add(self, other, x):
        self.x += other.x + x

    def __repr__(self):
        return "Party animal {} is at {} parties, dude.".format( self.nam
                                                                ,self.x)
