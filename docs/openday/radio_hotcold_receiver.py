from microbit import *
import radio

# Radio setup
radio.config(group=7)
radio.on()

# Smoothing + timeout
smooth_rssi = -95
last_packet_time = running_time()


def display_level(level):
    display.clear()

    # Clamp level between 0 and 5
    if level < 0:
        level = 0
    if level > 5:
        level = 5

    # Level 0 = no bars
    if level == 0:
        return

    # Light rows from bottom upward
    for i in range(level):
        row = 4 - i
        for x in range(5):
            display.set_pixel(x, row, 9)


while True:
    packet = radio.receive_full()
    now = running_time()

    if packet:
        msg, rssi, timestamp = packet
        last_packet_time = now

        # Smooth RSSI
        smooth_rssi = (smooth_rssi * 0.7) + (rssi * 0.3)

        # Map RSSI so:
        # -75 = 0 bars (≈1 meter)
        # -55 = 5 bars (≈2 cm)
        level = scale(int(smooth_rssi), from_=(-75, -55), to=(0, 5))

        # Hard cutoff for weak signals
        if smooth_rssi < -75:
            level = 0

        display_level(level)

    else:
        # No packets for 0.5 seconds → drop to zero
        if now - last_packet_time > 500:
            display_level(0)

    sleep(100)
