echo "Cloning external submodules/libs"
git submodule update --init
echo "Copying external libs into pico libs folder"
ln -srf circuitpython-libs/Adafruit_CircuitPython_HID/adafruit_hid/ pico/libs/
