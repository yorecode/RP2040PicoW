# webapislcd.py to scroll web jokes and astronauts on LCD1602
# Author: Brian Tiffin
# License: MIT
#
# Started: January 10, 2024
# Modified: 2024-01-10/04:27-0500 
# Tectonics: Tested with Micropython, Dec 23, 2023 uf2.
#            Update lcd1602.py with listings in README
#            flash secrets.py with ssid= and password=
#            flash this to main.py
#
"""Exploring the RPi RP2040 Pico W and SunFounder Kepler kit"""

import network
import time
import urequests
import secrets

import lcd1602

# pick an api or both.
astros = False
jokes = True
    
# not forever
passes = 0
limit = 100

try:
    lcd = lcd1602.LCD()
    lcd.clear()
    lcd.write(0, 0, "Hello world, RPi")
    lcd.write(0, 1, "PicoW Kepler kit")

    wlan=network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(secrets.ssid, secrets.password)

    while not wlan.isconnected():
        print("Waiting for " + secrets.ssid + "...")
        time.sleep(1)


    if astros:
        astronauts = urequests.get("http://api.open-notify.org/astros.json").json()
        print("Active astronauts:")
        for names in astronauts["people"]:
            print(" "*4+names["name"])
        print()

    if jokes:
        while passes < limit:
            passes = passes + 1
            lcd.clear()

            joke = urequests.get("http://official-joke-api.appspot.com/random_joke").json()
            txt = joke["setup"]
            print(txt)
            #lcd.write(0, 0, txt)
            lcd.scrollleft(0, 0, txt)
            time.sleep(1)

            txt = joke["punchline"]
            #lcd.write(0, 1, txt)
            print(txt)
            lcd.scrollleft(0, 1, txt)
            time.sleep(3)

    wlan.disconnect()
    wlan.active(False)

except KeyboardInterrupt:
    wlan.disconnect()
    wlan.active(False)
