# this is the class module file

class PartyAnimal(object):
    x = 0
    name = ''

    def __init__(self, name, x=1):  # If we don't specify parties, assume 1.
        name = name.capitalize()
        self.name, self.x = name, x
        if self.x > 1:
            partyname = 'parties'
        else:
            partyname = 'party'
        print('{} just started partying at {} {}'.format(str(self.name),
                                                         self.x,
                                                         partyname))

    def party(self):
        self.x += 1
        print(self.name, 'attended party number', self.x)

    def add(self, other, x):
        try:
            self.x += other.x + x
            print('We just added {} parties to {}'.format(self.x,
                                                          self.name))
        except:
            print('You need to pass a valid party dude, and other is a {}, \
            amigo, and we aren\'t going to fly with it'.format(type(other)))

    def __repr__(self):
        return "Party animal {} is at {} parties, dude." \
            .format(str(self.name).capitalize(), self.x)

    def __del__(self):
        print('Party goer {} just *****  PASSED OUT *****, and is out of the game, at {} parties'\
              .format(self.name, self.x))
