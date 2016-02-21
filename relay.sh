#!/bin/bash

# GPIO Control with Raspberry Pi

GPIOPORT=18
STATE=$(cat /sys/class/gpio/gpio$GPIOPORT/value)

echo $GPIOPORT > /sys/class/gpio/export
echo "out" > /sys/class/gpio/gpio$GPIOPORT/direction

if [ "$STATE" == "1" ]; then
    echo "0" > /sys/class/gpio/gpio$GPIOPORT/value
else
    echo "1" > /sys/class/gpio/gpio$GPIOPORT/value
fi
