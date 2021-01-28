from pyvesync import VeSync
from pystray import Icon as icon, Menu as menu, MenuItem as item
from PIL import Image
import json

# Rename account-ex.json to account.json and fill in your VeSync account details
with open('account.json') as j:
  account = json.load(j)

dd = []
de = []

def refreshList():
    manager = VeSync(account['email'], account['password'], time_zone=account['timezone'])
    manager.login()
    manager.update()
    firstRun = 0
    dd.clear()
    de.clear()
    for device in manager.outlets:
        dd.append(device.displayJSON()['Device Name'])
        de.append(device.displayJSON()['Status'])
    return manager

manager = refreshList()
  
def toggle(x):
    def inner(icon, item):
        if de[x]=='on':
            manager.outlets[x].turn_off()
            de[x]='off'
        elif de[x]=='off':
            manager.outlets[x].turn_on()
            de[x]='on'
    return inner
    
menuObj=menu(lambda: [
    item(dd[i],toggle(i))
    for i in range(0,len(dd))]
    + [menu.SEPARATOR]
    + [item('Refresh Devices', lambda icon, item: refreshList())]
    + [item('Exit', lambda icon, item: icon.stop())]
)

# Plug icon made by https://www.flaticon.com/authors/pixel-perfect
icon("VeTray", icon=Image.open("plug.png"), title="VeTray", menu=menuObj).run()