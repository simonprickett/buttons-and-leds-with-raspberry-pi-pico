import machine
import time
import utime

blue_led = machine.Pin(2, machine.Pin.OUT)
blue_btn = machine.Pin(4, machine.Pin.IN, machine.Pin.PULL_UP)

green_led = machine.Pin(7, machine.Pin.OUT)
green_btn = machine.Pin(9, machine.Pin.IN, machine.Pin.PULL_UP)

blue_last = time.ticks_ms()
green_last = time.ticks_ms()

def button_handler(pin):
    global blue_last, green_last, blue_btn, green_btn
      
    if pin is blue_btn:
        if time.ticks_diff(time.ticks_ms(), blue_last) > 500:
            blue_led.toggle()
            blue_last = time.ticks_ms()
    elif pin is green_btn:
        if time.ticks_diff(time.ticks_ms(), green_last) > 500:
            green_led.toggle()
            green_last = time.ticks_ms()

blue_led.value(0)
blue_btn.irq(trigger = machine.Pin.IRQ_RISING, handler = button_handler)
green_led.value(0)
green_btn.irq(trigger = machine.Pin.IRQ_RISING, handler = button_handler)

