#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.ev3devices import TouchSensor
from pybricks.parameters import Port

# Create your objects here

# Initialize the EV3 Brick.
ev3 = EV3Brick()

arms_motor = Motor(Port.D)
legs_motor = Motor(Port.A)
touch_sensor = TouchSensor(Port.S1)

while(True):
    if touch_sensor.pressed():
        arms_motor.run(5000)
        legs_motor.run(5000)
    else:
        arms_motor.run(0)
        legs_motor.run(0)