# vetray
VeTray is a lightweight Python-powered system tray application that allows the easy control of VeSync Etekcity WiFi Smart Outlets. 

![Screenshot showing VeTray menu on Windows 10](https://i.imgur.com/RqGv0MI.png)

## Getting Started
1. Clone repo contents to a folder
2. Run `pip install pyvesync pystray`
3. Rename `account-ex.json` to `account.json` and input your VeSync account information and [timezone](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)
4. Run `vetray.py`
5. Right click the plug icon in your system tray
6. Click any menu item to toggle the power state of the outlet

Pro-tip: If you're on Windows, you can rename `vetray.py` to `vetray.pyw` to run VeTray without showing the console window.

## Known Issues
If an outlet's power state changes from outside VeTray (either through the VeSync app, a smart assistant, or the physical toggle button), you will have to click the menu option twice to toggle the power state.

<sub><sup>Thanks to [Pixel-Perfect](https://www.flaticon.com/authors/pixel-perfect) from FlatIcon for making the royalty-free plug icon.<sub><sup>
