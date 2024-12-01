# Xpt-2046-driver-for-raspberry-pi
Use this library for touch with any xpt-2046 chip compatible display.
Use for Rpi 3 and up, including all Zero models

Gpio Pinout:

Raspberry Pi      Xpt2046 <br>

SCLK_1 (GPIO21) |	CLK <br>
CE_1 (GPIO17)	  | CS <br>
MOSI_1 (GPIO20)	| DIN <br>
MISO_1 (GPIO19)	| DO <br>
GPIO26	        | IRQ <br>

Instructions:
1. Paste code into /home/[your username]/touchmodule
2. Run python /home/[your username]/touchmodule/touch_ctr.py
3. Paste python /home/[your username]/touchmodule/touch_ctr.py & into /etc/rc.local


Tested with ILI9488 display and xpt2046 touch chip, should work on any display with touch.
