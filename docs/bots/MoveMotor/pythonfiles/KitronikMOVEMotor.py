# microbit-module: KitronikMOVEMotor@2.0.0
# Gerard McCarthy

# based on microbit-module: KitronikMOVEMotor@1.0.0
# and MakeCode module: https://github.com/KitronikLtd/pxt-kitronik-motor-driver
# Copyright (c) Kitronik Ltd 2019.
# The MIT License (MIT)

# for quick lookups of hex values see https://www.prepressure.com/library/technology/ascii-binary-hex
# See datasheet: https://www.nxp.com/docs/en/data-sheet/PCA9632.pdf

from microbit import i2c


# A module to simplify the driving of the motors on Kitronik
# :MOVE Motor buggy with micro:bit
# main constants
CHIP_ADDR = 0x62
# CHIP_ADDR is the standard chip address for the PCA9632,
# datasheet refers to LED control but chip is used for PWM to motor driver
MODE_1_REG_ADDR = 0x00
MODE_1_REG_VALUE = 0x00
# 00000000 setup to normal mode and not to respond to sub address
MODE_2_REG_ADDR = 0x01
MODE_2_REG_VALUE = 0x04
# 00000100 Setup to make changes on ACK, outputs set to open-drain
# open-drain 25 mA current sink capability at 5 V
# in makecode has MODE_2_REG_VALUE = 0x0D 00001101
# Setup to make changes on ACK, outputs set to Totem poled
# totem pole with a 25 mA sink, 10 mA source capability at 5 V.
MOTOR_OUT_ADDR = 0x08  # 00001000 MOTOR output register address
MOTOR_OUT_VALUE = 0xAA   # 10101010 Outputs set to be controlled PWM registers
# Register offsets for the motors
RIGHT_MOTOR_REV = 0x02   # PWM0
RIGHT_MOTOR = 0x03       # PWM1
LEFT_MOTOR = 0x04        # PWM2
LEFT_MOTOR_REV = 0x05    # PWM3
ALL_MOTOR = 0xA2    # 10100010


