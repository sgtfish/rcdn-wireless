from Adafruit_MotorHAT import Adafruit_MotorHAT

class Robot(object):
    def __init__(self, addr=0x60, pumpkin_id=4, pumpkin_trim=0):
        # Initialize motor HAT and left, right motor.
        self._mh = Adafruit_MotorHAT(addr)
        self._pumpkin = self._mh.getMotor(pumpkin_id)

        # Start with motors turned off.
        self._pumpkin.run(Adafruit_MotorHAT.RELEASE)

    def _pumpkin_speed(self, speed):
        #assert 0 <= speed <= 255, 'Speed must be a value between 0 to 255 inclusive!'
        speed = max(0, min(255, speed))  # Constrain speed to 0-255 after trimming.
        self._pumpkin.setSpeed(speed)

    def _spin_left(self, speed):
        self._pumpkin_speed(speed)
        self._pumpkin.run(Adafruit_MotorHAT.BACKWARD)

    def _spin_right(self, speed, seconds=None):
        self._pumpkin_speed(speed)
        self._pumpkin.run(Adafruit_MotorHAT.FORWARD)


    def _spin(self, lspeed, rspeed):
        if(lspeed > rspeed):
            self._spin_right(rspeed)
        if(rspeed > lspeed):
            self._spin_left(lspeed)
