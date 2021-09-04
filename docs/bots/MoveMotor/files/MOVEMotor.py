# MOVEMotor module for motors, line following and distance sensing
# requires microbit v2
# GMC-code; 2021
# The MIT License (MIT)

# A microbit v2 micropython module for the Kitronik :MOVE Motor buggy
# see Kitronic MakeCode module: https://github.com/KitronikLtd/pxt-kitronik-motor-driver
# for quick lookups of hex values
# see https://www.prepressure.com/library/technology/ascii-binary-hex
# See datasheet: https://www.nxp.com/docs/en/data-sheet/PCA9632.pdf

from microbit import i2c, pin1, pin2, pin13, pin14
import machine
import utime


# constants
RIGHT_LINE_SENSOR_PIN = pin1
LEFT_LINE_SENSOR_PIN = pin2
TRIGGER_PIN = pin14
ECHO_PIN = pin13

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


class MOVEMotorMotors:

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

    def stop_left(self):
        stop_buffer = bytearray(2)
        stop_buffer[0] = LEFT_MOTOR
        stop_buffer[1] = 0
        i2c.write(CHIP_ADDR, stop_buffer, False)
        stop_buffer[0] = LEFT_MOTOR_REV
        i2c.write(CHIP_ADDR, stop_buffer, False)

    def stop_right(self):
        stop_buffer = bytearray(2)
        stop_buffer[1] = 0
        stop_buffer[0] = RIGHT_MOTOR
        i2c.write(CHIP_ADDR, stop_buffer, False)
        stop_buffer[0] = RIGHT_MOTOR_REV
        i2c.write(CHIP_ADDR, stop_buffer, False)

    def stop(self):
        self.stop_left()
        self.stop_right()

    @staticmethod
    def _analog_speed(speed):
        # input speed = -10 to 0 to 10
        # output = 60 to 255
        if speed < 0 and speed >= -10:
            return int((speed * -21) + 45)
        elif speed > 0 and speed <= 10:
            return int((speed * 21) + 45)
        else:
            return 0

    def left_motor(self, speed=1, duration=None):
        motor_buffer = bytearray(2)
        gnd_pin_buffer = bytearray(2)
        motor_buffer[1] = self._analog_speed(speed)
        gnd_pin_buffer[1] = 0
        if (speed > 0):
            motor_buffer[0] = LEFT_MOTOR
            gnd_pin_buffer[0] = LEFT_MOTOR_REV
        else:
            motor_buffer[0] = LEFT_MOTOR_REV
            gnd_pin_buffer[0] = LEFT_MOTOR
        i2c.write(CHIP_ADDR, motor_buffer, False)
        i2c.write(CHIP_ADDR, gnd_pin_buffer, False)
        if duration is not None:
            utime.sleep_ms(duration)
            self.stop_left()

    def right_motor(self, speed=1, duration=None):
        motor_buffer = bytearray(2)
        gnd_pin_buffer = bytearray(2)
        motor_buffer[1] = self._analog_speed(speed)
        gnd_pin_buffer[1] = 0
        if (speed > 0):
            motor_buffer[0] = RIGHT_MOTOR
            gnd_pin_buffer[0] = RIGHT_MOTOR_REV
        else:
            motor_buffer[0] = RIGHT_MOTOR_REV
            gnd_pin_buffer[0] = RIGHT_MOTOR
        i2c.write(CHIP_ADDR, motor_buffer, False)
        i2c.write(CHIP_ADDR, gnd_pin_buffer, False)
        if duration is not None:
            utime.sleep_ms(duration)
            self.stop_right()

    @staticmethod
    def _straight_line_adjustment(analog_speed, adjustment):
        # limit adjustment to 0 to 20
        # make percentage adjustment (adjustment/max analog) to _analog_speed
        if adjustment < 0:
            adjustment = 0
        elif adjustment > 20:
            adjustment = 20
        return int(analog_speed * (255 - adjustment)/255)

    def backward(self, speed=1, duration=None, decrease_left=0, decrease_right=0):
        analog_speed = abs(self._analog_speed(speed))
        motor_buffer = bytearray(5)
        motor_buffer[0] = ALL_MOTOR
        # [1 to 4] is RIGHT_MOTOR_REV; RIGHT_MOTOR; LEFT_MOTOR; LEFT_MOTOR_REV
        motor_buffer[1] = self._straight_line_adjustment(analog_speed, decrease_right)
        motor_buffer[2] = 0
        motor_buffer[3] = 0
        motor_buffer[4] = self._straight_line_adjustment(analog_speed, decrease_left)
        i2c.write(CHIP_ADDR, motor_buffer, False)
        if duration is not None:
            utime.sleep_ms(duration)
            self.stop()

    def forward(self, speed=1, duration=None, decrease_left=0, decrease_right=0):
        analog_speed = abs(self._analog_speed(speed))
        motor_buffer = bytearray(5)
        motor_buffer[0] = ALL_MOTOR
        # [1 to 4] is RIGHT_MOTOR_REV; RIGHT_MOTOR; LEFT_MOTOR; LEFT_MOTOR_REV
        motor_buffer[1] = 0
        motor_buffer[2] = self._straight_line_adjustment(analog_speed, decrease_right)
        motor_buffer[3] = self._straight_line_adjustment(analog_speed, decrease_left)
        motor_buffer[4] = 0
        i2c.write(CHIP_ADDR, motor_buffer, False)
        if duration is not None:
            utime.sleep_ms(duration)
            self.stop()

    @staticmethod
    def _turn_radius_factor(radius=25):
        # limit radius (in cm) of inner wheel to 4 to 800 cm
        # calculate the relative speed factor of the inner to outer wheel
        # uses approximate distance between buggy wheels of 8.5 cm
        if radius < 4:
            radius = 4
        elif radius > 800:
            radius = 800
        return (radius + 8.5) / radius

    def left(self, speed=1, radius=25, duration=None):
        # right motor faster than left
        analog_speed = self._analog_speed(speed)
        turn_radius_factor = self._turn_radius_factor(radius)
        motor_buffer = bytearray(5)
        motor_buffer[0] = ALL_MOTOR
        # [1 to 4] is RIGHT_MOTOR_REV; RIGHT_MOTOR; LEFT_MOTOR; LEFT_MOTOR_REV
        motor_buffer[1] = 0
        motor_buffer[2] = analog_speed
        motor_buffer[3] = int(analog_speed/turn_radius_factor)
        motor_buffer[4] = 0
        i2c.write(CHIP_ADDR, motor_buffer, False)
        if duration is not None:
            utime.sleep_ms(duration)
            self.stop()

    def right(self, speed=1, radius=25, duration=None):
        # left motor faster than right
        analog_speed = self._analog_speed(speed)
        turn_radius_factor = self._turn_radius_factor(radius)
        motor_buffer = bytearray(5)
        motor_buffer[0] = ALL_MOTOR
        # [1 to 4] is RIGHT_MOTOR_REV; RIGHT_MOTOR; LEFT_MOTOR; LEFT_MOTOR_REV
        motor_buffer[1] = 0
        motor_buffer[2] = int(analog_speed/turn_radius_factor)
        motor_buffer[3] = analog_speed
        motor_buffer[4] = 0
        i2c.write(CHIP_ADDR, motor_buffer, False)
        if duration is not None:
            utime.sleep_ms(duration)
            self.stop()

    def spin(self, speed=1, direction='left', duration=None):
        analog_speed = abs(self._analog_speed(speed))
        motor_buffer = bytearray(5)
        motor_buffer[0] = ALL_MOTOR
        # [1 to 4] is RIGHT_MOTOR_REV; RIGHT_MOTOR; LEFT_MOTOR; LEFT_MOTOR_REV
        if direction == 'right':
            motor_buffer[1] = analog_speed
            motor_buffer[2] = 0
            motor_buffer[3] = analog_speed
            motor_buffer[4] = 0
        elif direction == 'left':
            motor_buffer[1] = 0
            motor_buffer[2] = analog_speed
            motor_buffer[3] = 0
            motor_buffer[4] = analog_speed
        else:  # left
            motor_buffer[1] = 0
            motor_buffer[2] = analog_speed
            motor_buffer[3] = 0
            motor_buffer[4] = analog_speed
        i2c.write(CHIP_ADDR, motor_buffer, False)
        if duration is not None:
            utime.sleep_ms(duration)
            self.stop()


