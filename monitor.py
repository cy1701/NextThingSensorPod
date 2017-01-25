#!/usr/bin/env python3

import os
import time
import subprocess
#import onewire
from w1thermsensor import W1ThermSensor
import paho.mqtt.client as mqtt
import CHIP_IO.GPIO as GPIO

GPIO.setup("CSID0", GPIO.IN)
GPIO.setup("CSID1", GPIO.IN)
mqttc = mqtt.Client()


mqttc.username_pw_set(username="user", password="pass")


if GPIO.input("CSID0"):
    print("HIGH")
else:
    print("LOW")



