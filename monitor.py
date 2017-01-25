#!/usr/bin/env python3
########################################################
#
# Monitor program to send switch status and temp to
# MQTT proxy. 
#
#######################################################


import os
import time
import subprocess
from w1thermsensor import W1ThermSensor #https://github.com/timofurrer/w1thermsensor
import paho.mqtt.client as mqtt

import CHIP_IO.GPIO as GPIO
GPIO.setup("CSID0", GPIO.IN)
GPIO.setup("CSID1", GPIO.IN)

mqttc = mqtt.Client()


mqttc.username_pw_set(username="user", password="pass")

# Testing GPIO 
if GPIO.input("CSID0"):
    print("HIGH")
else:
    print("LOW")