class MOVEMotorLineSensors:

    def __init__(self):
        self.left_offset = 0
        self.right_offset = 0

    def line_sensor_calibrate(self):
        rightLineSensor = RIGHT_LINE_SENSOR_PIN.read_analog()
        leftLineSensor = LEFT_LINE_SENSOR_PIN.read_analog()
        offset = int(abs(rightLineSensor-leftLineSensor)/2)
        if leftLineSensor > rightLineSensor:
            self.left_offset = -offset
            self.right_offset = offset
        else:
            self.left_offset = offset
            self.right_offset = -offset

    def line_sensor_read(self, sensor):
        if sensor == 'left':
            return LEFT_LINE_SENSOR_PIN.read_analog() + self.left_offset
        elif sensor == 'right':
            return RIGHT_LINE_SENSOR_PIN.read_analog() + self.right_offset


class MOVEMotorDistanceSensors:

    def distance(self):
        ECHO_PIN.set_pull(ECHO_PIN.NO_PULL)
        TRIGGER_PIN.write_digital(0)
        utime.sleep_us(2)
        TRIGGER_PIN.write_digital(1)
        utime.sleep_us(10)
        TRIGGER_PIN.write_digital(0)
        distance = machine.time_pulse_us(ECHO_PIN, 1, 1160000)
        if distance > 0:
            # distance in cm
            return round(distance/58)
        else:
            return 0
