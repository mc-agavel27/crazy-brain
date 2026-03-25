#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port

# Create your objects here

# Initialize the EV3 Brick.
ev3 = EV3Brick()

# Initialize a motor at port B.
test_motor = Motor(Port.A)
arms_motor = Motor(Port.D)

# Write your program here

ev3.screen.load_image("freddy.png")
ev3.speaker.set_speech_options(pitch=0)
ev3.speaker.say("yo... it's me. Golden Freddy Fazbear.")

arms_motor.run(5000)
#ev3.speaker.say("I am in large amounts of physical pain")

for j in range(10):
    test_motor.run_angle(10000, 360 * 4, wait=True)
    test_motor.run_angle(10000, -360 * 2, wait=True)