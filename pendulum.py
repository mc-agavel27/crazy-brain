#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port
import random

# Create your objects here

# Initialize the EV3 Brick.
ev3 = EV3Brick()

ev3.speaker.set_volume(10, which="Beep")

arms_motor = Motor(Port.D)

ev3.speaker.set_speech_options(pitch=0, voice="whisper")
ev3.speaker.say("yo... it's doom time.")

for j in range(1000000):
        arms_motor.run_angle(10000000, j * 10, wait=True)
        arms_motor.run_angle(10000000, -j * 10, wait=True)