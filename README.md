# Buttons and LEDs with the Raspberry Pi Pico

This is a quick demonstration of how to use [MicroPython](http://micropython.org/) to read button presses and control LEDs with the [Raspberry Pi Pico](https://www.raspberrypi.org/products/raspberry-pi-pico/).  This README is a work in progress, I'll update it with a wiring diagram etc as I make progress with an article about this project on [my website](https://simonprickett.dev/).

## Hardware Used

* 1 x Raspberry Pi Pico ([buy in UK](https://shop.pimoroni.com/products/raspberry-pi-pico) | [buy in USA](https://www.adafruit.com/product/4864)).
* 1 x Adafruit 24mm LED arcade button green ([buy in UK](https://thepihut.com/products/mini-led-arcade-button-24mm-green) | [buy in USA](https://www.adafruit.com/product/3433)).
* 1 x Adafruit 24mm LED arcade button blue ([buy in UK](https://thepihut.com/products/mini-led-arcade-button-24mm-translucent-blue) | [buy in USA](https://www.adafruit.com/product/3432)).
* 4 x Adafruit arcade button quick connect wires ([buy in UK](https://thepihut.com/products/arcade-button-quick-connect-wire-pairs-0-11-10-pack) | [buy in USA](https://www.adafruit.com/product/1152)) - optional, just means a little less soldering but you could use the wire below for all connections.  I used these for the button and LED connections on each button.
* Hook up wires, I like using single core ones (easier to poke through holes in circuit boards) but anything will do.  I used these for the ground connections for each button. ([buy in UK](https://thepihut.com/products/hook-up-wire-spool-set-22awg-solid-core-6-x-25-ft) | [buy in USA](https://www.adafruit.com/product/1311)).
* Soldering iron ([buy in UK](https://shop.pimoroni.com/products/antex-xs25-soldering-iron-uk-plug) | [buy in USA](https://www.adafruit.com/product/3685)).
* * USB A to micro USB cable (for programming, then powering the finished project) ([buy in UK](https://shop.pimoroni.com/products/usb-a-to-microb-cable-black) | [buy in USA](https://www.adafruit.com/product/2185)).
* Cardboard box (you don't need an enclosure, but it keeps everything together!  I also find plastic take out food containers work well for this stuff).

## Software Tools

I used [Thonny](https://thonny.org/) to edit the code and save it to the Pi Pico, because it has support for that.  I am not a fan of Thonny, and will look at ways to use a better editor such as [VS Code](https://code.visualstudio.com/) with the Pico in future.

## Software

I wrote the software in MicroPython.  This is a basic demo of how to detect a button press and toggle an LED in response to it.

I used a basic time delay debounce approach to the button press - waiting 500 milliseconds after a press was detected before allowing another one to register.

## Demonstration

Here's a GIF showing this project working:

![Project Demo Gif](https://i.makeagif.com/media/3-06-2021/GHc9dF.gif)
