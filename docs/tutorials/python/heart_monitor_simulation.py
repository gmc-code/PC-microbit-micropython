# heart_monitor_simulation
from microbit import *

hb1 = Image("00009:00009:00009:99999:00000")
hb2 = Image("00090:00090:00090:99999:00009")
hb3 = Image("00900:00900:00900:99999:00090")
hb4 = Image("09000:09000:09000:99999:00900")
hb5 = Image("90000:90000:90000:99999:09000")
hb6 = Image("00000:00000:00000:99999:90000")
hb7 = Image("00000:00000:00000:99999:00000")

heart_beat = [hb1, hb2, hb3, hb4, hb5, hb6, hb7]


def delay_for_heart_rate(hr=60):
    return int(60000/(hr * 7))


display.show(hb7)

while True:
    if pin0.is_touched():
        hr_delay = delay_for_heart_rate(60)
        display.show(heart_beat, delay=hr_delay, wait=True)
    elif pin1.is_touched():
        hr_delay = delay_for_heart_rate(100)
        display.show(heart_beat, delay=hr_delay, wait=True)
    elif pin2.is_touched():
        hr_delay = delay_for_heart_rate(150)
        display.show(heart_beat, delay=hr_delay, wait=True)

