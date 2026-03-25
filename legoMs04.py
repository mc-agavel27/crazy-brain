from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, UltrasonicSensor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase
from pybricks.tools import wait

ev3 = EV3Brick()

obstacle_sensor = UltrasonicSensor(Port.S2)

motor = Motor(Port.D)
car1 = Motor(Port.A)
car2 = Motor(Port.B)

car = DriveBase(car1, ca2, wheel_diameter=55.5, axle_track=104)

ev3.speaker.beep()
ev3.screen.clear()

car.drive(10000, 0)

while(True):
    distance = obstacle_sensor.distance()
    ev3.screen.print("Dist: " + str(distance) + " mm")
    if distance <= 300:
        motor.run(10000)
    else:
        motor.run(0)
        