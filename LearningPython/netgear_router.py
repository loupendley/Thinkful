from pynetgear import Netgear

mypassword = 'password'
netgear = Netgear(password=mypassword)

for i in netgear.get_attached_devices():
    print("attached device = {}".format(i))
