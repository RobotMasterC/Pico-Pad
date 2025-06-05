import time
import board
import busio
import digitalio
import displayio
import terminalio
import usb_hid

from variables import * 

from adafruit_display_text import label
import adafruit_displayio_ssd1306

from adafruit_hid.keyboard import Keyboard
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode


key1  = [CTRL, SHIFT, Q]
key2  = [CTRL, Y]
key3  = [CTRL, C]
key4  = [CTRL, Z]
key5  = [CTRL, J]
key6  = [CTRL, X]
key7  = [ALT, TAB]
key8  = [GUI, SHIFT, S]
key9  = [CTRL, C]
key10 = [CTRL, V]

initial_delay = 0.4
repeat_rate = 0.05

displayio.release_displays()
i2c = busio.I2C(scl=board.GP1, sda=board.GP0)
display_bus = displayio.I2CDisplay(i2c, device_address=0x3C)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)

splash = displayio.Group()
display.root_group = splash

text_area = label.Label(terminalio.FONT, text="", color=0xFFFF00, x=10, y=28, scale=2)
splash.append(text_area)
splash.append(label.Label(terminalio.FONT, text="hc", color=0xFFFF00, x=110, y=5, scale=1))
splash.append(label.Label(terminalio.FONT, text="@Robilty", color=0xFFFF00, x=10, y=5, scale=1))

keyboard = Keyboard(usb_hid.devices)
cc = ConsumerControl(usb_hid.devices)

key_configs = [
    {'pin': board.GP10, 'keys': key1},
    {'pin': board.GP11, 'keys': key2},
    {'pin': board.GP12, 'keys': key3},
    {'pin': board.GP13, 'keys': key4},
    {'pin': board.GP14, 'keys': key5},
    {'pin': board.GP9, 'keys': key6},
    {'pin': board.GP16, 'keys': key7},
    {'pin': board.GP17, 'keys': key8},
    {'pin': board.GP18, 'keys': key9},
    {'pin': board.GP19, 'keys': key10},
]

for config in key_configs:
    btn = digitalio.DigitalInOut(config['pin'])
    btn.direction = digitalio.Direction.INPUT
    btn.pull = digitalio.Pull.UP
    config['button'] = btn
    config['held'] = False
    config['last_time'] = 0

CLK_PIN = board.GP4
DT_PIN = board.GP3
SW_PIN = board.GP2

clk = digitalio.DigitalInOut(CLK_PIN)
clk.direction = digitalio.Direction.INPUT

dt = digitalio.DigitalInOut(DT_PIN)
dt.direction = digitalio.Direction.INPUT

sw = digitalio.DigitalInOut(SW_PIN)
sw.direction = digitalio.Direction.INPUT
sw.pull = digitalio.Pull.UP

clk_last = clk.value

last_state = (clk.value, dt.value)

def voldown():
    print("Volume Down")
    cc.send(ConsumerControlCode.VOLUME_DECREMENT)

def volup():
    print("Volume Up")
    cc.send(ConsumerControlCode.VOLUME_INCREMENT)

def show_text_on_oled(message):
    text_area.text = message

def keycode_list_to_string(key_list):
    return "+".join(KEY_LABELS.get(k, str(k)) for k in key_list)

while True:
    now = time.monotonic()

    for config in key_configs:
        btn = config['button']
        if not btn.value: 
            if not config['held']:
                keyboard.press(*config['keys'])
                show_text_on_oled(keycode_list_to_string(config['keys']))
                config['last_time'] = now
                config['held'] = True
                keyboard.release_all()
            elif now - config['last_time'] >= initial_delay:
                keyboard.press(*config['keys'])
                show_text_on_oled(keycode_list_to_string(config['keys']))
                config['last_time'] = now - (initial_delay - repeat_rate)
                keyboard.release_all()
        else:
            config['held'] = False

    current_state = (clk.value, dt.value)
    
    if current_state != last_state:
        if last_state == (1, 0) and current_state == (0, 0):
            volup()
        elif last_state == (0, 1) and current_state == (0, 0):
            voldown()
        last_state = current_state

    time.sleep(0.001)
