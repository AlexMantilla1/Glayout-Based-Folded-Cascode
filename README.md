# Glayout-Based Folded-Cascode OTA Generator

[![License: GPL-3.0](https://img.shields.io/badge/License-GPL--3.0-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

This repository contains the necessary files for the semi-automatic layout generation of a Folded-Cascode Operational Transconductance Amplifier (OTA). The project is developed in Python using the **gLayout** framework and targets the **GlobalFoundries 180nm (gf180mcuD)** PDK.

The methodology involves defining parameterized functions for the circuit, which allows for the automatic generation of multiple layout variations by adjusting design parameters like transistor sizes and placement matrices.

---

## Table of Contents

1.  [Installation for Testing](#1-installation-for-testing)
2.  [Repository Structure](#2-files-inside-this-repo)
3.  [Design Specifications](#3-specifications-of-the-designed-folded-cascode)

---

## 1. Installation for Testing

This project is designed to run within the **IIC-OSIC-TOOLS** containerized environment, which provides all the necessary EDA tools.

### 1.1. Installing IIC-OSIC-TOOLS Container

First, ensure you have Docker installed. Then, pull and run the recommended container for this workflow. For detailed instructions, please refer to the official documentation [here](https://github.com/iic-jku/iic-osic-tools). In this specific work, the VNC interface has been used.

### 1.2. Installing IIC-OSIC-TOOLS Container

Once inside the container's shell, clone this repository to your working directory.

```bash
git clone https://github.com/AlexMantilla1/Glayout-Based-Folded-Cascode.git
cd Glayout-Based-Folded-Cascode
```

### 1.3. VS Code-Based Workflow with Glayout

This repository includes scripts to set up a self-contained Conda environment, ensuring all Python dependencies are managed correctly.

#### A. Install the Environment (Run Once)

Run the installation script. This will download Miniconda and create a dedicated environment with all the required packages (glayout, numpy, etc.).

```bash
./install_conda_env.sh
```

#### B. Activate the Environment (For Every New Session)

Before working on the project, source the setup script in your terminal. This activates the Conda environment.

```bash
. setup_glayout.sh
```

Your terminal prompt should now show (GLdev), indicating the environment is active.

#### C. Launch VS Code

For the best experience, launch VS Code from the activated terminal. This ensures the editor's terminal and Python extension will automatically use the correct (GLdev) environment.

```bash
# From the terminal where you sourced the setup script
code .
```

## 2. Files Inside This Repo

The repository is organized into design files and the Python-based layout generation scripts.

#### designs/gf180/:

Contains the schematic design and characterization files for the gf180nm PDK.

Xschem: Schematics for the OTA.

CACE: Files for circuit characterization and simulation.

#### glayout/:

Contains the Python source code for the layout generators. This is where the parameterized cells and routing logic are defined.

#### Files for Installing Dependencies:

install_conda_env.sh: The one-time installation script for the Conda environment.

setup_glayout.sh: The script to activate the Conda environment in a terminal session.

## 3. Specifications of the Designed Folded Cascode

Four designs were implemented to evaluate the proposed flow, all based on an OTA folded cascode topology with an N-type differential input and a single-ended output. The core amplifier circuit is shown here:

![Core Amplifier Schematic](img/Folded_core.png)

while the biasing circuit is presented as:

![Biasing Circuit Schematic](img/Folded_bias.png)


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
      <td align="center">--</td>
      <td align="center">1</td>
      <td align="center">5</td>
      <td align="center">--</td>
      <td align="center">--</td>
      <td align="center">--</td>
      <td align="center">--</td>
      <td align="center">--</td>
      <td align="center">--</td>
    </tr>
    <tr>
      <td align="center">Av</td>
      <td align="center">[dB]</td>
      <td align="center">--</td>
      <td align="center">--</td>
      <td align="center">--</td>
      <td align="center">--</td>
      <td align="center">--</td>
      <td align="center">--</td>
      <td align="center">--</td>
      <td align="center">--</td>
      <td align="center">--</td>
    </tr>
    <tr>
      <td align="center">PM</td>
      <td align="center">[°]</td>
      <td align="center">--</td>
      <td align="center">--</td>
      <td align="center">80</td>
      <td align="center">--</td>
      <td align="center">--</td>
      <td align="center">--</td>
      <td align="center">--</td>
      <td align="center">--</td>
      <td align="center">--</td>
    </tr>
    <tr>
      <td align="center">Voff</td>
      <td align="center">[mV]</td>
      <td align="center">-10</td>
      <td align="center">--</td>
      <td align="center">10</td>
      <td align="center">--</td>
      <td align="center">--</td>
      <td align="center">--</td>
      <td align="center">--</td>
      <td align="center">--</td>
      <td align="center">--</td>
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