class MOVEMotor:

    # An initialisation function to setup the PCA9632 chip correctly
    def __init__(self):
        buffer = bytearray(2)
        buffer[0] = MODE_1_REG_ADDR
        buffer[1] = MODE_1_REG_VALUE
        i2c.write(CHIP_ADDR, buffer, False)
        buffer[0] = MODE_2_REG_ADDR
        buffer[1] = MODE_2_REG_VALUE
        i2c.write(CHIP_ADDR, buffer, False)
        buffer[0] = MOTOR_OUT_ADDR
        buffer[1] = MOTOR_OUT_VALUE
        i2c.write(CHIP_ADDR, buffer, False)

    # analog signal required is about 60 to 255
    # input -10 to 0 to 10

    @staticmethod
    def AnalogSpeed(speed):
        # input speed = -10 to 0 to 10
        # output = 60 to 255
        if speed < 0 and speed >= -10:
            return int((speed * -21) + 45)
        elif speed > 0 and speed <= 10:
            return int((speed * 21) + 45)
        else:
            return 0

    def LeftMotor(self, speed=1):
        analog_speed = self.AnalogSpeed(speed)
        motorBuffer = bytearray(2)
        gndPinBuffer = bytearray(2)
        motorBuffer[1] = analog_speed
        gndPinBuffer[1] = 0
        if (speed < 0):
            # going backwards
            motorBuffer[0] = LEFT_MOTOR_REV
            gndPinBuffer[0] = LEFT_MOTOR
        elif (speed > 0):
            # going forwards
            motorBuffer[0] = LEFT_MOTOR
            gndPinBuffer[0] = LEFT_MOTOR_REV
        else:
            # no speed, or stopping
            motorBuffer[0] = LEFT_MOTOR_REV
            gndPinBuffer[0] = LEFT_MOTOR
        i2c.write(CHIP_ADDR, motorBuffer, False)
        i2c.write(CHIP_ADDR, gndPinBuffer, False)

    def RightMotor(self, speed=1):
        analog_speed = self.AnalogSpeed(speed)
        motorBuffer = bytearray(2)
        gndPinBuffer = bytearray(2)
        motorBuffer[1] = analog_speed
        gndPinBuffer[1] = 0
        if (speed < 0):
            # going backwards
            motorBuffer[0] = RIGHT_MOTOR_REV
            gndPinBuffer[0] = RIGHT_MOTOR
        elif (speed > 0):
            # going forwards
            motorBuffer[0] = RIGHT_MOTOR
            gndPinBuffer[0] = RIGHT_MOTOR_REV
        else:
            motorBuffer[0] = RIGHT_MOTOR_REV
            gndPinBuffer[0] = RIGHT_MOTOR
        i2c.write(CHIP_ADDR, motorBuffer, False)
        i2c.write(CHIP_ADDR, gndPinBuffer, False)

    def StopLeft(self):
        stopBuffer = bytearray(2)
        stopBuffer[0] = LEFT_MOTOR
        stopBuffer[1] = 0
        i2c.write(CHIP_ADDR, stopBuffer, False)
        stopBuffer[0] = LEFT_MOTOR_REV
        i2c.write(CHIP_ADDR, stopBuffer, False)

    def StopRight(self):
        stopBuffer = bytearray(2)
        stopBuffer[1] = 0
        stopBuffer[0] = RIGHT_MOTOR
        i2c.write(CHIP_ADDR, stopBuffer, False)
        stopBuffer[0] = RIGHT_MOTOR_REV
        i2c.write(CHIP_ADDR, stopBuffer, False)

    def Stop(self):
        self.StopLeft()
        self.StopRight()

    @staticmethod
    def StraightLimiter(analog_speed, adjustment):
        # limit adjustment to 0 to 20
        # make percentage adjustment (adjustment/max analog) to analog_speed
        if adjustment < 0:
            adjustment = 0
        elif adjustment > 20:
            adjustment = 20
        return int(analog_speed * (255 - adjustment)/255)

    def Reverse(self, speed=1, decrease_left=0, decrease_right=0):
        analog_speed = self.AnalogSpeed(speed)
        motorBuffer = bytearray(5)
        motorBuffer[0] = ALL_MOTOR
        # [1 to 4] is RIGHT_MOTOR_REV; RIGHT_MOTOR; LEFT_MOTOR; LEFT_MOTOR_REV
        motorBuffer[1] = self.StraightLimiter(analog_speed, decrease_right)
        motorBuffer[2] = 0
        motorBuffer[3] = 0
        motorBuffer[4] = self.StraightLimiter(analog_speed, decrease_left)
        i2c.write(CHIP_ADDR, motorBuffer, False)

    def Forward(self, speed=1, decrease_left=0, decrease_right=0):
        analog_speed = self.AnalogSpeed(speed)
        motorBuffer = bytearray(5)
        motorBuffer[0] = ALL_MOTOR
        # [1 to 4] is RIGHT_MOTOR_REV; RIGHT_MOTOR; LEFT_MOTOR; LEFT_MOTOR_REV
        motorBuffer[1] = 0
        motorBuffer[2] = self.StraightLimiter(analog_speed, decrease_right)
        motorBuffer[3] = self.StraightLimiter(analog_speed, decrease_left)
        motorBuffer[4] = 0
        i2c.write(CHIP_ADDR, motorBuffer, False)

    @staticmethod
    def TurnTightnesFactor(tightness='tight'):
        if tightness == 'tight':
            return 8
        elif tightness == 'wide':
            return 1.5
        else:   # standard
            return 3

    def Left(self, speed=1, tightness='standard'):
        # right motor faster than left
        # tightness: tight 8, standard 4, wide 2
        analog_speed = self.AnalogSpeed(speed)
        turn_tightness_factor = self.TurnTightnesFactor(tightness)
        motorBuffer = bytearray(5)
        motorBuffer[0] = ALL_MOTOR
        # [1 to 4] is RIGHT_MOTOR_REV; RIGHT_MOTOR; LEFT_MOTOR; LEFT_MOTOR_REV
        motorBuffer[1] = 0
        motorBuffer[2] = analog_speed
        motorBuffer[3] = int(analog_speed/turn_tightness_factor)
        motorBuffer[4] = 0
        i2c.write(CHIP_ADDR, motorBuffer, False)

    def Right(self, speed=1, tightness='standard'):
        # left motor faster than right
        # tightness: tight 8, standard 4, wide 2
        analog_speed = self.AnalogSpeed(speed)
        turn_tightness_factor = self.TurnTightnesFactor(tightness)
        motorBuffer = bytearray(5)
        motorBuffer[0] = ALL_MOTOR
        # [1 to 4] is RIGHT_MOTOR_REV; RIGHT_MOTOR; LEFT_MOTOR; LEFT_MOTOR_REV
        motorBuffer[1] = 0
        motorBuffer[2] = int(analog_speed/turn_tightness_factor)
        motorBuffer[3] = analog_speed
        motorBuffer[4] = 0
        i2c.write(CHIP_ADDR, motorBuffer, False)

    def Spin(self, speed=1, direction='left'):
        analog_speed = self.AnalogSpeed(speed)
        motorBuffer = bytearray(5)
        motorBuffer[0] = ALL_MOTOR
        # [1 to 4] is RIGHT_MOTOR_REV; RIGHT_MOTOR; LEFT_MOTOR; LEFT_MOTOR_REV
        if direction == 'left':
            motorBuffer[1] = analog_speed
            motorBuffer[2] = 0
            motorBuffer[3] = analog_speed
            motorBuffer[4] = 0
        else:  # right
            motorBuffer[1] = 0
            motorBuffer[2] = analog_speed
            motorBuffer[3] = 0
            motorBuffer[4] = analog_speed
        i2c.write(CHIP_ADDR, motorBuffer, False)
