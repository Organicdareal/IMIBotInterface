from __future__ import division
import math
from Chassis import Chassis


class ControlsHandler:

    servo_min = 1000  # Min pulse length out of 4096
    servo_max = 4095  # Max pulse length out of 4096
    servo_scale = servo_max - servo_min

    def __init__(self):
        self.chassis = Chassis()
        self.angle = 0
        self.strength = 0
        self.totalFreq = 0

    def setDirection(self):
        x = math.cos(math.radians(self.angle))
        # print int(self.totalFreq), int(self.totalFreq - self.totalFreq * math.fabs(x))

        if x > 0:
            self.chassis.setLeftSpeed(int(self.totalFreq))
            self.chassis.setRightSpeed(int(self.totalFreq - self.totalFreq * x))
        elif x < 0:
            self.chassis.setRightSpeed(int(self.totalFreq))
            self.chassis.setLeftSpeed(int(self.totalFreq - self.totalFreq * math.fabs(x)))

    def move(self, angleBT, strengthBT):
        self.angle = angleBT
        self.strength = strengthBT
        # print angleBT, strengthBT

        if strengthBT == 0:
            self.chassis.stop()
        else:
            factor = strengthBT/100
            self.totalFreq = (self.servo_scale * factor) + self.servo_min
            # print int(freq)

            # if 316 <= self.angle <= 360 or 0 <= self.angle <= 45:
            #     self.chassis.turnRight()
            # elif 46 <= self.angle <= 135:
            #     self.chassis.forward()
            # elif 136 <= self.angle <= 225:
            #     self.chassis.turnLeft()
            # elif 226 <= self.angle <= 315:
            #     self.chassis.reverse()

            if 350 <= self.angle <= 360 or 0 <= self.angle <= 10:
                self.chassis.turnRight()
                self.chassis.setTotalSpeed(int(self.totalFreq))
            elif 11 <= self.angle <= 169:
                self.chassis.forward()
                self.setDirection()
            elif 170 <= self.angle <= 190:
                self.chassis.turnLeft()
                self.chassis.setTotalSpeed(int(self.totalFreq))
            elif 191 <= self.angle <= 349:
                self.chassis.reverse()
                self.setDirection()
