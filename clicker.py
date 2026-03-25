#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.ev3devices import TouchSensor
from pybricks.parameters import Port, Color

# Create your objects here

# Initialize the EV3 Brick.
ev3 = EV3Brick()

money = 0
richmode = 1
threshold = 10

arms_motor = Motor(Port.D)
legs_motor = Motor(Port.A)
touch_sensor = TouchSensor(Port.S1)

ev3.speaker.set_volume(1, which="Beep")

while True:
    ev3.screen.draw_text(0, 0, str(money), text_color=Color.BLACK)
    if touch_sensor.pressed():
        # 1. Do your action here
        ev3.speaker.beep(money, 100)
        money += richmode
        print("Money:", money)
        ev3.screen.clear()
        ev3.screen.draw_text(0, 0, str(money), text_color=Color.BLACK)
        ev3.screen.draw_text(0, 20, str(threshold), text_color=Color.BLACK)

        # 2. "Wait for Release" - This loop runs as long as your finger is down
        while touch_sensor.pressed():
            pass # Do nothing, just wait
    
    while(money >= threshold):
        if money >= threshold:
            money -= threshold
            richmode += 1
            threshold *= 1.1
            threshold = round(threshold)
            ev3.screen.clear()
            ev3.screen.draw_text(0, 0, str(money), text_color=Color.BLACK)
            ev3.screen.draw_text(0, 20, str(threshold), text_color=Color.BLACK)