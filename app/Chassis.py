from __future__ import division
import RPi.GPIO as GPIO
import Adafruit_PCA9685

class Chassis:


    def __init__(self):
        self.pwm = Adafruit_PCA9685.PCA9685()
        self.pwm.set_pwm_freq(60)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(26, GPIO.OUT)
        GPIO.setup(19, GPIO.OUT)
        GPIO.setup(13, GPIO.OUT)
        GPIO.setup(6, GPIO.OUT)
        GPIO.output(26, False)
        GPIO.output(13, False)
        GPIO.output(19, False)
        GPIO.output(6, False)


    def stop(self):
        #print 'stop'
        GPIO.output(26, False)
        GPIO.output(13, False)
        GPIO.output(19, False)
        GPIO.output(6, False)

    def forward(self, tf = 0.1):
        #print 'forward'
        GPIO.output(26, False)
        GPIO.output(13, False)
        GPIO.output(19, True)
        GPIO.output(6, True)
        #time.sleep(tf)

    def reverse(self, tf = 0.1):
        #print 'reverse'
        GPIO.output(19, False)
        GPIO.output(6, False)
        GPIO.output(26, True)
        GPIO.output(13, True)
        #time.sleep(tf)

    def turnLeft(self, tf = 0.1):
        #print 'left'
        GPIO.output(26, False)
        GPIO.output(6, False)
        GPIO.output(13, True)
        GPIO.output(19, True)
        #time.sleep(tf)

    def turnRight(self, tf = 0.1):
        #print 'right'
        GPIO.output(13, False)
        GPIO.output(6, True)
        GPIO.output(19, False)
        GPIO.output(26, True)
        #time.sleep(tf)

    def setLeftSpeed(self, freq):
        self.pwm.set_pwm(0, 0, freq)

    def setRightSpeed(self, freq):
        self.pwm.set_pwm(1, 0, freq)

    def setTotalSpeed(self, freq):
        self.pwm.set_pwm(0, 0, freq)
        self.pwm.set_pwm(1, 0, freq)
