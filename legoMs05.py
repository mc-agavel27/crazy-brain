#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, UltrasonicSensor
from pybricks.parameters import Port
from pybricks.tools import wait

ev3 = EV3Brick()

obstacle_sensor = UltrasonicSensor(Port.S2)

motor = Motor(Port.D)
car = Motor(Port.A)

ev3.speaker.beep()
ev3.screen.clear()

def weapon_systems(doActivate):
    if(doActivate):
        motor.run(10000)
    else:
        motor.run(0)

def get_distance():
    return obstacle_sensor.distance()

def activate():
    car.run(10000)

    while(True):
        ev3.screen.print("Dist: " + str(distance) + " mm")
        if get_distance() <= 300:
            weapon_systems(True)
        else:
            weapon_systems(False)

activate()