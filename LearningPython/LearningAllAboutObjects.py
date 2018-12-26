#   This is from the book Python For Everybody, by Charles R. Severance,
#   Page 178

from party import PartyAnimal

class CricketFan(PartyAnimal):

    points = 0

    def six(self):
        self.points = self.points + 6
        self.party()
        print(self.name, "just completed {} party, darty points".format(self.points))


p = PartyAnimal('phil')
x = PartyAnimal("ximena")
x.add(2300, 'abcd')
assert isinstance(x, object)
print(x)
x.add(PartyAnimal('nikky', 4000), 200)
m = PartyAnimal('mike', 2300)
z = PartyAnimal('Zed')
s = PartyAnimal('sylvia', 1)
s.party()
j = PartyAnimal("Jim", 3)
j.party()
j = CricketFan('Jim', 100)
j.party()
j.six()
# print("object \"j\" is now a {}".format(type(j)))
# print(dir(j))
p = PartyAnimal("Pachuco", 20)
s.add(m, 10)
t = PartyAnimal('Ted', 2)
s.party()
t.add(s, 1000)
t.party()
print(t)
print(s)
print(m)
print(j)
print(z)




