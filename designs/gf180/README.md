
# Schematic Design

In this folder you will find all files related to schematic design and verification. Here we have implemented Xschem as user interface tool to run ngspice and design typical case, then using CACE to run PVT and MC simulations.

As mentioned in home, four designs were implemented to evaluate the proposed flow, all based on an OTA folded cascode topology with an N-type differential input and a single-ended output. The core amplifier circuit is shown here:

![Core Amplifier Schematic](../../img/Folded_core.png)

while the biasing circuit is presented as:

![Biasing Circuit Schematic](../../img/Folded_bias.png)

The concept behind this 4 versions is that the same circuit can be designed for different applications, requesting high gain and low offset, or requesting wide-band signal amplification. However, the layout structure may not change, even if devices dimentions change, placement and signal work may stay the same. 



The table below summarizes the key performance metrics obtained from pre and post-layout simulations for V1 design.


<table align="center">
  <thead>
    <tr>
      <th rowspan="2" align="center">Symbol</th>
      <th rowspan="2" align="center">Units</th>
      <th colspan="3" align="center">Spec</th>
      <th colspan="3" align="center">Schematic</th>
      <th colspan="3" align="center">Post-Layout</th>
    </tr>
    <tr>
      <th align="center">Min</th>
      <th align="center">Typ</th>
      <th align="center">Max</th>
      <th align="center">Min</th>
      <th align="center">Typ</th>
      <th align="center">Max</th>
      <th align="center">Min</th>
      <th align="center">Typ</th>
      <th align="center">Max</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td align="center">Temp</td>
      <td align="center">[°C]</td>
      <td align="center">-40</td>
      <td align="center">25</td>
      <td align="center">125</td>
      <td align="center">-40</td>
      <td align="center">25</td>
      <td align="center">125</td>
      <td align="center">-40</td>
      <td align="center">25</td>
      <td align="center">125</td>
    </tr>
    <tr>
      <td align="center">VDD</td>
      <td align="center">[V]</td>
      <td align="center">2.97</td>
      <td align="center">3.3</td>
      <td align="center">3.63</td>
      <td align="center">2.97</td>
      <td align="center">3.3</td>
      <td align="center">3.63</td>
      <td align="center">2.97</td>
      <td align="center">3.3</td>
      <td align="center">3.63</td>
    </tr>
    <tr>
      <td align="center">UGBW</td>
      <td align="center">[MHz]</td>
      <td align="center">10</td>
      <td align="center">--</td>
      <td align="center">--</td>
      <td align="center">11.1</td>
      <td align="center">26</td>
      <td align="center">53.9</td>
      <td align="center">10.1</td>
      <td align="center">20.8</td>
      <td align="center">47</td>
    </tr>
    <tr>
      <td align="center">Av</td>
      <td align="center">[dB]</td>
      <td align="center">70</td>
      <td align="center">--</td>
      <td align="center">--</td>
      <td align="center">75.9</td>
      <td align="center">81</td>
      <td align="center">82.8</td>
      <td align="center">75.8</td>
      <td align="center">80.6</td>
      <td align="center">82.7</td>
    </tr>
    <tr>
      <td align="center">PM</td>
      <td align="center">[°]</td>
      <td align="center">50</td>
      <td align="center">--</td>
      <td align="center">--</td>
      <td align="center">72.1</td>
      <td align="center">73</td>
      <td align="center">75.7</td>
      <td align="center">57.8</td>
      <td align="center">60.2</td>
      <td align="center">63.9</td>
    </tr>
    <tr>
      <td align="center">Voff(3Sig)</td>
      <td align="center">[mV]</td>
      <td align="center">--</td>
      <td align="center">--</td>
      <td align="center">10</td>
      <td align="center">--</td>
      <td align="center">--</td>
      <td align="center">14.1</td>
      <td align="center">--</td>
      <td align="center">--</td>
      <td align="center">3.5</td>
    </tr>
    <tr>
      <td align="center">CL</td>
      <td align="center">[pF]</td>
      <td align="center">--</td>
      <td align="center">5</td>
      <td align="center">--</td>
      <td align="center">--</td>
      <td align="center">5</td>
      <td align="center">--</td>
      <td align="center">--</td>
      <td align="center">5</td>
      <td align="center">--</td>
    </tr> 
  </tbody>
</table>