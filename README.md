# Pico Macro keyboard (CircuitPython)

## Installation

### Install CircuitPython 7+ on the Pico
* Download it from here: https://circuitpython.org/board/raspberry_pi_pico/
* Hold the BOOTSEL button while plugging in the Pico.
* Drop the CircuitPython.uf2 file in the Pico's CIRCUITPYTHON drive.

### Upload the code to the Pico
* Clone submodules etc.:
  ```bash
  $ ./install.sh
  Cloning external submodules/libs
  Copying external libs into pico libs folder
  ```
* Copy all files from the [pico](./pico) folder to your CircuitPython drive. And voilà!

## Usage
* Add mappings to config.json for the pins to key combinations
* Hold down GP0 upon boot to enable only-keyboard mode
