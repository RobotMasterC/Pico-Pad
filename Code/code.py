import time
import board
import busio
import digitalio
import displayio
import terminalio
import usb_hid

from adafruit_display_text import label
import adafruit_displayio_ssd1306

from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode

displayio.release_displays()
i2c = busio.I2C(scl=board.GP1, sda=board.GP0)
display_bus = displayio.I2CDisplay(i2c, device_address=0x3C)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)

splash = displayio.Group()
display.root_group = splash


text_area = label.Label(terminalio.FONT, text="", color=0xFFFF00, x=28, y=28, scale=2)
splash.append(text_area)

# Static "hc" label in top-right corner
hc_label = label.Label(terminalio.FONT, text="hc", color=0xFFFF00, x=110, y=5, scale=1)
splash.append(hc_label)

# Static "hc" label in top-right corner
hc_label = label.Label(terminalio.FONT, text="@Robilty", color=0xFFFF00, x=10, y=5, scale=1)
splash.append(hc_label)


cc = ConsumerControl(usb_hid.devices)
keyboard = Keyboard(usb_hid.devices)

button_copy = digitalio.DigitalInOut(board.GP21) 
button_copy.direction = digitalio.Direction.INPUT
button_copy.pull = digitalio.Pull.UP

button_paste = digitalio.DigitalInOut(board.GP22) 
button_paste.direction = digitalio.Direction.INPUT
button_paste.pull = digitalio.Pull.UP


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

def voldown():
    print("Volume Down")
    cc.send(ConsumerControlCode.VOLUME_DECREMENT)

def volup():
    print("Volume Up")
    cc.send(ConsumerControlCode.VOLUME_INCREMENT)

def show_text_on_oled(message):
    text_area.text = message

while True:
    if not button_copy.value:
        keyboard.press(Keycode.CONTROL, Keycode.C)
        show_text_on_oled("CTRL+C")
        time.sleep(0.2)
        keyboard.release_all()
    elif not button_paste.value:
        keyboard.press(Keycode.CONTROL,Keycode.V)
        show_text_on_oled("CTRL+V")
        time.sleep(0.2)
        keyboard.release_all()


    # Rotary encoder volume control
    clk_state = clk.value
    if clk_state != clk_last:
        if dt.value != clk_state:
            volup()
        else:
            voldown()
        clk_last = clk_state

    time.sleep(0.01)

