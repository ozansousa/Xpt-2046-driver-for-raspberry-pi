# Xpt-2046-driver-for-raspberry-pi
Use this library for touch with any xpt-2046 chip compatible display.
Use for Rpi 3 and up, including all Zero models

Gpio Pinout:


<table>
  <tr>
    <th>Company</th>
    <th>Contact</th>
    <th>Country</th>
  </tr>
  <tr>
    <td>Alfreds Futterkiste</td>
    <td>Maria Anders</td>
    <td>Germany</td>
  </tr>
  <tr>
    <td>Centro comercial Moctezuma</td>
    <td>Francisco Chang</td>
    <td>Mexico</td>
  </tr>
  <tr>
    <td>Ernst Handel</td>
    <td>Roland Mendel</td>
    <td>Austria</td>
  </tr>
  <tr>
    <td>Island Trading</td>
    <td>Helen Bennett</td>
    <td>UK</td>
  </tr>
  <tr>
    <td>Laughing Bacchus Winecellars</td>
    <td>Yoshi Tannamuri</td>
    <td>Canada</td>
  </tr>
  <tr>
    <td>Magazzini Alimentari Riuniti</td>
    <td>Giovanni Rovelli</td>
    <td>Italy</td>
  </tr>
</table>
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
