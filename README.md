# Xpt-2046-driver-for-raspberry-pi
Use this library for touch with any xpt-2046 chip compatible display.
Use for Rpi 3 and up, including all Zero models

Gpio Pinout:


<table>
  <tr>
    <th>Raspberry Pi</th>
    <th>Xpt2046</th>
  </tr>
  <tr>
    <td>SCLK_1 (GPIO21)</td>
    <td>CS</td>
  </tr>
  <tr>
    <td>CE_1 (GPIO17)</td>
    <td>CLK</td>
  </tr>
  <tr>
    <td>MOSI_1 (GPIO20)</td>
    <td>DIN</td>
  </tr>
  <tr>
    <td>MISO_1 (GPIO19)</td>
    <td>DO </td>
  </tr>
  <tr>
    <td>GPIO26</td>
    <td>IRQ</td>
  </tr>
</table>

Instructions:
1. Install pyautogui with pip install pyautogui
2. Paste code into /home/[your username]/touchmodule
3. Fill in parameters in touch_ctr.py
4. Run python /home/[your username]/touchmodule/touch_ctr.py
5. Paste python /home/[your username]/touchmodule/touch_ctr.py & into /etc/rc.local


Tested with ILI9488 display and xpt2046 touch chip, should work on any display with touch.
